#type: ignore
import typing

from pydantic import BaseModel

import Service
import asyncio

from Models import Variant, Product
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List, Dict
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from common.filterbuilder import filterbuilder

from sqlalchemy.orm import undefer_group, joinedload

from sqlalchemy import select,text
from component.cache import cache
from component.snowFlakeId import snowFlack


class VariantService(CRUDBase[Models.Variant]):

    @cache(key_builder='getpkcachename',expire=3600*48)
    async def findByPk(self,dbSession: AsyncSession,id:int,lang:str='')->Models.Variant:
        if lang:
            statment=select(Models.Variant).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Variant).where(self.model.id==id)
        print(statment)
        results = await dbSession.execute(statment)
        return results.scalar_one_or_none()

    async def findByAttribute(self,dbsession:AsyncSession,filters:Dict={},sep:str=' and ',lang:str='en')->List[Models.Variant]:
        filter=filterbuilder(filters,sep)
        statment=select(self.model).where(text(filter))
        results=await dbsession.execute(statment)
        tmp=results.scalars().all()
        print('tmp::',tmp)
        return tmp



from modules.backend.product.ProductShema import BackendProductAddproductPostRequest
from modules.backend.product.ProductShema import Variant as VariantSchema
class ProductService(CRUDBase[Models.Product]):
    @cache(key_builder='getpkcachename', expire=3600 * 48)
    async def findByPk(self,db:AsyncSession,id:int,lang:str=''):
        if lang:
            statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Product).where(self.model.id==id)
        results = await db.execute(statment)
        return results.scalar_one_or_none()

    #for frontend show product detail. frontend shall use ssr generate static html.
    #only when cache missed,the function will be called.
    async def productdetailbyvariantid(self,db:AsyncSession,variantid:str):
        # statment=select(Product).select_from(Variant).join(Product,Product.product_id==Variant.product_id).filter(Variant.variant_id==variantid)
        # product=(await db.execute(statment)).scalar_one_or_none()
        # print(product)
        # variantsstatment=select(Variant).filter(Variant.product_id==product.product_id)
        # variants = (await db.execute(variantsstatment)).scalars().all()
        # print(variants)
        productidstatment= select(Variant.product_id).filter(Variant.variant_id == variantid).subquery()
        statment=select(Product).options(joinedload(Product.Variants)).filter(Product.product_id==productidstatment)

        result=(await db.execute(statment)).unique().scalar_one_or_none()
        print(result.json())
        return result




    async def addproduct(self,db:AsyncSession,inSchema:'BackendProductAddproductPostRequest')->Dict:
        #add to product table.
        dic = inSchema.dict(exclude={'attributes', 'specifications', 'subproducts'})

        dic['image'] = dic['image'][0]['image_url']
        productmodel = Models.Product(**dic)
        db.add(productmodel)



        #add variant
        #if inparams has no subproduct(variant),add proudct as itself's variant
        #every product must have a variant,search engine require this.

        variantarr = []
        if not inSchema.subproducts:
            tmpvariant=VariantSchema.parse_obj(inSchema)
            variantarr.append(tmpvariant)
        else:
            print('else::::')
            for subproduct in inSchema.subproducts:
                subproduct.brand_en=inSchema.brand_en
                subproduct.brand_id=inSchema.brand_id
                subproduct.status=inSchema.status
                subproduct.product_id=productmodel.product_id
                variantarr.append(subproduct)
        for variantShema in variantarr:
            print('????')
            variantmodel=Models.Variant(image=VariantSchema.image[0],**variantShema.dict(exclude={'image'}))

            for img in variantShema.image:
                imgmodel=Models.VariantImage(image_url=img.image_url,image_alt=img.image_alt)
                variantmodel.Images.append(imgmodel)

            db.add(variantmodel)


if __name__ == "__main__":
    pass
    from common.globalFunctions import async2sync
    from common.dbsession import getdbsession
    async def productdetailbyvariantid():
        async with getdbsession() as db:
            tmp=await Service.productService.productdetailbyvariantid(db,87318319723451458)
            print(tmp)
    async2sync(productdetailbyvariantid)()


