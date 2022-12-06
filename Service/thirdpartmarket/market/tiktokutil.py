from typing import Dict, Any, List

from sqlalchemy.ext.asyncio import AsyncSession
import datetime
import Models
import Service
from component.snowFlakeId import snowFlack



def filloutProduct(product:Models.TiktokProduct,json_data:Dict)->Any:

    product.market_updated_at =datetime.datetime.fromtimestamp(json_data["update_time"]/1000,datetime.timezone.utc)
    product.name=json_data["product_name"]
    if 1:
    #try:


        product.category_ids=','.join([str(tmp['id']) for tmp in json_data["category_list"]])
        product.category_names = ','.join([tmp["local_display_name"] for tmp in json_data["category_list"]])
        product.market_create_time=datetime.datetime.fromtimestamp(json_data["create_time"]/1000,datetime.timezone.utc)
        product.description=json_data['description']
        product.images=','.join([ tmp["thumb_url_list"][0] for tmp in json_data["images"]])
        product.package_height=json_data['package_height']
        product.package_weight=json_data['package_weight']
        product.package_length=json_data['package_length']
        product.package_width=json_data['package_width']
        product.market_product_id=json_data["product_id"]
        product.status = json_data['product_status']
        try:
            product.brand_id = json_data['brand']['id']
            product.brand_name = json_data['brand']['name']
        except Exception as e:
            print(json_data)
    # except Exception as e:
    #     print(e)
    #     pass

def filloutVariant(variant:Models.TiktokVariant,variant_json:Dict,product:Models.TiktokProduct)->Any:
    variant.tiktokproduct_id = product.tiktokproduct_id

    variant.sku = variant_json["seller_sku"]

    variant.market_product_id= product.market_product_id
    variant.price = variant_json['price']["original_price"]
    variant.currency_code = variant_json['price']["currency"]
    variant.market_varant_id=variant_json['id']



async def addproducts(db:AsyncSession,products:List[Dict],store_id:int,merchant_id:int)->Any:
    productarr=[]
    variantarr=[]
    for json_data in products:
        product=Models.TiktokProduct()
        product.store_id=store_id
        product.merchant_id=merchant_id
        filloutProduct(product,json_data)
        productarr.append(product)
        for variant_json in json_data['skus']:
            variant=Models.TiktokVariant()
            variant.store_id=store_id
            variant.merchant_id=merchant_id
            filloutVariant(variant,variant_json,product)
            variantarr.append(variant)

    db.add_all(productarr)
    db.add_all(variantarr)
    await db.commit()

async def addOrders(db:AsyncSession,orders:List[Dict],store_id:int,merchant_id:int)->Any:
    order_arr=[]
    orderitem_arr=[]
    status_dic={"SHIPPED":"SHIPPED"}
    for json_data in orders:
        order=Models.Order()
        order.market_id=(await Service.thirdmarketService.getMarket('tiktok')).market_id
        order.market_name=(await Service.thirdmarketService.getMarket('tiktok')).market_name
        order.merchant_id=merchant_id
        order.merchant_name=(await Service.merchantService.findByPk(merchant_id)).merchant_name
        order.status=status_dic[json_data["state"]]
        order.order_currency_code=json_data["general_payment_details"]["payment_total"]["currency_code"]

        order.market_order_number=json_data["id"]
        try:
            order.shipping_method=json_data["tracking_information"][0]["shipping_provider"]["name"]
        except Exception as e:
            print(e)
        order.base_grand_total=json_data["general_payment_details"]["payment_total"]['amount']
        order.total_item_count=1
        order.market_updatetime=json_data["updated_at"]

        order_arr.append(order)
        order_item=Models.OrderItem()
        order_item.order_id=order.order_id
        order_item.product_id=json_data["product_information"]['id']
        order_item.variant_id=json_data["product_information"]["variation_id"]
        order_item.sku=json_data["product_information"]["sku"]
        order_item.name=json_data["product_information"]["name"]
        order_item.image=json_data["product_information"]["name"]
        orderitem_arr.append(order_item)

    db.add_all(order_arr)
    db.add_all(orderitem_arr)
    await db.commit()



