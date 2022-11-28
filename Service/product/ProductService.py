# import Service
# from Models import Variant, Product
# from Service.base import CRUDBase
# import Models
# from typing import List, Dict
# from sqlalchemy.ext.asyncio import AsyncSession
# from common import filterbuilder
# from sqlalchemy.orm import undefer_group
# from sqlalchemy import select,text
# from component.cache import cache
# from modules.backend.product.ProductShema import BackendProductAddproductPostRequest
# from modules.backend.product.ProductShema import Variant as VariantSchema
#
# class VariantService(CRUDBase[Models.Variant]):
#
#     @cache(key_builder='getpkcachename',expire=3600*48)#type: ignore
#     async def findByPk(self,dbSession: AsyncSession,id:int,lang:str='')->Models.Variant:
#         if lang:
#             statment=select(Models.Variant).options(undefer_group(lang)).where(self.model.id==id)
#         else:
#             statment = select(Models.Variant).where(self.model.id==id)
#         print(statment)
#         results = await dbSession.execute(statment)
#         return results.scalar_one_or_none()#type: ignore
#
#     async def findByAttribute(self,dbsession:AsyncSession,filters:Dict={},sep:str=' and ',lang:str='en')->List[Models.Variant]:
#         filter=filterbuilder(filters,sep)
#         statment=select(self.model).where(text(filter))#type: ignore
#         results=await dbsession.execute(statment)
#         tmp=results.scalars().all()
#         print('tmp::',tmp)
#         return tmp
#
#
#
#
# class ProductService(CRUDBase[Models.Product]):
#
#     @cache(key_builder='getpkcachename', expire=3600 * 48)#type: ignore
#     async def findByPk(self,db:AsyncSession,id:int,lang:str='*')->Product:
#         if lang:
#             statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
#         else:
#             statment = select(Models.Product).where(self.model.id==id)
#         results = await db.execute(statment)
#         return results.scalar_one_or_none()#type:ignore
#
#
#     async def productdetailbyvariantid(self,db:AsyncSession,variantid:str,lang:str='en')->Product:
#         # for frontend show product detail. frontend shall use ssr generate static html.
#         # only when cache missed,the function will be called.
#         productidstatment= select(Variant.product_id).filter(Variant.variant_id == variantid).subquery()
#         statment=select(Product).options(undefer_group(lang).joinedload(Product.Variants).undefer_group(lang).joinedload(Variant.Images)).filter(Product.product_id==productidstatment)
#         result=(await db.execute(statment)).unique().scalar_one_or_none()
#         return result #type: ignore
#
#
#
#
#     async def addproduct(self,db:AsyncSession,inSchema:'BackendProductAddproductPostRequest')->Dict:
#         #add to product table.
#         dic = inSchema.dict(exclude={'attributes', 'specifications', 'subproduct','category'})
#
#         dic['image'] = dic['image'][0]['image_url']
#         productmodel = Models.Product(**dic)
#         db.add(productmodel)
#
#         for specification in inSchema.specifications:#type: ignore
#             specifmodel=Models.ProductSpecification(product_id=productmodel.product_id,
#                                                     preattrspecific_id=11,
#                                                     specificationname_en=specification.name,
#                                                     specificationvalue_en=','.join(specification.value)
#                                                     )
#             db.add(specifmodel)
#
#         for attribute in inSchema.attributes:#type: ignore
#             model=Models.ProductAttribute(
#                 product_id=productmodel.product_id,
#                 attributename_en=attribute.name,
#                 attributevalue_en=attribute.value
#             )
#             db.add(model)
#
#         for cat in inSchema.category:
#             mode=Models.ProductCategory(category_id=cat,product_id=productmodel.product_id)#type: ignore
#             db.add(mode)
#         #add variant
#         #if inparams has no subproduct(variant),add proudct as itself's variant
#         #every product must have a variant,search engine require this.
#
#         variantarr = []
#         if not inSchema.subproduct:
#             tmpvariant=VariantSchema.parse_obj(inSchema)
#             variantarr.append(tmpvariant)
#         else:
#             print('else::::')
#             for subproduct in inSchema.subproduct:
#                 subproduct.brand_en=inSchema.brand_en
#                 subproduct.brand_id=inSchema.brand_id
#                 subproduct.status=inSchema.status
#                 subproduct.product_id=productmodel.product_id#type: ignore
#                 variantarr.append(subproduct)
#         for variantShema in variantarr:
#             print('????')
#             variantmodel=Models.Variant(image=variantShema.image[0].image_url,**variantShema.dict(exclude={'image'}))
#
#             for img in variantShema.image:
#                 imgmodel=Models.VariantImage(image_url=img.image_url,image_alt=img.image_alt)
#                 variantmodel.Images.append(imgmodel)
#
#             db.add(variantmodel)
#         return {'status':'success'}
#
# if __name__ == "__main__":
#     pass
#     from common.globalFunctions import cmdlineApp
#     from component.dbsession import getdbsession
#     async def productdetailbyvariantid()->None:
#         async with getdbsession() as db:
#             tmp=await Service.productService.productdetailbyvariantid(db,87318319723451458,'cn')
#             print(tmp)
#     cmdlineApp(productdetailbyvariantid)()
#
#
