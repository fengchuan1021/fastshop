from typing import Dict, Any, List

from sqlalchemy.ext.asyncio import AsyncSession

import Models
import Service
from common.CurrencyRate import CurrencyRate
from component.snowFlakeId import snowFlack

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

async def addproducts(db:AsyncSession,products:List[Dict],store_id:int,merchant_id:int)->Any:
    productarr=[]
    variantarr=[]
    for json_data in products:
        product=Models.WishProduct()
        product.store_id=store_id
        product.merchant_id=merchant_id
        filloutProduct(product,json_data)
        productarr.append(product)
        for variant_json in json_data['variations']:
            variant=Models.WishVariant()
            variant.store_id=store_id
            variant.merchant_id=merchant_id
            filloutVariant(variant,variant_json,product)
            variantarr.append(variant)

    db.add_all(productarr)
    db.add_all(variantarr)
    await db.commit()

async def addOrders(db:AsyncSession,orders:List[Dict],store:Models.Store,merchant_id:int)->Any:
    order_arr=[]
    orderitem_arr=[]
    address_arr=[]#type: ignore

    status_dic={"SHIPPED":"SHIPPED","REFUNDED":"REFUNDED"}
    for json_data in orders:
        order=Models.Order()
        RATE = await CurrencyRate(order.order_currency_code)
        order.market_id=(await Service.thirdmarketService.getMarket('wish')).market_id
        order.market_name=(await Service.thirdmarketService.getMarket('wish')).market_name
        order.merchant_id=merchant_id
        order.merchant_name=store.merchant_name
        order.status=status_dic[json_data["state"]]

        order.order_currency_code=json_data["order_payment"]["general_payment_details"]["payment_total"]["currency_code"]
        order.grand_total = json_data["order_payment"]["general_payment_details"]["payment_total"]['amount']
        order.base_shipping_amount=json_data["order_payment"]["general_payment_details"]["shipping_merchant_payment"]['amount']*RATE
        order.shipping_amount = json_data["order_payment"]["general_payment_details"]["shipping_merchant_payment"][
                                         'amount']
        order.base_grand_total=order.grand_total*RATE
        order.currency_rate=RATE

        try:
            order.customer_firstname=json_data["full_address"]["shipping_detail"]["name"]
        except Exception as e:
            print(e)
        order.market_order_number=json_data["id"]
        order.discount_amount=json_data["order_payment"]["general_payment_details"]["product_price"]["amount"]-json_data["order_payment"]["general_payment_details"]["product_merchant_payment"]["amount"]
        order.base_discount_amount=order.discount_amount*RATE
        #order.tax_amount=json_data["tax_information"]["transaction_tax"]
        try:
            order.shipping_method=json_data["tracking_information"][0]["shipping_provider"]["name"]
        except Exception as e:
            print(e)

        order.total_item_count=json_data["order_payment"]["general_payment_details"]["product_quantity"]
        order.market_updatetime=json_data["updated_at"]

        order_arr.append(order)
        order_item=Models.OrderItem()
        order_item.order_id=order.order_id
        order_item.market_product_id=json_data["product_information"]['id']
        order_item.market_variant_id=json_data["product_information"]["variation_id"]
        order_item.sku=json_data["product_information"]["sku"]
        order_item.variant_name=json_data["product_information"]["name"]
        order_item.image=json_data["product_information"]["variation_image_url"]
        order_item.qty_ordered=order.total_item_count
        order_item.price=json_data["order_payment"]["general_payment_details"]["product_merchant_payment"]['amount']/order_item.qty_ordered
        order_item.base_price=order_item.price*RATE
        order_item.original_price=json_data["order_payment"]["general_payment_details"]["product_price"]['amount']
        order_item.base_original_price=order_item.original_price*RATE
        order_item.discount_amount=order_item.original_price-order_item.price#type: ignore
        order_item.base_discount_amount=order_item.discount_amount*RATE
        order_item.row_total=json_data["order_payment"]["general_payment_details"]["product_merchant_payment"]['amount']
        order_item.base_row_total=order_item.row_total*RATE

        orderitem_arr.append(order_item)

    db.add_all(order_arr)
    db.add_all(orderitem_arr)
    await db.commit()



