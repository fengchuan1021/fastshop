#   timestamp: 2022-10-29T02:15:04+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class PickUp(BaseModel):
    pick_up_start_time: Optional[int] = Field(None, description='')
    pick_up_end_time: Optional[int] = Field(None, description='')


class SelfShipment(BaseModel):
    tracking_number: str = Field(
        ...,
        description='For package with SEND_BY_SELLER as delivery_option(merchant self-shipping mode), developer needs to input tracking_number to call this API.',
    )
    shipping_provider_id: str = Field(
        ...,
        description='For package with SEND_BY_SELLER as delivery_option(merchant self-shipping mode), developer needs to input shipping_provider to call this API.',
    )


class ApiFulfillmentRtsPostRequest(BaseModel):
    package_id: str = Field(..., description='')
    pick_up_type: Optional[int] = Field(
        None, description='- Pick_up = 1;<br>- Drop_off = 2;'
    )
    pick_up: Optional[PickUp] = None
    self_shipment: SelfShipment


class FailPackage(BaseModel):
    package_id: Optional[int] = Field(None, description='')
    fail_code: Optional[int] = Field(None, description='')
    fail_reason: Optional[str] = Field(None, description='')


class Data(BaseModel):
    fail_packages: Optional[List[FailPackage]] = None


class ApiFulfillmentRtsPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiFulfillmentPreCombinePkgListGetRequest(BaseModel):
    cursor: Optional[str] = Field(None, description='')
    page_size: int = Field(..., description='')


class PreCombinePkgListItem(BaseModel):
    pre_combine_pkg_id: Optional[str] = Field(
        None, description='ID of the package can be combined'
    )
    order_id_list: Optional[List[str]] = None


class Data1(BaseModel):
    pre_combine_pkg_list: Optional[List[PreCombinePkgListItem]] = None
    next_cursor: Optional[str] = Field(None, description='')
    more: Optional[bool] = Field(
        None, description='Show if there are more combinable order combinations'
    )
    total: Optional[int] = Field(
        None, description='The total number combinable order combinations'
    )


class ApiFulfillmentPreCombinePkgListGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class SplitGroupItem(BaseModel):
    pre_split_pkg_id: int = Field(
        ...,
        description='The unique identification  designed by yourself.<br>If you input 123 as request, the response will return 123 as your unique identification',
    )
    order_line_id_list: List[int]


class ApiFulfillmentOrderSplitConfirmPostRequest(BaseModel):
    order_id: int = Field(..., description='')
    split_group: List[SplitGroupItem]


class ConfirmResultListItem(BaseModel):
    pre_split_pkg_id: Optional[int] = Field(
        None,
        description='The unique identification  designed by yourself.<br>If you input 123 as request, the response will return 123 as your unique identification',
    )
    confirm_result: Optional[bool] = Field(
        None, description='If this order split success'
    )


class SuccessListItem(BaseModel):
    pre_split_pkg_id: Optional[int] = Field(
        None,
        description='The unique identification  designed by yourself.<br>If you input 123 as request, the response will return 123 as your unique identification',
    )
    package_id: Optional[int] = Field(
        None, description='Fulfillment id of success init fulfillment'
    )


class FailListItem(BaseModel):
    pre_split_pkg_id: Optional[int] = Field(
        None,
        description='The unique identification  designed by yourself.<br>If you input 123 as request, the response will return 123 as your unique identification',
    )
    fail_reason: Optional[str] = Field(
        None, description='the reason why can not be split'
    )


class Data2(BaseModel):
    confirm_result_list: Optional[List[ConfirmResultListItem]] = None
    success_list: Optional[List[SuccessListItem]] = None
    fail_list: Optional[List[FailListItem]] = None


class ApiFulfillmentOrderSplitConfirmPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class ApiFulfillmentPackagePickupConfigListGetRequest(BaseModel):
    package_id: str = Field(..., description='')


class PickUpTimeListItem(BaseModel):
    start_time: Optional[str] = Field(None, description='')
    end_time: Optional[str] = Field(None, description='')
    avaliable: Optional[bool] = Field(
        None, description='Can I make an appointment for this time period?'
    )


