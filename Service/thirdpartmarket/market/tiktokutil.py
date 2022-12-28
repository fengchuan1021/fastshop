from typing import Dict, Any, List

from sqlalchemy.ext.asyncio import AsyncSession
import datetime
import Models
import Service
from common.CurrencyRate import CurrencyRate
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
            print(35,json_data)
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
    try:
        variant.warehouse_id=variant_json["stock_infos"][0]["warehouse_id"]
        variant.inventory=variant_json["stock_infos"][0]["available_stock"]
    except Exception as e:
        pass



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

async def addOrders(db:AsyncSession,orders:List[Dict],store:Models.Store,merchant_id:int)->Any:

    order_arr=[]
    orderitem_arr=[]
    address_arr=[]
    shippment_arr=[]#type: ignore
    shippmentItem_arr=[]#type: ignore
    status_dic={111:"AWAITING_SHIPMENT",100:'UNPAID',112:'AWAITING_COLLECTION',114:'PARTIALLY_SHIPPING',121:'IN_TRANSIT',122:'DELIVERED',130:'COMPLETED',140:'CANCELLED',
                998:"REQUIRE_REVIEW",
                999:"REQUIRE_PLATFORM_REVIEW"}
    for json_data in orders:
        order=Models.Order()
        order.store_id = store.store_id
        order.store_name = store.store_name
        order.order_currency_code = json_data["payment_info"]["currency"]
        RATE=await CurrencyRate(order.order_currency_code)
        order.market_id=(await Service.thirdmarketService.getMarket('tiktok')).market_id
        order.market_name=(await Service.thirdmarketService.getMarket('tiktok')).market_name
        order.merchant_id=merchant_id
        order.merchant_name=store.merchant_name
        order.customer_note=json_data["buyer_message"]
        order.customer_id=json_data["buyer_uid"]
        order.currency_rate=RATE
        #"cancel_order_sla"
        order.market_createtime=datetime.datetime.fromtimestamp(float(json_data["create_time"])/1000,tz=datetime.timezone.utc)
        #"delivery_option": "SEND_BY_SELLER",
        order.market_delivery_option=json_data["delivery_option"]

        order.status=status_dic[json_data["order_status"]]
        try:
            order.customer_firstname=json_data["recipient_address"]['name']
        except Exception as e:
            print(100,e)

        order.market_order_id = json_data["order_id"]

        #payment info
        order.grand_total=json_data['payment_info']["total_amount"]

        order.base_grand_total = order.grand_total*RATE
        order.discount_amount=json_data["payment_info"]["seller_discount"]
        order.base_discount_amount = json_data["payment_info"]["seller_discount"]*RATE
        order.tax_amount=json_data["payment_info"]["taxes"]
        order.base_tax_amount = order.tax_amount*RATE




        try:
            order.paied_time=datetime.datetime.fromtimestamp(json_data['paid_time']/1000,tz=datetime.timezone.utc)
            order.payment_method = json_data['payment_method']
            pass
        except Exception as e:
            print(121,e)

        order.total_item_count=1
        order.market_updatetime=datetime.datetime.fromtimestamp(json_data["update_time"],tz=datetime.timezone.utc)
        order_arr.append(order)

        #添加收货地址
        if "recipient_address" in json_data:
            address=Models.ShipOrderAddress()
            address.is_tmp='Y'
            address.order_id=order.order_id

            address.street=json_data["recipient_address"]["address_detail"]
            address.city=json_data["recipient_address"]["city"]
            address.district=json_data["recipient_address"]["district"]
            address.full_address=json_data['recipient_address']["full_address"]
            address.firstname=json_data['recipient_address']['name']
            address.telephone=json_data['recipient_address']['phone']
            address.country=json_data['recipient_address']["region"]
            address.country_code=json_data['recipient_address']["region_code"]
            address.postcode=json_data['recipient_address']['zipcode']
            address.region=json_data['recipient_address']['state']
            address_arr.append(address)

        #添加发货
        if "package_list" in json_data:
            for package_data in json_data["package_list"]:
                package_detail=await Service.tiktokService.getPackageDetail(db,store,package_data["package_id"])
                shippment=Models.OrderShipment()
                shippment.order_id=order.order_id
                shippment.total_qty=sum([int(item["quantity"]) for order in package_detail["order_info_list"] for item in order["sku_list"]])
                shippment.shipping_address_id=address.shiporder_address_id
                shippment.track_number=package_detail["tracking_number"]
                try:
                    shippment.carrier_name=package_detail["shipping_provider"]
                    shippment.track_number=package_detail["tracking_number"]
                    shippment.market_package_id=package_detail["package_id"]
                    shippment.package_status=package_detail["package_status"]
                except Exception as e:
                    print(160,e)
                shippment.market_updatetime=datetime.datetime.fromtimestamp(package_detail["update_time"],datetime.timezone.utc)
                shippment_arr.append(shippment)
                #添加order_shipment_item
                for order_sku_info in package_detail["order_info_list"]:
                    for sku_info in order_sku_info["sku_list"]:
                        shipmentItem=Models.OrderShipmentItem()
                        shipmentItem.order_shipment_id=shippment.order_shipment_id
                        shipmentItem.market_order_id=order_sku_info["order_id"]
                        shipmentItem.order_id=order.order_id
                        shipmentItem.qty=sku_info["quantity"]
                        shipmentItem.name=sku_info["sku_name"]
                        shipmentItem.market_sku_id=sku_info["sku_id"]
                        shippmentItem_arr.append(shipmentItem)





        #添加order item
        for item in json_data["item_list"]:
            order_item=Models.OrderItem()
            order_item.order_id=order.order_id
            order_item.market_variant_id=item["sku_id"]
            order_item.market_product_id=item["product_id"]
            order_item.sku=item["seller_sku"]
            order_item.product_name=item["product_name"]
            order_item.qty_ordered=item["quantity"]
            order_item.image=item["sku_image"]
            order_item.variant_name=item['sku_name']
            order_item.price=item["sku_sale_price"]
            order_item.original_price = item["sku_original_price"]
            order_item.base_original_price=item["sku_original_price"]*RATE
            order_item.base_price=item["sku_sale_price"]*RATE
            order_item.discount_amount=item["sku_seller_discount"]
            order_item.base_discount_amount=item["sku_seller_discount"]*RATE
            order_item.row_total=item["sku_sale_price"]*item["quantity"]
            order_item.base_row_total=item["sku_sale_price"]*item["quantity"]*RATE

            orderitem_arr.append(order_item)


    db.add_all(order_arr)
    db.add_all(orderitem_arr)
    db.add_all(address_arr)
    db.add_all(shippment_arr)
    db.add_all(shippmentItem_arr)




