#   timestamp: 2022-10-29T02:15:05+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class ApiPromotionActivityCreatePostRequest(BaseModel):
    request_serial_no: str = Field(
        ...,
        description='Request sequence number which is used to identify unique requests. Max. Length 128 bytes.',
    )
    title: str = Field(
        ..., description='Promotion name (50 characters max.) The name must be unique'
    )
    promotion_type: int = Field(
        ...,
        description='Activity Type:<br>1=FixedPrice<br>2=DirectDiscount<br>3=FlashSale<br>CAN NOT CHANGE once promotion been created',
    )
    begin_time: int = Field(..., description='Promotion start time，unix timestamp')
    end_time: int = Field(..., description='Promotion end time，unix timestamp')
    product_type: int = Field(
        ...,
        description='1=SPU<br>2=SKU<br><br>CAN NOT CHANGE once promotion been created',
    )


class Data(BaseModel):
    request_serial_no: Optional[str] = Field(
        None, description='user input request_serial_no'
    )
    promotion_id: Optional[str] = Field(
        None, description='A unique ID that identifies different promotions'
    )
    create_time: Optional[int] = Field(
        None, description='The time when the promotion is created'
    )
    update_time: Optional[int] = Field(
        None, description='The time when the promotion is updated'
    )
    status: Optional[int] = Field(
        None,
        description='Activity status<br>1 - To be started<br>2- In progress<br>3- Expired<br>4- has expired',
    )


class ApiPromotionActivityCreatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiPromotionActivityDeactivatePostRequest(BaseModel):
    request_serial_no: str = Field(
        ...,
        description='Request sequence number, used to mark unique requests, support idempotent .The merchant side needs to remain unique. Scope for the entire marketing business domain.Length less than or equal to 128 bytes.You can generate by time and machine id/thread id and counter，or just use uuid.<br><br>',
    )
    promotion_id: str = Field(..., description='promotion id')


class Data1(BaseModel):
    request_serial_no: Optional[str] = Field(
        None, description='User input request_serial_no<br>'
    )
    promotion_id: Optional[str] = Field(
        None, description='A unique ID that identifies promotions'
    )
    title: Optional[str] = Field(None, description='Promotion title')
    status: Optional[int] = Field(
        None,
        description='Activity status:<br>1 - To be started<br>2- In progress<br>3- Expired<br>4- Deactived',
    )
    update_time: Optional[int] = Field(None, description='Promotion update time')


class ApiPromotionActivityDeactivatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiPromotionActivityItemsRemovePostRequest(BaseModel):
    request_serial_no: str = Field(
        ...,
        description='Request sequence number, used to mark unique requests, support idempotent .The merchant side needs to remain unique. Scope for the entire marketing business domain.Length less than or equal to 128 bytes.You can generate by time and machine id/thread id and counter，or just use uuid.<br><br>',
    )
    promotion_id: str = Field(..., description='Promotion id')
    spu_list: Optional[List[str]] = None
    sku_list: Optional[List[str]] = None


class Data2(BaseModel):
    request_serial_no: Optional[str] = Field(
        None, description='user input request_serial_no<br><br>'
    )
    promotion_id: Optional[str] = Field(None, description='promotion id')
    status: Optional[int] = Field(None, description='promotion status')
    update_time: Optional[int] = Field(None, description='promotion update time')


class ApiPromotionActivityItemsRemovePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class ApiPromotionActivityGetGetRequest(BaseModel):
    promotion_id: str = Field(..., description='Promotion ID<br>')


class SkuListItem(BaseModel):
    product_id: Optional[str] = Field(None, description='Product ID')
    sku_id: Optional[str] = Field(None, description='SKU ID')
    promotion_price: Optional[str] = Field(
        None,
        description='Available only if the promotion type is FixedPrice/FlashSale<br>',
    )
    discount: Optional[str] = Field(
        None, description='Available only if the promotion type is DirectDiscount (%)'
    )
    num_limit: Optional[int] = Field(
        None,
        description='Promotion stock: you can either input "-1" (no limit) or a specific number. Promotion stock you set must not be greater than the current stock.',
    )
    user_limit: Optional[int] = Field(
        None,
        description='Purchase limit per buyer: you can either input "-1" (no limit) or a specific number.',
    )


class ProductListItem(BaseModel):
    product_id: Optional[str] = Field(None, description='ProductID')
    promotion_price: Optional[str] = Field(
        None,
        description='Available only if the promotion type is FixedPrice/FlashSale<br>',
    )
    discount: Optional[str] = Field(
        None, description='Available only if the promotion type is DirectDiscount (%)'
    )
    num_limit: Optional[int] = Field(
        None,
        description='Promotion stock: you can either input "-1" (no limit) or a specific number. Promotion stock you set must not be greater than the current stock.',
    )
    user_limit: Optional[int] = Field(
        None,
        description='Purchase limit per buyer: you can either input "-1" (no limit) or a specific number.',
    )
    sku_list: Optional[List[SkuListItem]] = None


