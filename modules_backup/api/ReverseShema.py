#   timestamp: 2022-10-29T02:15:04+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field



class ApiReverseReverseRequestConfirmPostRequest(BaseModel):
    reverse_order_id: str = Field(
        ..., description='The identification of a Tiktok reverse order'
    )


class ApiReverseReverseRequestConfirmPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Dict[str, Any]] = None


class ApiReverseReverseOrderListPostRequest(BaseModel):
    update_time_from: Optional[int] = Field(
        None, description='Unix timestamp. Reverse order updated time.'
    )
    update_time_to: Optional[int] = Field(
        None, description='Unix timestamp. Reverse order updated time.'
    )
    reverse_type: Optional[int] = Field(
        None,
        description='Filter by reverse type.<br>Available value: <br>REFUND_ONLY = 2;<br>RETURN_AND_REFUND = 3;<br>REQUEST_CANCEL = 4;',
    )
    sort_by: Optional[int] = Field(
        None,
        description='Available value: <br>REQUEST_TIME = 0; (default)<br>UPDATE_TIME = 1;<br>REFUND_TOTAL = 2;',
    )
    sort_type: Optional[int] = Field(
        None, description='Available value: <br>ASCE = 0;<br>DESC = 1; (default)'
    )
    offset: int = Field(
        ...,
        description='Use this field to specify the offset of the order. Must be greater than or equal to 0.<br>If "offset" is less than 0, then "offset" is assigned the default value of 0.',
    )
    size: int = Field(
        ...,
        description='Use this field to specify the maximum number of orders to obtain in a single page. Must be 1-100.<br>If "size" is less than 1, then "size" is assigned the default value of 10. If "size" is greater than 100, then "size" is assigned the default value of 100;',
    )
    reverse_order_status: Optional[int] = Field(
        None,
        description='Available value: AFTERSALE_APPLYING = 1; AFTERSALE_REJECT_APPLICATION = 2;AFTERSALE_RETURNING = 3;AFTERSALE_BUYER_SHIPPED = 4; AFTERSALE_SELLER_REJECT_RECEIVE = 5;AFTERSALE_SUCCESS = 50; CANCEL_SUCCESS = 51;CLOSED = 99;COMPLETE = 100;',
    )
    order_id: Optional[int] = Field(None, description='')
    reverse_order_id: Optional[int] = Field(None, description='')


class ReturnItemListItem(BaseModel):
    return_product_id: Optional[str] = Field(None, description='Reverse product id')
    return_product_name: Optional[str] = Field(None, description='Reverse product name')
    sku_id: Optional[str] = Field(None, description='SKU id')
    seller_sku: Optional[str] = Field(None, description='Seller sku')
    sku_name: Optional[str] = Field(None, description='Sku properties')
    return_quantity: Optional[int] = Field(None, description='Reverse SKU quantity')
    product_images: Optional[str] = Field(None, description='The image of product')


class ReverseRecordListItem(BaseModel):
    description: Optional[str] = Field(None, description='Reverse record description.')
    update_time: Optional[int] = Field(None, description='Reverse record update time.')
    reason_text: Optional[str] = Field(None, description='Reverse reason.')
    additional_message: Optional[str] = Field(
        None, description='Reverse additional message.'
    )
    additional_image_list: Optional[List[str]] = None


class ReverseListItem(BaseModel):
    reverse_order_id: Optional[str] = Field(
        None, description='The identification of a TikTok reverse order'
    )
    order_id: Optional[str] = Field(
        None, description='The identification of a TikTok order'
    )
    refund_total: Optional[str] = Field(None, description='Buyer refund total amount')
    currency: Optional[str] = Field(None, description='Currency for payment.')
    reverse_type: Optional[int] = Field(
        None,
        description='Available value: <br>REFUND_ONLY = 2;<br>RETURN_AND_REFUND = 3;<br>REQUEST_CANCEL = 4;',
    )
    return_reason: Optional[str] = Field(None, description='Buyer return reason.')
    return_item_list: Optional[List[ReturnItemListItem]] = None
    reverse_status_value: Optional[int] = Field(
        None,
        description='Available value: <br>AFTERSALE_APPLYING = 1; <br>AFTERSALE_REJECT_APPLICATION = 2;<br>AFTERSALE_RETURNING = 3;<br>AFTERSALE_BUYER_SHIPPED = 4; <br>AFTERSALE_SELLER_REJECT_RECEIVE = 5;<br>AFTERSALE_SUCCESS = 50; <br>CANCEL_SUCCESS = 51;<br>CLOSED = 99;<br>COMPLETE = 100;',
    )
    reverse_request_time: Optional[int] = Field(
        None, description='Time of reverse request. Unix timestamp.'
    )
    reverse_update_time: Optional[int] = Field(
        None, description='Time of reverse update. Unix timestamp.'
    )
    return_tracking_id: Optional[str] = Field(
        None, description='The return tracking ID when buyer returns the items.'
    )
    reverse_record_list: Optional[List[ReverseRecordListItem]] = None


class Data(BaseModel):
    reverse_list: Optional[List[ReverseListItem]] = None
    more: Optional[bool] = Field(
        None, description='Whether it has more orders on the next page or not'
    )


class ApiReverseReverseOrderListPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiReverseOrderCancelPostRequest(BaseModel):
    order_id: str = Field(..., description='')
    cancel_reason_key: str = Field(..., description='')


class Data1(BaseModel):
    reverse_main_order_id: Optional[int] = Field(None, description='')


class ApiReverseOrderCancelPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiReverseReverseReasonListGetRequest(BaseModel):
    reverse_action_type: Optional[int] = Field(
        None,
        description='Available value: <br>CANCEL = 1;<br>REFUND = 2;<br>RETURN_AND_REFUND = 3;<br>REQUEST_CANCEL_REFUND = 4;',
    )
    reason_type: Optional[int] = Field(
        None,
        description='Available value: <br>STARTE_REVERSE = 1;    <br>REJECT_APPLY = 2;  <br>REJECT_PARCEL  = 3;',
    )
    fulfillment_status: Optional[int] = Field(
        None,
        description='Available value: <br>UNINITIATE = 1;    <br>BEFORE_RTS = 2;  <br>RTS  = 3;  <br>DELIVERED = 4;',
    )


class ReverseReasonListItem(BaseModel):
    reverse_reason_key: Optional[str] = Field(
        None,
        description='Reverse reason key. It can be used as input param in the RejectReverse API.',
    )
    reverse_reason: Optional[str] = Field(
        None, description='Reverse reason content that will be exposed to buyer.'
    )
    available_order_status_list: Optional[int] = Field(
        None,
        description='Order status for which current reverse reason applies. (may not exist)<br>Available value: <br>CREATED = 0;<br>TO_SHIP = 200;<br>SHIPPING = 305;<br>DELIVERED = 310;',
    )


class Data2(BaseModel):
    reverse_reason_list: Optional[List[ReverseReasonListItem]] = None


class ApiReverseReverseReasonListGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class ApiReverseReverseRequestRejectPostRequest(BaseModel):
    reverse_order_id: str = Field(
        ..., description='The identification of a TikTok reverse order'
    )
    reverse_reject_reason_key: str = Field(
        ...,
        description='The applicable reason keys for rejecting reverse order in different scenarios can be obtained from the "GetReverseReason" API',
    )
    reverse_reject_comments: Optional[str] = Field(
        None,
        description='The free comments for rejecting reverse order, limit 500 characters.',
    )


class ApiReverseReverseRequestRejectPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Dict[str, Any]] = None
