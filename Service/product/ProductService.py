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
    async def productdetailbyvariantid(self,db:AsyncSession,variantid:str,lang='en'):

        productidstatment= select(Variant.product_id).filter(Variant.variant_id == variantid).subquery()
        statment=select(Product).options(undefer_group(lang).joinedload(Product.Variants).undefer_group(lang).joinedload(Variant.Images)).filter(Product.product_id==productidstatment)
        result=(await db.execute(statment)).unique().scalar_one_or_none()
        return result




    async def addproduct(self,db:AsyncSession,inSchema:'BackendProductAddproductPostRequest')->Dict:
        #add to product table.
        dic = inSchema.dict(exclude={'attributes', 'specifications', 'subproduct','category'})

        dic['image'] = dic['image'][0]['image_url']
        productmodel = Models.Product(**dic)
        db.add(productmodel)

        for specification in inSchema.specifications:
            specifmodel=Models.ProductSpecification(product_id=productmodel.product_id,
                                                    preattrspecific_id=11,
                                                    specificationname_en=specification.name,
                                                    specificationvalue_en=','.join(specification.value)
                                                    )
            db.add(specifmodel)

        for attribute in inSchema.attributes:
            model=Models.ProductAttribute(
                product_id=productmodel.product_id,
                attributename_en=attribute.name,
                attributevalue_en=attribute.value
            )
            db.add(model)

        for cat in inSchema.category:
            mode=Models.ProductCategory(category_id=cat,product_id=productmodel.product_id)
            db.add(mode)
        #add variant
        #if inparams has no subproduct(variant),add proudct as itself's variant
        #every product must have a variant,search engine require this.

        variantarr = []
        if not inSchema.subproduct:
            tmpvariant=VariantSchema.parse_obj(inSchema)
            variantarr.append(tmpvariant)
        else:
            print('else::::')
            for subproduct in inSchema.subproduct:
                subproduct.brand_en=inSchema.brand_en
                subproduct.brand_id=inSchema.brand_id
                subproduct.status=inSchema.status
                subproduct.product_id=productmodel.product_id
                variantarr.append(subproduct)
        for variantShema in variantarr:
            print('????')
            variantmodel=Models.Variant(image=variantShema.image[0].image_url,**variantShema.dict(exclude={'image'}))

            for img in variantShema.image:
                imgmodel=Models.VariantImage(image_url=img.image_url,image_alt=img.image_alt)
                variantmodel.Images.append(imgmodel)

            db.add(variantmodel)


if __name__ == "__main__":
    pass
    from common.globalFunctions import async2sync, toJson
    from common.dbsession import getdbsession
    async def productdetailbyvariantid():
        async with getdbsession() as db:
            tmp=await Service.productService.productdetailbyvariantid(db,87318319723451458,'cn')
            print(tmp)
    async2sync(productdetailbyvariantid)()


