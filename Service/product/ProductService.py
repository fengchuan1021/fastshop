#type: ignore
import typing

from pydantic import BaseModel

import Service
import asyncio
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List, Dict
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from common.filterbuilder import filterbuilder

from sqlalchemy.orm import undefer_group

from sqlalchemy import select,text
from component.cache import cache

if typing.TYPE_CHECKING:
    from modules.backend.product.ProductShema import BackendProductAddproductPostRequest



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




class ProductService():
    @cache(key_builder='getpkcachename', expire=3600 * 48)
    async def findByPk(self,db:AsyncSession,id:int,lang:str=''):
        if lang:
            statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Product).where(self.model.id==id)
        results = await db.execute(statment)
        return results.scalar_one_or_none()

    async def addtovariant_table(self,db:AsyncSession,inSchema:'BackendProductAddproductPostRequest'):
        Variant = Models.Variant(**inSchema.dict(exclude={'stock', 'attributes', 'subproduct', 'images'}))

        VariantDynamic = Models.VariantDynamic(**inSchema.dict(include={'stock'}))

    async def addproduct(self,db:AsyncSession,inSchema:'BackendProductAddproductPostRequest')->Dict:
        #add to product table.
        dic = inSchema.dict(exclude={'attributes', 'specifications', 'subproduct'})
        if isinstance(dic['image'], list):
            dic['image'] = dic['image'][0]
        productmodel = Models.Product(**dic)
        db.add(productmodel)



        #add variant
        #variant split to 2 table,one for static column,one for dynamic Column

        #if inparams has no subproduct(variant),add proudct as itself's variant
        #every product must have a variant,search engine require this.

        if not inSchema.subproduct:

            await Service.VariantService.create(inSchema)
            await Service.variantDynamicService.create(inSchema)
        else:
            variantarr = []
            for subproduct in inSchema.subproducts:
                subproduct.brand_en=inSchema.brand_en
                subproduct.brand_id=inSchema.brand_id
                subproduct.status=inSchema.status
                subproduct.product_id=productmodel.product_id


        Variant=Models.Variant(**inSchema.dict(exclude={'stock','attributes','subproduct','images'}))

        VariantDynamic=Models.VariantDynamic(**inSchema.dict(include={'stock'}))

        for attribute in inSchema.attributes:
            Variant.images.append(Models.ProductAttribute(**attribute.dict()))

        db.add(Variant)
        db.add(VariantDynamic)

if __name__ == "__main__":
    pass
    # from common.globalFunctions import async2sync
    # from common.dbsession import getdbsession
    # async def findbyproductpk():
    #     async with getdbsession() as db:
    #         tmp=await Service.productService.findByPk(db,68451662070547522)
    #         print(tmp)
    # async2sync(findbyproductpk)()