class Data3(BaseModel):
    is_pick_up: Optional[bool] = Field(
        None, description='Does this package support door-to-door collection'
    )
    is_drop_off: Optional[bool] = Field(
        None, description='Does this package support point delivery'
    )
    pick_up_time_list: Optional[List[PickUpTimeListItem]] = None
    drop_off_point_url: Optional[str] = Field(
        None, description='View deliverable logistics outlets via URL'
    )


class ApiFulfillmentPackagePickupConfigListGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data3] = None


class ApiFulfillmentPackageRemovePostRequest(BaseModel):
    package_id: str = Field(..., description='')
    order_id_list: Optional[List[str]] = None


class PackageListItem(BaseModel):
    package_id: Optional[str] = Field(None, description='')
    order_id_list: Optional[List[str]] = None


class FailedPackageListItem(BaseModel):
    package_id: Optional[str] = Field(
        None, description='Failed to create a new package after removal'
    )
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')


class Data4(BaseModel):
    package_list: Optional[List[PackageListItem]] = None
    failed_package_list: Optional[List[FailedPackageListItem]] = None


class ApiFulfillmentPackageRemovePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data4] = None


class ApiFulfillmentShippingInfoGetRequest(BaseModel):
    package_id: str = Field(..., description='')


class TrackingInfoListItem(BaseModel):
    update_time: Optional[int] = Field(
        None, description='Time for the status update. Unix timestamp.'
    )
    description: Optional[str] = Field(
        None, description='Description of the tracking info.'
    )


class Data5(BaseModel):
    tracking_info_list: Optional[List[TrackingInfoListItem]] = None


class ApiFulfillmentShippingInfoGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data5] = None


class ApiFulfillmentOrderSplitVerifyPostRequest(BaseModel):
    order_id_list: List[int]


class ResultListItem(BaseModel):
    order_id: Optional[int] = Field(None, description='')
    verify_order_result: Optional[bool] = Field(
        None, description='If this order can be split'
    )


class FailListItem1(BaseModel):
    order_id: Optional[int] = Field(None, description='')
    fail_reason: Optional[str] = Field(
        None, description='the reason why can not be split'
    )


class Data6(BaseModel):
    result_list: Optional[List[ResultListItem]] = None
    fail_list: Optional[List[FailListItem1]] = None


class ApiFulfillmentOrderSplitVerifyPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data6] = None


class ApiFulfillmentShippingInfoUpdatePostRequest(BaseModel):
    package_id: str = Field(..., description='')
    tracking_number: str = Field(..., description='')
    provider_id: str = Field(..., description='')


class Data7(BaseModel):
    update_success: Optional[bool] = Field(None, description='')
    failed_reason: Optional[str] = Field(None, description='')


class ApiFulfillmentShippingInfoUpdatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data7] = None


class ApiFulfillmentUploadfilePostRequest(BaseModel):
    file_data: str = Field(
        ...,
        description='Import the file in pdf format. The file is a string generated by base64 encoding. The original file size must not exceed 10M.',
    )
    file_name: str = Field(..., description='附件名称')


class Data8(BaseModel):
    file_id: Optional[str] = Field(None, description='附件ID')
    file_url: Optional[str] = Field(None, description='附件URL')
    file_name: Optional[str] = Field(None, description='附件名称')
    file_type: Optional[str] = Field(None, description='PDF only')


class ApiFulfillmentUploadfilePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data8] = None


class DeliveryPackage(BaseModel):
    package_id: Optional[int] = Field(None, description='The ID of package')
    delivery_type: Optional[int] = Field(
        None,
        description="For package which hasn't been deliveried, if delivery success, please input 1, if delivery failed, please input 2; For package which has been deliveried, if you want to update the attachment, please input 3.<br><br>1：DELIVER；<br>2：DELIVERY_FAILED；<br>3：UPDATE_POD；",
    )
    reason: Optional[int] = Field(
        None,
        description="delivery failed reason:<br>when deliver_type=2， this data is required, will be invalid when at the other type<br>103=it has an invalid shipping address<br>104=the customer was unavailable<br>105=the customer can't be reached<br>106=it was declined by the customer<br>100=of a shipping delay<br>116=package lost<br>117=package damage<br>110=a force majeure event occurred<br>148=something went wrong",
    )
    file_type: Optional[int] = Field(
        None, description='attachment type<br>1 = IMG<br>2 = PDF'
    )
    file_url: Optional[str] = Field(None, description='attachment URL')


