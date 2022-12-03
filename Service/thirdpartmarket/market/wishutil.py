from typing import Dict, Any, List

from sqlalchemy.ext.asyncio import AsyncSession

import Models
import Service
from component.snowFlakeId import snowFlack


async def addorupdateproduct(db:AsyncSession,wishProduct:Dict,ourid:int=0)->Any:
    if ourid:
        product=await Service.wishproductService.findByPk(ourid)
    else:
        product = Models.WishProduct()
        product.wishproduct_id = snowFlack.getId()

    product.subcategory_id = wishProduct['subcategory_id']
    product.updated_at = wishProduct['updated_at']
    product.num_sold = wishProduct['num_sold']
    product.wish_id = wishProduct['id']
    product.category = wishProduct['category']
    product.is_promoted = wishProduct['is_promoted']
    product.status = wishProduct['status']
    product.description = wishProduct['description']
    product.tags = ','.join(wishProduct['tags'])
    product.num_saves = wishProduct['num_saves']
    product.is_csp_enabled = wishProduct['is_csp_enabled']
    product.extra_images = ','.join(wishProduct['extra_images'])
    product.category_experience_eligibility = wishProduct['category_experience_eligibility']
    product.main_image = wishProduct['main_image']['url']
    product.name = wishProduct['name']
    product.created_at = wishProduct['created_at']
    for wishVariant in wishProduct['variations']:

        if not ourid:
            variant = Models.WishVariant()
        else:
            variant = await Service.wishvariantService.findOne(Models.WishVariant.wish_id==wishVariant['id'])#type: ignore
            if not variant:
                variant = Models.WishVariant()

        variant.wishproduct_id = product.wishproduct_id
        variant.status = wishVariant['status']
        variant.sku = wishVariant['sku']
        variant.product_id = wishProduct['id']
        variant.price = wishVariant['price']['amount']
        variant.currency_code = wishVariant['price']['currency_code']
        variant.cost_price = wishVariant['cost']['amount']
        variant.cost_currency_code = wishVariant['cost']['currency_code']
        variant.gtin = wishVariant['gtin']
        variant.wish_id = wishVariant['id']
        db.add(variant)
    if ourid:
        #todo delete not used variant
        pass
    db.add(product)
    await db.flush()
    await db.commit()
def filloutProduct(product:Models.WishProduct,json_data:Dict)->Any:
    product.subcategory_id = json_data['subcategory_id']
    product.updated_at = json_data['updated_at']
    product.num_sold = json_data['num_sold']
    product.wish_id = json_data['id']
    product.category = json_data['category']
    product.is_promoted = json_data['is_promoted']
    product.status = json_data['status']
    product.description = json_data['description']
    product.tags = ','.join(json_data['tags'])
    product.num_saves = json_data['num_saves']
    product.is_csp_enabled = json_data['is_csp_enabled']
    product.extra_images = ','.join(json_data['extra_images'])
    product.category_experience_eligibility = json_data['category_experience_eligibility']
    product.main_image = json_data['main_image']['url']
    product.name = json_data['name']
    product.created_at = json_data['created_at']
def filloutVariant(variant:Models.WishVariant,variant_json:Dict,product:Models.WishProduct)->Any:
    variant.wishproduct_id = product.wishproduct_id
    variant.status = variant_json['status']
    variant.sku = variant_json['sku']
    variant.product_id = product.wish_id
    variant.price = variant_json['price']['amount']
    variant.currency_code = variant_json['price']['currency_code']
    variant.cost_price = variant_json['cost']['amount']
    variant.cost_currency_code = variant_json['cost']['currency_code']
    variant.gtin = variant_json['gtin']
    variant.wish_id = variant_json['id']

async def addproducts(db:AsyncSession,products:List[Dict])->Any:
    productarr=[]
    variantarr=[]
    for json_data in products:
        product=Models.WishProduct(wishproduct_id = snowFlack.getId())
        filloutProduct(product,json_data)
        productarr.append(product)
        for variant_json in json_data['variations']:
            variant=Models.WishVariant(wishvariant_id=snowFlack.getId())
            filloutVariant(variant,variant_json,product)
            variantarr.append(variant)

    db.add_all(productarr)
    db.add_all(variantarr)
    await db.commit()


