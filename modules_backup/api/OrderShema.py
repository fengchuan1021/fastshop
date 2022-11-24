#   timestamp: 2022-10-29T02:15:05+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class ApiOrdersDetailQueryPostRequest(BaseModel):
    order_id_list: Optional[List[str]] = None


class PaymentInfo(BaseModel):
    currency: Optional[str] = Field(None, description='Currency for payment.<br>')


class RecipientAddress(BaseModel):
    full_address: Optional[str] = Field(
        None, description='Address with detailed info.<br><br>'
    )
    region: Optional[str] = Field(
        None,
        description='For orders with masked region, please refer to the "region" field of GetAuthorizedShop. One shop_id has only one region.<br>',
    )
    state: Optional[str] = Field(None, description='')
    city: Optional[str] = Field(None, description='')
    district: Optional[str] = Field(None, description='')
    town: Optional[str] = Field(None, description='')
    phone: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    zipcode: Optional[str] = Field(None, description='')
    address_detail: Optional[str] = Field(None, description='')
    address_line_list: Optional[List[str]] = None
    region_code: Optional[str] = Field(None, description='region code')


class ItemListItem(BaseModel):
    sku_id: Optional[str] = Field(None, description='Sku id<br>')
    product_id: Optional[str] = Field(
        None, description='Product id. (origin is item id)<br>'
    )
    sku_name: Optional[str] = Field(None, description='Sku properties<br>')
    quantity: Optional[int] = Field(None, description='Quantity of sku.<br>')
    seller_sku: Optional[str] = Field(
        None, description='Seller input sku in order snapshot<br>'
    )
    product_name: Optional[str] = Field(None, description='Product name.<br>')
    sku_image: Optional[str] = Field(
        None, description='Sku image in order snapshot<br><br>'
    )
    sku_ext_status: Optional[int] = Field(
        None,
        description='The corresponding status of SKU for the scenario of buyer-request cancellation. <br>NONE_CANCELLATION = 0;<br>CANCEL_PENDING = 201;  <br>CANCEL_REJECT = 202;   <br>CANCEL_COMPLETED = 203; <br>This field will be used in future fulfillment apis.<br>',
    )
    sku_display_status: Optional[int] = Field(
        None,
        description='- UNPAID = 100;<br>- TO_SHIP = 110;<br>- AWAITING_SHIPMENT = 111;<br>- AWAITING_COLLECTION = 112;<br>- IN_TRANSIT = 121;<br>- DELIVERED = 122;<br>- COMPLETED = 130;<br>- CALCELLED = 140;',
    )
    sku_cancel_reason: Optional[str] = Field(None, description='')
    sku_cancel_user: Optional[str] = Field(None, description='')
    sku_rts_time: Optional[int] = Field(None, description='')
    sku_type: Optional[int] = Field(
        None, description='normal = 0;<br>presale = 1;<br>virtual = 2;<br>cod = 3;'
    )


class PackageListItem(BaseModel):
    package_id: Optional[str] = Field(
        None,
        description='Package ID. <br>This field will be used in future fulfillment apis.<br><br>',
    )


class OrderLineListItem(BaseModel):
    order_line_id: Optional[str] = Field(None, description='')
    sku_id: Optional[str] = Field(None, description='Sku id<br>')
    ext_status: Optional[int] = Field(None, description='')
    display_status: Optional[int] = Field(None, description='')
    product_id: Optional[str] = Field(None, description='')
    product_name: Optional[str] = Field(None, description='')
    sku_name: Optional[str] = Field(None, description='')
    seller_sku: Optional[str] = Field(None, description='')
    sku_image: Optional[str] = Field(None, description='')
    sku_type: Optional[int] = Field(None, description='')
    rts_time: Optional[int] = Field(None, description='')
    cancel_reason: Optional[str] = Field(None, description='')
    cancel_user: Optional[str] = Field(None, description='')
    package_id: Optional[int] = Field(None, description='')
    package_status: Optional[int] = Field(None, description='')
    package_freeze_status: Optional[int] = Field(None, description='')
    shipping_provider_id: Optional[str] = Field(None, description='')
    shipping_provider_name: Optional[str] = Field(None, description='')
    tracking_number: Optional[str] = Field(None, description='')