class ApiFulfillmentDeliveryPostRequest(BaseModel):
    delivery_packages: Optional[List[DeliveryPackage]] = None


class FailPackage1(BaseModel):
    package_id: Optional[int] = Field(None, description='package ID')
    err_code: Optional[int] = Field(None, description='error code')
    message: Optional[str] = Field(None, description='error reason')


class Data9(BaseModel):
    fail_packages: Optional[List[FailPackage1]] = None


class ApiFulfillmentDeliveryPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data9] = None


class ApiFulfillmentUploadimagePostRequest(BaseModel):
    img_data: str = Field(..., description='')
    img_scene: int = Field(
        ...,
        description='{<br>  "0": "UNSPECIFIED",<br>  "1": "PRODUCT_IMAGE",<br>  "2": "DESCRIPTION_IMAGE",<br>  "3": "PROPERTY_IMAGE",<br>  "4": "CERTIFICATION_IMAGE",<br>  "5": "SIZE_CHART_IMAGE"<br>}',
    )


class Data10(BaseModel):
    img_id: Optional[str] = Field(None, description='image uri')
    img_url: Optional[str] = Field(None, description='image url')
    img_height: Optional[int] = Field(None, description='')
    img_width: Optional[int] = Field(None, description='')
    img_scene: Optional[int] = Field(None, description='')


class ApiFulfillmentUploadimagePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data10] = None


class ApiFulfillmentShippingDocumentGetRequest(BaseModel):
    package_id: str = Field(..., description='')
    document_type: int = Field(
        ...,
        description='Available value: SHIPPING_LABEL/ PICK_LIST/ PACK_LIST<br>- SHIPPING_LABEL = 1<br>- PICK_LIST = 2<br>- SL+PL = 3<br>PACK_LIST is not available in this version.',
    )
    document_size: Optional[int] = Field(
        None,
        description='Use this field to specify the size of document to obtain. Available value: A6/A5.  A6 by default.<br>- A6 = 0<br>- A5 = 1',
    )


class Data11(BaseModel):
    doc_url: Optional[str] = Field(None, description='')


class ApiFulfillmentShippingDocumentGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data11] = None


class ApiFulfillmentDetailGetRequest(BaseModel):
    package_id: str = Field(..., description='')


class SkuListItem(BaseModel):
    sku_id: Optional[str] = Field(None, description='')
    sku_name: Optional[str] = Field(None, description='')
    sku_image: Optional[str] = Field(None, description='')
    quantity: Optional[str] = Field(None, description='')


class OrderInfoListItem(BaseModel):
    order_id: Optional[str] = Field(None, description='')
    sku_list: Optional[List[SkuListItem]] = None


class Data12(BaseModel):
    package_id: Optional[str] = Field(None, description='')
    order_info_list: Optional[List[OrderInfoListItem]] = None
    package_status: Optional[int] = Field(
        None,
        description='- TO_FULFILL = 1; <br>- PROCESSING = 2; <br>- FULFILLING = 3;<br>- COMPLETED = 4;<br>- CANCELLED = 5;',
    )
    package_freeze_status: Optional[int] = Field(
        None,
        description='- FREEZE = 1; When the package is pending review for cancellation.<br>- UNFREEZE = 2;',
    )
    sc_tag: Optional[int] = Field(
        None, description='- DEFAULT = 0<br>- COMBINE =1<br>- SPLIT = 2'
    )
    print_tag: Optional[int] = Field(
        None,
        description='- None = 0<br>- only picking_list = 1<br>- only shipping_label = 4<br>- shipping label+picking_list= 5<br>PACK_LIST is not available in this version.',
    )
    sku_tag: Optional[int] = Field(
        None,
        description='Whether there are multiple SKU IDs in a package<br>- ONE = 1<br>- MANY = 2',
    )
    note_tag: Optional[int] = Field(
        None, description='- BUYER_UNNOTED = 0<br>- BUYER_NOTED = 1'
    )
    delivery_option: Optional[str] = Field(
        None,
        description='STANDARD = 1<br>EXPRESS = 2<br>ECONOMY = 3<br>SEND_BY_SELLER = 4',
    )
    shipping_provider: Optional[str] = Field(None, description='')
    shipping_provider_id: Optional[str] = Field(None, description='')
    tracking_number: Optional[str] = Field(None, description='')
    pick_up_type: Optional[int] = Field(
        None,
        description='Whether the package is delivered by pick_up or drop_off.<br>- Pick_up = 1;<br>- Drop_off = 2;',
    )
    pick_up_start_time: Optional[int] = Field(None, description='Unix timestamp')
    pick_up_end_time: Optional[int] = Field(None, description='Unix timestamp')
    create_time: Optional[int] = Field(None, description='Unix timestamp')
    update_time: Optional[int] = Field(None, description='Unix timestamp')
    order_line_id_list: Optional[List[str]] = None
    cancel_because_logistic_issue: Optional[int] = Field(
        None,
        description='package cancel because logistic = 2; <br>package cancel not because logistic = 1',
    )


class ApiFulfillmentDetailGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data12] = None


class PreCombinePkgListItem1(BaseModel):
    pre_combine_pkg_id: str = Field(
        ..., description='ID of the package can be combined'
    )
    order_id_list: Optional[List[str]] = None


class ApiFulfillmentPreCombinePkgConfirmPostRequest(BaseModel):
    pre_combine_pkg_list: Optional[List[PreCombinePkgListItem1]] = None


class PackageListItem1(BaseModel):
    package_id: Optional[str] = Field(
        None,
        description='The package ID generated after the package is successfully combined',
    )
    order_id_list: Optional[List[str]] = None


class FailedPackageListItem1(BaseModel):
    package_id: Optional[str] = Field(
        None,
        description='The package ID generated after the package is unsuccessfully combined',
    )
    code: Optional[int] = Field(None, description='Error code of this package')
    message: Optional[str] = Field(None, description='Error message of this package')


class Data13(BaseModel):
    package_list: Optional[List[PackageListItem1]] = None
    failed_package_list: Optional[List[FailedPackageListItem1]] = None


class ApiFulfillmentPreCombinePkgConfirmPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data13] = None


class ApiFulfillmentSearchPostRequest(BaseModel):
    create_time_from: Optional[int] = Field(None, description='Unix timestamp')
    create_time_to: Optional[int] = Field(None, description='Unix timestamp')
    update_time_from: Optional[int] = Field(None, description='Unix timestamp')
    update_time_to: Optional[int] = Field(None, description='Unix timestamp')
    package_status: Optional[int] = Field(
        None,
        description='- TO_FULFILL = 1; <br>- PROCESSING = 2; <br>- FULFILLING = 3;<br>- COMPLETED = 4;<br>- CANCELLED = 5;',
    )
    cursor: Optional[str] = Field(
        None,
        description='This field value would be returned in response data and you can use this to search the data on the next page. You do not need it at first search.',
    )
    sort_by: Optional[int] = Field(
        None,
        description='Default value: 1<br>- CREATE_TIME = 1<br>- ORDER_PAY_TIME = 2<br>- UPDATE_TME = 3',
    )
    sort_type: Optional[int] = Field(
        None, description='Default value: 2<br>- ASC = 1<br>- DESC = 2'
    )
    page_size: int = Field(
        ...,
        description='Use this field to specify the maximum number of orders to obtain in a single page. Must be 1-50.',
    )
    cancel_because_logistic_issue: Optional[int] = Field(
        None,
        description='search all package ,   0 or nil; <br>cancel because logistic issue = 2; <br>cansel not because logistic = 1',
    )


class PackageListItem2(BaseModel):
    package_id: Optional[str] = Field(None, description='')
    package_status: Optional[int] = Field(
        None,
        description='- TO_FULFILL = 1; <br>- PROCESSING = 2; <br>- FULFILLING = 3;<br>- COMPLETED = 4;<br>- CANCELLED = 5;',
    )
    create_time: Optional[int] = Field(None, description='Unix timestamp')
    update_time: Optional[int] = Field(None, description='Unix timestamp')


class Data14(BaseModel):
    more: Optional[bool] = Field(None, description='')
    next_cursor: Optional[str] = Field(None, description='')
    package_list: Optional[List[PackageListItem2]] = None
    total: Optional[int] = Field(None, description='Total amount of the search result')


class ApiFulfillmentSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data14] = None
