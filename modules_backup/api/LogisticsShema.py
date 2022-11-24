#   timestamp: 2022-10-29T02:15:05+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field



class ApiLogisticsShippingDocumentGetRequest(BaseModel):
    order_id: str = Field(..., description='')
    document_type: str = Field(
        ...,
        description='Use this field to specify the type of document to obtain. Available value: SHIPPING_LABEL/ PICK_LIST/ SL_PL<br>SL_PL is to print both SHIPPING_LABEL and PICK_LIST in one pdf.',
    )
    document_size: Optional[str] = Field(
        None,
        description='Use this field to specify the size of document to obtain. Available value: A6/A5.  A6 by default.<br>',
    )


class Data(BaseModel):
    doc_url: Optional[str] = Field(
        None,
        description='By accessing this URL, you can download the document. Each URL can only be accessed  one time.<br><br>',
    )


class ApiLogisticsShippingDocumentGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiLogisticsGetSubscribedDeliveryoptionsPostRequest(BaseModel):
    warehouse_id_list: List[str]


class WarehouseDeliveryItem(BaseModel):
    delivery_option: Optional[str] = Field(
        None, description='1: standard<br>2: express<br>3: economy<br>4: send_by_seller'
    )
    service_id: Optional[str] = Field(None, description='7062707987635252416')
    service_name: Optional[str] = Field(None, description='')


class WarehouseListItem(BaseModel):
    warehouse_id: Optional[str] = Field(None, description='')
    warehouse_delivery: Optional[List[WarehouseDeliveryItem]] = None


class Data1(BaseModel):
    warehouse_list: Optional[List[WarehouseListItem]] = None


class ApiLogisticsGetSubscribedDeliveryoptionsPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiLogisticsShipGetGetRequest(BaseModel):
    order_id: str = Field(..., description='')


class TrackingInfoItem(BaseModel):
    update_time: Optional[int] = Field(
        None, description='Time for the status update.<br>'
    )
    description: Optional[str] = Field(
        None, description='Description of the tracking info.<br>'
    )


class TrackingInfoListItem(BaseModel):
    tracking_info: Optional[List[TrackingInfoItem]] = None


class Data2(BaseModel):
    tracking_info_list: Optional[List[TrackingInfoListItem]] = None


class ApiLogisticsShipGetGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class WarehouseAddress(BaseModel):
    region: Optional[str] = Field(None, description='')
    state: Optional[str] = Field(None, description='')
    city: Optional[str] = Field(None, description='')
    district: Optional[str] = Field(None, description='')
    town: Optional[str] = Field(None, description='')
    phone: Optional[str] = Field(None, description='')
    contact_person: Optional[str] = Field(None, description='')
    zipcode: Optional[str] = Field(None, description='It may be empty<br>')
    full_address: Optional[str] = Field(None, description='')
    region_code: Optional[str] = Field(None, description='region code')


class WarehouseListItem1(BaseModel):
    warehouse_id: Optional[str] = Field(None, description='')
    warehouse_name: Optional[str] = Field(None, description='')
    warehouse_effect_status: Optional[int] = Field(
        None,
        description='Available Value:<br>EFFECTIVE = 1;<br>NONEFFECTIVE = 2;<br>RESTRICTED = 3;<br>',
    )
    warehouse_type: Optional[int] = Field(
        None,
        description='Available Value:<br>SALES_WAREHOUSE = 1;<br>RETURN_WAREHOUSE = 2;<br>LOCAL_RETURN_WAREHOUSE = 3;<br>',
    )
    warehouse_sub_type: Optional[int] = Field(
        None,
        description='Available Value:<br>DOMESTIC_WAREHOUSE = 1;<br>CB_OVERSEA_WAREHOUSE = 2;<br>CB_DIRECT_SHIPPING_WAREHOUSE = 3;<br>',
    )
    warehouse_address: Optional[WarehouseAddress] = None
    is_default: Optional[bool] = Field(None, description='')


class Data3(BaseModel):
    warehouse_list: Optional[List[WarehouseListItem1]] = None


class ApiLogisticsGetWarehouseListGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data3] = None


class ItemWeightLimit(BaseModel):
    max_weight: Optional[int] = Field(None, description='Max weight of package.<br>')
    min_weight: Optional[int] = Field(None, description='Min weight of package.<br>')


class ItemDimensionLimit(BaseModel):
    length: Optional[int] = Field(None, description='Limit length of package.<br>')
    width: Optional[int] = Field(None, description='Limit width of package.<br>')
    height: Optional[int] = Field(None, description='Limit height of package.<br>')


class ShippingProviderListItem(BaseModel):
    shipping_provider_id: Optional[str] = Field(
        None, description='The id of the shipping provider<br>'
    )
    shipping_provider_name: Optional[str] = Field(
        None, description='The name of the shipping provider.<br>'
    )


class DeliveryOptionListItem(BaseModel):
    delivery_option_id: Optional[str] = Field(
        None, description='The id of delivery option.<br>'
    )
    delivery_option_name: Optional[str] = Field(
        None, description='The name of delivery option.<br>'
    )
    item_weight_limit: Optional[ItemWeightLimit] = None
    item_dimension_limit: Optional[ItemDimensionLimit] = None
    shipping_provider_list: Optional[List[ShippingProviderListItem]] = None


class Data4(BaseModel):
    delivery_option_list: Optional[List[DeliveryOptionListItem]] = None


class ApiLogisticsShippingProvidersGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data4] = None


class ApiLogisticsTrackingPostRequest(BaseModel):
    order_id: str = Field(..., description='')
    tracking_number: str = Field(..., description='')
    provider_id: str = Field(..., description='')


class ApiLogisticsTrackingPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Dict[str, Any]] = None
