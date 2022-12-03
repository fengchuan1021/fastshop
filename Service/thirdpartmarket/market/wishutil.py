from typing import Dict, Any

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
