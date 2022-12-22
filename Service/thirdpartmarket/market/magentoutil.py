from typing import List, Dict, Any, Iterable

from sqlalchemy.ext.asyncio import AsyncSession

import Models
def filloutProduct(product:Models.MagentoProduct,json_data:Dict)->Any:
    product.name=json_data['name']
    product.magento_id=json_data['id']
    product.sku=json_data['sku']
    print(json_data)
    try:
        product.price=json_data['price']
    except Exception as e:
        pass
    product.status=json_data['status']
    product.visibility=json_data['visibility']
    product.market_created_at=json_data['created_at']
    product.market_updated_at=json_data['updated_at']
    product.main_image=json_data["media_gallery_entries"][0]["file"]
    for tmp in json_data["custom_attributes"]:
        if tmp["attribute_code"]=='url_key':
            product.url_key=tmp['value']
        elif tmp["attribute_code"]=="description":
            product.description=tmp['value']
async def addproducts(db:AsyncSession,products:Iterable[Dict],store_id:int,merchant_id:int)->Any:
    productarr=[]

    for json_data in products:
        product=Models.MagentoProduct()
        product.store_id=store_id
        product.merchant_id=merchant_id
        filloutProduct(product,json_data)
        productarr.append(product)

    db.add_all(productarr)

    await db.commit()