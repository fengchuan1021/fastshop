from sqlalchemy import select
from sqlalchemy.orm import Load

from Service.base import CRUDBase
import Models
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_

from Models import Shop,VariantShop,Variant

from modules.backend.sitewarehouse.InventoryShema import BackendSiteSetvariantsitestatusPostRequest


class VariantSiteService(CRUDBase[Models.VariantShop]):
    async def getproductsitestockdetail(self,db:AsyncSession,product_id:str)->list:
        #statment=select(Models.Variant).options(selectinload(Models.Variant.Images),joinedload(Models.Variant.Sites),undefer_group('en')).filter(Models.Variant.product_id == product_id)


        statment=select(Shop,Variant,VariantShop).select_from(Shop).join(Variant,Variant.product_id == product_id).outerjoin(VariantShop,and_(Shop.shop_id==VariantShop.shop_id,Variant.variant_id==VariantShop.variant_id))
        statment=statment.options(Load(Variant).load_only(Variant.image,Variant.sku,Variant.name_en),Load(Shop).load_only(Shop.shop_id,Shop.site_name,Shop.warehouse_id,Shop.warehouse_name)).order_by(Variant.variant_id)
        results=await (await db.connection()).execute(statment)
        return results.mappings().all()
        #sql=statment.compile()
        #tmp=await db.execute(str(sql),sql.params)#type: ignore
    async def setvariantsitestatus(self,db:AsyncSession,inobj:BackendSiteSetvariantsitestatusPostRequest)->dict:

        statment=select(VariantShop).filter(VariantShop.variant_id==inobj.variant_id,VariantShop.shop_id==inobj.shop_id)
        oldvariantsite=(await db.execute(statment)).scalar_one_or_none()
        if not oldvariantsite: #no old record. check insert
            if not inobj.price:
                return {"status": 'failed', 'msg': "must set the price"}
            if not inobj.warehouse_id:#not set the warehouse_id get from site
                site=await Service.siteService.findByPk(inobj.shop_id)
                if not site:
                    return {"status": 'failed', 'msg': "site not found"}
                inobj.warehouse_id=site.warehouse_id
                inobj.warehouse_name=site.warehouse_name
            model=VariantShop(**inobj.dict())
            db.add(model)
            try:
                await db.commit()
                return {"status": 'success', 'msg': "add ok"}
            except Exception as e:
                return {"status": 'failed', 'msg': "add failed"}
        else: #has old record update it
            oldvariantsite.warehouse_id=inobj.warehouse_id
            oldvariantsite.warehouse_name=inobj.warehouse_name
            if inobj.price:
                oldvariantsite.price=inobj.price
            if inobj.qty:
                oldvariantsite.qty=inobj.qty
            oldvariantsite.status=inobj.status
            try:
                await db.commit()
                return {"status": 'success', 'msg': "udpate ok"}
            except Exception as e:
                return {"status": 'failed', 'msg': "update failed"}


        pass




if __name__ == "__main__":
    print('11')
    from common.globalFunctions import async2sync
    from component.dbsession import getdbsession
    import Service
    async def test():#type: ignore
        async with getdbsession() as db:#type: ignore
            result=await Service.variantSiteService.getproductsitestockdetail(db,'87305569047680067')#type: ignore
            #print(result)


    async2sync(test)()