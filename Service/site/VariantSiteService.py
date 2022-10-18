from sqlalchemy import select, text
from sqlalchemy.engine import MappingResult
from sqlalchemy.orm import joinedload, undefer_group, selectinload, Load

from Service.base import CRUDBase
import Models
from typing import Union, Optional, Dict
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_


from component.cache import cache
from Models import Site,VariantSite,Variant
from sqlalchemy.sql.expression import literal
class VariantSiteService(CRUDBase[Models.VariantSite]):
    async def getproductsitestockdetail(self,db:AsyncSession,product_id:str)->MappingResult:
        #statment=select(Models.Variant).options(selectinload(Models.Variant.Images),joinedload(Models.Variant.Sites),undefer_group('en')).filter(Models.Variant.product_id == product_id)


        statment=select(Site,Variant,VariantSite).select_from(Site).join(Variant,Variant.product_id == product_id).outerjoin(VariantSite,and_(Site.site_id==VariantSite.site_id,Variant.variant_id==VariantSite.variant_id))
        statment=statment.options(Load(Variant).load_only(Variant.image,Variant.sku),Load(Site).load_only(Site.site_id,Site.site_name))
        sql=statment.compile()
        tmp=await db.execute(str(sql),sql.params)#type: ignore
        results=tmp.mappings()
        #results=(await (await db.connection()).execute(statment)).mappings()
        return results



if __name__ == "__main__":
    print('11')
    from common.globalFunctions import async2sync
    from common.dbsession import getdbsession
    import Service
    async def test():#type: ignore
        async with getdbsession() as db:#type: ignore
            result=await Service.variantSiteService.getproductsitestockdetail(db,'87305569047680067')#type: ignore
            #print(result)


    async2sync(test)()