class OrderListItem(BaseModel):
    order_id: Optional[str] = Field(None, description='')
    order_status: Optional[int] = Field(
        None,
        description='Available value: <br>UNPAID = 100;<br>AWAITING_SHIPMENT = 111; <br>AWAITING_COLLECTION = 112;<br>PARTIALLY_SHIPPING = 114;<br>IN_TRANSIT = 121; <br>DELIVERED = 122;<br>COMPLETED = 130;<br>CANCELLED = 140;<br>',
    )
    payment_method: Optional[str] = Field(
        None,
        description='The method for paying. Available value:  <br>BANK_TRANSFER = 1;<br>CASH = 2;<br>DANA_WALLET = 3;<br>BANK_CARD = 4;<br>OVO = 5;<br>CASH_ON_DELIVERY = 6;<br>GO_PAY = 7;<br>PAYPAL = 8;<br>APPLEPAY = 9;<br>SHOPEEPAY = 10;<br>KLARNA = 11;<br>KLARNA_PAY_NOW = 12;<br>KLARNA_PAY_LATER = 13;<br>KLARNA_PAY_OVER_TIME = 14;<br>TRUE_MONEY = 15;<br>RABBIT_LINE_PAY = 16;<br>IBANKING = 17;<br>TOUCH_GO = 18;<br>BOOST = 19;<br>ZALO_PAY = 20;<br>MOMO = 21;<br>BLIK = 22;<br>PAYMAYA = 23;<br>GCASH = 24;<br>AKULAKU  = 25;<br>GOOGLE_PAY = 26;<br>GRAB_PAY = 27;<br>',
    )
    delivery_option: Optional[str] = Field(
        None,
        description='The method of delivery. Available value: STANDARD/ EXPRESS/ ECONOMY/ SEND_BY_SELLER .<br>Orders with STANDARD / EXPRESS / ECONOMY are platform logistics mode. Applicable region: cross-border & ID local<br>Orders with SEND_BY_SELLER are merchant self-shipping mode. Applicable region: UK local<br>STANDARD=1<br>EXPRESS=2<br>ECONOMY=3<br>SEND_BY_SELLER=4<br>',
    )
    shipping_provider: Optional[str] = Field(
        None, description='The name of the current shipping provider. <br>'
    )
    shipping_provider_id: Optional[str] = Field(
        None, description='The id of the current shipping provider.<br>'
    )
    create_time: Optional[str] = Field(None, description='Unix timestamp for ms.<br>')
    paid_time: Optional[int] = Field(None, description='Unix timestamp for ms.<br>')
    buyer_message: Optional[str] = Field(None, description='The note from buyer.<br>')
    payment_info: Optional[PaymentInfo] = None
    recipient_address: Optional[RecipientAddress] = None
    item_list: Optional[List[ItemListItem]] = None
    cancel_reason: Optional[str] = Field(
        None, description='The reason for cancelling action.<br>'
    )
    cancel_user: Optional[str] = Field(
        None,
        description='The method of delivery. Avaliable value:  SELLER/ BUYER/ SYSTEM .<br>',
    )
    ext_status: Optional[int] = Field(
        None,
        description='Sub-status of order status. Developer can ignore 0 and 101-104. <br>201, 202, 203 are the corresponding status for the scenario of buyer-request cancellation. Buyer-request cancellation can only be triggered by buyers BEFORE the order is arranged shipment(order_status=112). Buyers can only request return/refund  AFTER <br>Available value: <br>UN_DEFINED = 0;<br>RC_PROCESSING = 101; // Risk control in progress<br>RC_APPROVED = 102; // Risk control approved<br>RC_AUTO_APPROVED = 103; // Risk control expired with no',
    )
    order_status_old: Optional[str] = Field(None, description='')
    tracking_number: Optional[str] = Field(None, description='Tracking number<br>')
    rts_time: Optional[int] = Field(
        None,
        description='The time merchants shipped order(call ShipOrder successfully).<br>Unix timestamp.<br>',
    )
    rts_sla: Optional[int] = Field(
        None,
        description='The latest shipping time specified by the platform.<br>Unix timestamp.<br>',
    )
    tts_sla: Optional[int] = Field(
        None,
        description='The latest collection time specified by the platform.<br>Unix timestamp.<br>',
    )
    cancel_order_sla: Optional[int] = Field(
        None,
        description='The automatic cancellation time for orders specified by the platform.<br>Unix timestamp.<br>',
    )
    update_time: Optional[int] = Field(
        None, description='Time of order status changes.<br>Unix timestamp.<br>'
    )
    package_list: Optional[List[PackageListItem]] = None
    receiver_address_updated: Optional[int] = Field(
        None, description='0: no update<br>1: udpated<br>'
    )
    buyer_uid: Optional[str] = Field(None, description='Buyer User ID.<br>')
    split_or_combine_tag: Optional[str] = Field(
        None,
        description='Indicate whether the order is combined or split. <br>"combined" ;<br>"split" ;<br>This field will be used in future fulfillment apis.<br>',
    )
    fulfillment_type: Optional[int] = Field(
        None,
        description='Fulfillment type. Only orders with fulfillment type = 0 can be shipped by merchants.<br>FULFILLMENT_BY_MERCHANT = 0;   <br>FULFILLMENT_BY_PLATFORM = 1; <br>',
    )
    seller_note: Optional[str] = Field(None, description='')
    warehouse_id: Optional[str] = Field(None, description='')
    payment_method_type: Optional[int] = Field(None, description='')
    payment_method_name: Optional[str] = Field(None, description='')
    order_line_list: Optional[List[OrderLineListItem]] = None


