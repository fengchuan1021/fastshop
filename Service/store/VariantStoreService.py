# from sqlalchemy import select
# from sqlalchemy.orm import Load
#
# from Service.base import CRUDBase
# import Models
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.sql import and_
#
# from Models import Store,VariantStore,Variant
#
# from modules.backend.sitewarehouse.InventoryShema import BackendSiteSetvariantsitestatusPostRequest
#
#
# class VariantSiteService(CRUDBase[Models.VariantStore]):
#     async def getproductsitestockdetail(self,db:AsyncSession,product_id:str)->list:
#         #statment=select(Models.Variant).options(selectinload(Models.Variant.Images),joinedload(Models.Variant.Sites),undefer_group('en')).filter(Models.Variant.product_id == product_id)
#
#
#         statment=select(Store,Variant,VariantStore).select_from(Store).join(Variant,Variant.product_id == product_id).outerjoin(VariantStore,and_(Store.store_id==VariantStore.store_id,Variant.variant_id==VariantStore.variant_id))
#         statment=statment.options(Load(Variant).load_only(Variant.image,Variant.sku,Variant.name_en),Load(Store).load_only(Store.store_id,Store.site_name,Store.warehouse_id,Store.warehouse_name)).order_by(Variant.variant_id)
#         results=await (await db.connection()).execute(statment)
#         return results.mappings().all()
#         #sql=statment.compile()
#         #tmp=await db.execute(str(sql),sql.params)#type: ignore
#     async def setvariantsitestatus(self,db:AsyncSession,inobj:BackendSiteSetvariantsitestatusPostRequest)->dict:
#
#         statment=select(VariantStore).filter(VariantStore.variant_id==inobj.variant_id,VariantStore.store_id==inobj.store_id)
#         oldvariantsite=(await db.execute(statment)).scalar_one_or_none()
#         if not oldvariantsite: #no old record. check insert
#             if not inobj.price:
#                 return {"status": 'failed', 'msg': "must set the price"}
#             if not inobj.warehouse_id:#not set the warehouse_id get from site
#                 site=await Service.siteService.findByPk(inobj.store_id)
#                 if not site:
#                     return {"status": 'failed', 'msg': "site not found"}
#                 inobj.warehouse_id=site.warehouse_id
#                 inobj.warehouse_name=site.warehouse_name
#             model=VariantStore(**inobj.dict())
#             db.add(model)
#             try:
#                 await db.commit()
#                 return {"status": 'success', 'msg': "add ok"}
#             except Exception as e:
#                 return {"status": 'failed', 'msg': "add failed"}
#         else: #has old record update it
#             oldvariantsite.warehouse_id=inobj.warehouse_id
#             oldvariantsite.warehouse_name=inobj.warehouse_name
#             if inobj.price:
#                 oldvariantsite.price=inobj.price
#             if inobj.qty:
#                 oldvariantsite.qty=inobj.qty
#             oldvariantsite.status=inobj.status
#             try:
#                 await db.commit()
#                 return {"status": 'success', 'msg': "udpate ok"}
#             except Exception as e:
#                 return {"status": 'failed', 'msg': "update failed"}
#
#
#         pass
#
#
#
#
# if __name__ == "__main__":
#     print('11')
#     from common.globalFunctions import cmdlineApp
#     from component.dbsession import getdbsession
#     import Service
#     async def test():#type: ignore
#         async with getdbsession() as db:#type: ignore
#             result=await Service.variantSiteService.getproductsitestockdetail(db,'87305569047680067')#type: ignore
#             #print(result)
#
#
#     cmdlineApp(test)()