class Data3(BaseModel):
    promotion_id: Optional[str] = Field(None, description='Promotion ID<br>')
    title: Optional[str] = Field(None, description='Event name set by the merchant')
    promotion_type: Optional[int] = Field(
        None, description='Fields for determining the type of marketing campaign'
    )
    begin_time: Optional[int] = Field(
        None,
        description='The time when discount promotion starts. The start time must be later than current time.',
    )
    end_time: Optional[int] = Field(
        None,
        description='The time when discount promotion ends. The end time must be 10 mins later than the start time, and the promotion period must be less than 365 days.',
    )
    product_list: Optional[List[ProductListItem]] = None
    status: Optional[int] = Field(
        None,
        description='Promotion status<br>1 - Upcoming<br>2- Ongoing<br>3- Expired<br>4- Deactivated',
    )
    create_time: Optional[int] = Field(
        None, description='The time when the promotion was last updated'
    )
    update_time: Optional[int] = Field(
        None, description='The time when the promotion was created'
    )
    product_type: Optional[int] = Field(
        None, description='Activity product dimension<br>1=SPU<br>2=SKU'
    )


class ApiPromotionActivityGetGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data3] = None


class SkuListItem1(BaseModel):
    product_id: Optional[str] = Field(None, description='Product ID')
    sku_id: Optional[str] = Field(None, description='SKU ID')
    promotion_price: Optional[str] = Field(
        None,
        description='Available only if the activity type is FixedPrice/FlashSale<br>',
    )
    discount: Optional[str] = Field(
        None, description='Available only if the activity type is DirectDiscount (%)'
    )
    num_limit: Optional[int] = Field(
        None,
        description='Promotion stock: you can either input "-1" (no limit) or a specific number. Promotion stock you set must not be greater than the current stock.',
    )
    user_limit: Optional[int] = Field(
        None,
        description='Purchase limit per buyer: you can either input "-1" (no limit) or a specific number.',
    )


class ProductListItem1(BaseModel):
    product_id: Optional[str] = Field(None, description='product ID')
    promotion_price: Optional[str] = Field(
        None,
        description='Available only if the promotion type is FixedPrice/FlashSale.<br>',
    )
    discount: Optional[str] = Field(
        None, description='Available only if the promotion type is DirectDiscount (%)'
    )
    num_limit: Optional[int] = Field(
        None,
        description='Promotion stock: you can either input "-1" (no limit) or a specific number. Promotion stock you set must not be greater than the current stock.',
    )
    user_limit: Optional[int] = Field(
        None,
        description='Purchase limit per buyer: you can either input "-1" (no limit) or a specific number.',
    )
    sku_list: Optional[List[SkuListItem1]] = None


class ApiPromotionActivityItemsAddorupdatePostRequest(BaseModel):
    request_serial_no: str = Field(
        ...,
        description='Request sequence number which is used to identify unique requests. Max. Length 128 bytes',
    )
    promotion_id: int = Field(..., description='Promotion ID')
    product_list: Optional[List[ProductListItem1]] = None


class Data4(BaseModel):
    request_serial_no: Optional[str] = Field(
        None,
        description='Request sequence number which is used to identify unique requests. Max. Length 128 bytes',
    )
    promotion_id: Optional[str] = Field(None, description='Promotion ID')
    title: Optional[str] = Field(None, description='Promotion Title')
    update_time: Optional[int] = Field(None, description='Event update time')
    status: Optional[int] = Field(
        None,
        description='Promotion status<br>1 - Upcoming<br>2- Ongoing<br>3- Expired<br>4- Deactivated',
    )
    item_count: Optional[int] = Field(
        None, description='The number of items (ProductInfo objects) in this request'
    )


class ApiPromotionActivityItemsAddorupdatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data4] = None


class ApiPromotionActivityListPostRequest(BaseModel):
    offset: int = Field(
        ...,
        description='Promotion status<br>1 - Upcoming<br>2- Ongoing<br>3- Expired<br>4- Deactivated',
    )
    limit: int = Field(..., description='Offset position')
    status: Optional[int] = Field(
        None, description='Number of requests per request, [1,100]'
    )


class PromotionListItem(BaseModel):
    promotion_id: Optional[str] = Field(None, description='Promotion ID')
    title: Optional[str] = Field(None, description='Promotion name')
    promotion_type: Optional[int] = Field(None, description='Promotion Type')
    begin_time: Optional[int] = Field(None, description='Start time')
    end_time: Optional[int] = Field(None, description='End time')
    status: Optional[int] = Field(None, description='Promotion Status')
    create_time: Optional[int] = Field(None, description='Promotion create time')
    update_time: Optional[int] = Field(None, description='Promotion update time')
    product_type: Optional[int] = Field(None, description='Product type')


class Data5(BaseModel):
    total: Optional[int] = Field(
        None,
        description='Total number of activities, overview of activities under the current filter',
    )
    promotion_list: Optional[List[PromotionListItem]] = None


class ApiPromotionActivityListPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data5] = None


class ApiPromotionActivityUpdatePostRequest(BaseModel):
    request_serial_no: str = Field(
        ...,
        description='Request sequence number, used to mark unique requests, support idempotent .The merchant side needs to remain unique. Scope for the entire marketing business domain.Length less than or equal to 128 bytes.You can generate by time and machine id/thread id and counter，or just use uuid.<br><br>',
    )
    promotion_id: str = Field(..., description='A unique ID that identifies promotions')
    title: str = Field(..., description='Event name set by the merchant')
    begin_time: int = Field(..., description='Event start time，unix timestamp')
    end_time: int = Field(..., description='Event start time，unix timestamp')


class Data6(BaseModel):
    request_serial_no: Optional[str] = Field(
        None, description='User input request_serial_no<br>'
    )
    promotion_id: Optional[str] = Field(
        None, description='A unique ID that identifies promotions'
    )
    title: Optional[str] = Field(None, description='Event name set by the merchant')
    update_time: Optional[int] = Field(None, description='Event update time')


class ApiPromotionActivityUpdatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data6] = None