class Data(BaseModel):
    order_list: Optional[List[OrderListItem]] = None


class ApiOrdersDetailQueryPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiOrdersSearchPostRequest(BaseModel):
    start_time: Optional[int] = Field(
        None, description='deprecated plz use create_time_from'
    )
    end_time: Optional[int] = Field(
        None, description='deprecated plz use create_time_to'
    )
    order_status: Optional[int] = Field(
        None,
        description='Use this field to obtain orders in a specific status<br>- UNPAID = 100;<br>- AWAITING_SHIPMENT = 111; <br>- AWAITING_COLLECTION = 112;<br>- PARTIALLY_SHIPPING = 114;<br>- IN_TRANSIT = 121; <br>- DELIVERED = 122;<br>- COMPLETED = 130;<br>- CANCELLED = 140;',
    )
    page_size: int = Field(
        ...,
        description='Use this field to specify the maximum number of orders to obtain in a single page. Must be 1-50.',
    )
    sort_by: Optional[str] = Field(None, description='CREATE_TIME')
    cursor: Optional[str] = Field(
        None,
        description='- This field value would be returned in response data and you can use this to search the data on the next page. You do not need it at first search.',
    )
    create_time_from: Optional[int] = Field(
        None, description='Unix timestamp. Order creation time.'
    )
    create_time_to: Optional[int] = Field(
        None, description='Unix timestamp. Order creation time.'
    )
    update_time_from: Optional[int] = Field(
        None, description='Unix timestamp. Order creation time.'
    )
    update_time_to: Optional[int] = Field(
        None, description='Unix timestamp. Order creation time.'
    )
    sort_type: Optional[int] = Field(
        None, description='Available value: ASCE = 1;DESC = 2; (default)'
    )


class OrderListItem1(BaseModel):
    order_id: Optional[str] = Field(
        None,
        description='Unique id, same order id represent for the same order in the system',
    )
    order_status: Optional[int] = Field(
        None,
        description='Available value: <br>- UNPAID = 100;<br>- AWAITING_SHIPMENT = 111; <br>- AWAITING_COLLECTION = 112;<br>- PARTIALLY_SHIPPING = 114;<br>- IN_TRANSIT = 121; <br>- DELIVERED = 122;<br>- COMPLETED = 130;<br>- CANCELLED = 140;',
    )
    update_time: Optional[int] = Field(None, description='Unix timestamp.')


class Data1(BaseModel):
    more: Optional[bool] = Field(
        None, description='Whether has more orders in next page nor not<br>'
    )
    next_cursor: Optional[str] = Field(
        None, description='Cursor used for searching for more info.'
    )
    total: Optional[int] = Field(None, description='Total amount of the search result')
    order_list: Optional[List[OrderListItem1]] = None


class ApiOrdersSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None
