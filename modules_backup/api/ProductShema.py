#   timestamp: 2022-10-29T02:15:03+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class ApiProductsCategoriesRulesGetRequest(BaseModel):
    category_id: str = Field(
        ..., description='Only support the input of leaf categories'
    )


class ProductCertification(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    sample: Optional[str] = Field(
        None, description='Image of product qualification template'
    )
    is_mandatory: Optional[bool] = Field(None, description='')


class ExemptionOfIdentifierCode(BaseModel):
    support_identifier_code_exemption: Optional[bool] = Field(
        None,
        description='Only the UK market needs to fill in the GTIN code, UK sellers need to pay attention to whether the category allows GTIN exemption.',
    )


class CategoryRule(BaseModel):
    product_certifications: Optional[List[ProductCertification]] = None
    support_size_chart: Optional[bool] = Field(
        None, description='Whether to support input sizechart'
    )
    support_cod: Optional[bool] = Field(
        None, description='Whether to support opening cod'
    )
    exemption_of_identifier_code: Optional[ExemptionOfIdentifierCode] = None
    is_size_chart_mandatory: Optional[bool] = Field(
        None,
        description="This means whether the size chart information is mandatory in this category or not.<br>That the value is 'true' means that you must fill the sizechart information when you create product in this category .<br>That the value is ‘false’ means the sizechart is the optional information when you create product in this category.",
    )


class Data(BaseModel):
    category_rules: Optional[List[CategoryRule]] = None


class ApiProductsCategoriesRulesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiProductsRecoverPostRequest(BaseModel):
    product_ids: List[str]


class Data1(BaseModel):
    failed_product_ids: Optional[List[str]] = None


class ApiProductsRecoverPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiProductsBrandsGetRequest(BaseModel):
    category_id: Optional[str] = Field(None, description='')
    only_authorized: Optional[bool] = Field(
        None,
        description='You can use the "only_authorized" field to decide whether to search only authorized brands.',
    )
    brand_suggest: Optional[str] = Field(
        None,
        description='You can use the "brand_suggest" field to search for the brand name.',
    )
    page_size: Optional[int] = Field(
        None,
        description='"page_size" represents the return list pagination, the number of brands per page.<br>Integer between [1,200]. The "page_number" field and the "page_size" field should be used together. The product of the page_number field and the page_size field cannot exceed 10,000.',
    )
    page_number: Optional[int] = Field(
        None,
        description='"page number" represents the page number of the returned brand list.<br>Integer starting from 1. The "page_number" field and the "page_size" field should be used together. The product of the page_number field and the page_size field cannot exceed 10,000.',
    )


class BrandListItem(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    authorized_status: Optional[int] = Field(
        None,
        description='This field returns whether the brands are authorized.<br>Value:  Unauthorized = 1，Authorized = 2.',
    )


class Data2(BaseModel):
    brand_list: Optional[List[BrandListItem]] = None
    total_num: Optional[int] = Field(None, description='Total number of brands return.')


class ApiProductsBrandsGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class ApiProductsActivatePostRequest(BaseModel):
    product_ids: List[str]


class Data3(BaseModel):
    failed_product_ids: Optional[List[str]] = None


class ApiProductsActivatePostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data3] = None


class CategoryListItem(BaseModel):
    id: Optional[str] = Field(None, description='')
    parent_id: Optional[str] = Field(None, description='Parent category ID')
    local_display_name: Optional[str] = Field(
        None,
        description='The name of the category in the country where the shop operates',
    )
    is_leaf: Optional[bool] = Field(
        None, description='Whether the category is a leaf category'
    )


class Data4(BaseModel):
    category_list: Optional[List[CategoryListItem]] = None


class ApiProductsCategoriesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data4] = None


class ApiProductsSearchPostRequest(BaseModel):
    search_status: Optional[int] = Field(
        None,
        description='0-all、1-draft、2-pending、3-failed、4-live、5-seller_deactivated、6-platform_deactivated、7-freeze',
    )
    seller_sku_list: Optional[List[str]] = None
    create_time_from: Optional[int] = Field(
        None,
        description='This is the product create time , and this is the time range condition filter . We suggest that you search the time range by "create_time_from" and "create_time_to".<br>If you only fill in the "create_time_to",and the "create_time_from" is empty ,then we will set the earliest time of the shop to the field "create_time_from" by default.<br>If you only fill in the "create_time_from",and the "create_time_to" is empty ,then we will set "now" to the field "create_time_to" by default.<br>This field is required. This data should be a 10-digits timestamp',
    )
    create_time_to: Optional[int] = Field(
        None,
        description='This is the product create time , and this is the time range condition filter . We suggest that you search the time range by "create_time_from" and "create_time_to".<br>If you only fill in the "create_time_to",and the "create_time_from" is empty ,then we will set the earliest time of the shop to the field "create_time_from" by default.<br>If you only fill in the "create_time_from",and the "create_time_to" is empty ,then we will set "now" to the field "create_time_to" by default.<br>This field is required. This data should be a 10-digits timestamp',
    )
    update_time_from: Optional[int] = Field(
        None,
        description='This is the product updated time , and this is the time range condition filter . We suggest that you search the time range by "update_time_from" and "update_time_to".<br>If you only fill in the "update_time_to",and the "update_time_from" is empty ,then we will set the earliest time of the shop to the field "update_time_from" by default.<br>If you only fill in the "update_time_from",and the "update_time_to" is empty ,then we will set "now" to the field "update_time_to" by default.<br>This field is require. This data should be a 10-digits timestamp',
    )
    update_time_to: Optional[int] = Field(
        None,
        description='This is the product updated time , and this is the time range condition filter . We suggest that you search the time range by "update_time_from" and "update_time_to".<br>If you only fill in the "update_time_to",and the "update_time_from" is empty ,then we will set the earliest time of the shop to the field "update_time_from" by default.<br>If you only fill in the "update_time_from",and the "update_time_to" is empty ,then we will set "now" to the field "update_time_to" by default.<br>This field is require. This data should be a 10-digits timestamp',
    )
    page_number: int = Field(..., description='Integer starting from 1')
    page_size: int = Field(..., description='Return up to 100 records per page')


class Price(BaseModel):
    currency: Optional[str] = Field(None, description='')
    original_price: Optional[str] = Field(
        None, description='Original price of the product'
    )
    price_include_vat: Optional[str] = Field(
        None,
        description='This price can only be obtained in cross-border business. This price is obtained after adding duty and other taxes based on the original price entered<br>This price will be displayed to the customer on the product details page.',
    )


class StockInfo(BaseModel):
    warehouse_id: Optional[str] = Field(None, description='')
    available_stock: Optional[int] = Field(None, description='')


class Sku(BaseModel):
    id: Optional[str] = Field(None, description='')
    seller_sku: Optional[str] = Field(None, description='')
    price: Optional[Price] = None
    stock_infos: Optional[List[StockInfo]] = None


class Product(BaseModel):
    id: Optional[int] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    status: Optional[int] = Field(
        None,
        description='1-draft、2-pending、3-failed、4-live、5-seller_deactivated、6-platform_deactivated、7-freeze 、8-deleted',
    )
    skus: Optional[List[Sku]] = None
    sale_regions: Optional[List[str]] = None
    create_time: Optional[int] = Field(
        None, description='The latest update time of the product. (unit is second)'
    )
    update_time: Optional[int] = Field(
        None, description='The latest update time of the product. (unit is second)'
    )
    global_sync_failed_reasons: Optional[List[str]] = None


class Data5(BaseModel):
    total: Optional[int] = Field(None, description='')
    products: Optional[List[Product]] = None


class ApiProductsSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data5] = None


class ApiProductsDetailsGetRequest(BaseModel):
    product_id: str = Field(..., description='')
    need_audit_version: Optional[bool] = Field(None, description='')


class CategoryListItem1(BaseModel):
    id: Optional[str] = Field(None, description='')
    parent_id: Optional[str] = Field(None, description='')
    local_display_name: Optional[str] = Field(None, description='')
    is_leaf: Optional[bool] = Field(None, description='')


class Brand(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    status: Optional[int] = Field(None, description='ONLINE=1;<br>OFFLINE=2;')


class Image(BaseModel):
    height: Optional[int] = Field(None, description='')
    width: Optional[int] = Field(None, description='')
    thumb_url_list: Optional[List[str]] = None
    id: Optional[str] = Field(None, description='')
    url_list: Optional[List[str]] = None


class VideoInfo(BaseModel):
    main_url: Optional[str] = Field(None, description='')
    backup_url: Optional[str] = Field(None, description='')
    url_expire: Optional[int] = Field(None, description='')
    width: Optional[int] = Field(None, description='')
    height: Optional[int] = Field(None, description='')
    file_hash: Optional[str] = Field(None, description='')
    format: Optional[str] = Field(None, description='')
    size: Optional[int] = Field(None, description='')
    bitrate: Optional[int] = Field(None, description='')


class Video(BaseModel):
    id: Optional[str] = Field(None, description='')
    post_url: Optional[str] = Field(None, description='')
    media_type: Optional[str] = Field(None, description='')
    video_infos: Optional[List[VideoInfo]] = None


class WarrantyPeriod(BaseModel):
    warranty_id: Optional[int] = Field(None, description='')
    warranty_description: Optional[str] = Field(None, description='')


class Price1(BaseModel):
    original_price: Optional[str] = Field(None, description='')
    price_include_vat: Optional[str] = Field(None, description='')
    currency: Optional[str] = Field(None, description='')


class StockInfo1(BaseModel):
    warehouse_id: Optional[str] = Field(None, description='')
    available_stock: Optional[int] = Field(None, description='')


class ProductIdentifierCode(BaseModel):
    identifier_code: Optional[str] = Field(None, description='This is the GTIN code')
    identifier_code_type: Optional[int] = Field(
        None,
        description='Code type value: 1-GTIN、2-EAN、3-UPC、4-ISBN (input  one of them to this field)',
    )


class SkuImg(BaseModel):
    height: Optional[int] = Field(None, description='')
    width: Optional[int] = Field(None, description='')
    thumb_url_list: Optional[List[str]] = None
    id: Optional[str] = Field(None, description='')
    url_list: Optional[List[str]] = None


class SalesAttribute(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    value_id: Optional[str] = Field(None, description='')
    value_name: Optional[str] = Field(None, description='')
    sku_img: Optional[SkuImg] = None


class Sku1(BaseModel):
    id: Optional[str] = Field(None, description='')
    seller_sku: Optional[str] = Field(None, description='')
    price: Optional[Price1] = None
    stock_infos: Optional[List[StockInfo1]] = None
    product_identifier_code: Optional[ProductIdentifierCode] = None
    sales_attributes: Optional[List[SalesAttribute]] = None


class File(BaseModel):
    id: Optional[str] = Field(None, description='')
    list: Optional[List[str]] = None
    name: Optional[str] = Field(None, description='')
    type: Optional[str] = Field(None, description='')


class Image1(BaseModel):
    height: Optional[int] = Field(None, description='')
    width: Optional[int] = Field(None, description='')
    thumb_url_list: Optional[List[str]] = None
    id: Optional[str] = Field(None, description='')
    url_list: Optional[List[str]] = None


class ProductCertification1(BaseModel):
    id: Optional[str] = Field(None, description='')
    title: Optional[str] = Field(None, description='')
    files: Optional[List[File]] = None
    images: Optional[List[Image1]] = None


class SizeChart(BaseModel):
    height: Optional[int] = Field(None, description='')
    width: Optional[int] = Field(None, description='')
    thumb_url_list: Optional[List[str]] = None
    id: Optional[str] = Field(None, description='')
    url_list: Optional[List[str]] = None


class Value(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')


class ProductAttribute(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    values: Optional[List[Value]] = None


class QcReason(BaseModel):
    reason: Optional[str] = Field(None, description='')
    sub_reasons: Optional[List[str]] = None


class DeliveryService(BaseModel):
    delivery_service_id: Optional[int] = Field(None, description='Delivery service id')
    delivery_option_name: Optional[str] = Field(
        None, description='Delivery service name'
    )
    delivery_service_status: Optional[bool] = Field(
        None,
        description='This is the status of delivery service option, it means whether the delivery service is available on the current product, rather than the status of the delivery service itself.<br>ture=yes， false=no',
    )


class ExemptionOfIdentifierCode1(BaseModel):
    exemption_reason: Optional[List[int]] = None


class Data6(BaseModel):
    product_id: Optional[str] = Field(None, description='')
    product_status: Optional[int] = Field(
        None,
        description='1-draft、2-pending、3-failed(initial creation)、4-live、5-seller_deactivated、6-platform_deactivated、7-freeze 8-deleted',
    )
    product_name: Optional[str] = Field(None, description='')
    category_list: Optional[List[CategoryListItem1]] = None
    brand: Optional[Brand] = None
    images: Optional[List[Image]] = None
    video: Optional[Video] = None
    description: Optional[str] = Field(None, description='')
    warranty_period: Optional[WarrantyPeriod] = None
    warranty_policy: Optional[str] = Field(None, description='')
    package_length: Optional[int] = Field(None, description='')
    package_width: Optional[int] = Field(None, description='')
    package_height: Optional[int] = Field(None, description='')
    package_weight: Optional[str] = Field(None, description='')
    skus: Optional[List[Sku1]] = None
    product_certifications: Optional[List[ProductCertification1]] = None
    size_chart: Optional[SizeChart] = None
    is_cod_open: Optional[bool] = Field(None, description='')
    product_attributes: Optional[List[ProductAttribute]] = None
    qc_reasons: Optional[List[QcReason]] = None
    update_time: Optional[int] = Field(
        None, description='The time when the product was last updated(ms)'
    )
    create_time: Optional[int] = Field(
        None, description='The time when the product was last updated(ms)'
    )
    delivery_services: Optional[List[DeliveryService]] = None
    exemption_of_identifier_code: Optional[ExemptionOfIdentifierCode1] = None
    package_dimension_unit: Optional[str] = Field(None, description='')


class ApiProductsDetailsGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data6] = None


class Image2(BaseModel):
    id: str = Field(..., description='')


class SizeChart1(BaseModel):
    img_id: str = Field(
        ...,
        description='Only support the input of the sales attribute ID provided by the platform',
    )


class Image3(BaseModel):
    id: str = Field(
        ...,
        description='You can only use the request parameters of the UploadImg API as the request parameters',
    )


class File1(BaseModel):
    id: str = Field(
        ...,
        description='You can only use the request parameters of the UploadFile API as the request parameters',
    )
    name: str = Field(..., description='')
    type: str = Field(..., description='')


class ProductCertification2(BaseModel):
    id: str = Field(..., description='')
    images: List[Image3]
    files: List[File1]


class SkuImg1(BaseModel):
    id: str = Field(
        ...,
        description='You can only use the request parameters of the UploadImg API as the request parameters<br>At most, you can set a picture for one sales attribute. When only part of the sales attribute value is set with a picture, the system will use the product header image to fill in the sales attribute value without a picture<br>',
    )


class SalesAttribute1(BaseModel):
    attribute_id: Optional[str] = Field(
        None,
        description='Only support the input of the sales attribute ID provided by the platform<br>Enter up to three sales attributes',
    )
    attribute_name: Optional[str] = Field(None, description='')
    value_id: Optional[str] = Field(
        None,
        description='The platform does not enter existing sales attribute values by default<br>If you need to keep the existing sales attribute value, you need to enter the sales attribute value id given by the platform before. If you do not need to keep the existing sales attribute values, you do not need to enter the id assigned by the platform<br>If you need to add a new sales attribute value, you do not need to enter value_id. After the custom_value request is submitted, the merchant will get the value_id assigned by',
    )
    custom_value: Optional[str] = Field(
        None,
        description='If you need to retain the existing sales attribute value, you need to enter the sales attribute value id assigned by the platform. Among the existing sales attribute values, the sales attribute value id assigned by the platform determines the sales attribute value<br>If you need to add a new sales attribute value, for the sales attribute value, you need to enter a custom sales attribute value, and there can be no duplicate sales attribute values under the same sales attribute<br>It is recommended to a',
    )
    sku_img: SkuImg1


class StockInfo2(BaseModel):
    warehouse_id: str = Field(
        ...,
        description='This field is a required field (because some sellers will have multiple warehouses, sellers can get warehouse ID from API GetproductDetail. You must fill in the warehouse when you modify SKU).',
    )
    available_stock: int = Field(
        ...,
        description='The value should be non-negative numbers（include number 0）<br>The upper limit of the available stock value set at a time is 99999',
    )


class ProductIdentifierCode1(BaseModel):
    identifier_code: Optional[str] = Field(
        None,
        description='Identifier code logic：<br>1. Must be a numeric type<br>2. The number of characters needs to meet the requirements (GTIN: 14 digits, EAN: 8/13/14 digits, UPC: 12 digits, ISBN: 13 digits)<br>3. Different SKUs are not allowed to use the same gtin code.',
    )
    identifier_code_type: Optional[int] = Field(
        None,
        description='Code type value: 1-GTIN、2-EAN、3-UPC、4-ISBN (input  one of them to this field)',
    )


class Sku2(BaseModel):
    id: Optional[str] = Field(
        None,
        description='Optional field. If you enter a parameter, you can edit the existing SKU; If no parameter is entered, SKU is added.',
    )
    sales_attributes: List[SalesAttribute1]
    stock_infos: List[StockInfo2]
    seller_sku: Optional[str] = Field(
        None,
        description='The character length must not exceed 50<br>It is recommended to avoid using Chinese because the copy will be displayed to local users',
    )
    original_price: str = Field(
        ...,
        description='Indonesian rupiah, the minimum price is 100 ,and maximum price is 100 million.For Indonesia local to local business, please note that products with a discounted price of less than 2000 IDR may lead to a negative balance. For UK local business, the minimum price is 0.01GBP ,and maximum price is 5600 GBP For UK cross-border business, the minimum price is 0.01GBP ,and maximum price is 134.5 GBP Up to two digits after the decimal pointFor Thailand local buiness, the minimum price is 0.01TNB ,and maximum price is 260000TNB For Thailand crossborder buiness, the minimum price is 0.01THB ,and maximum price is 260000THBFor Malyasia local business(MYR), the minimum price is 0.01 MRY, and maximum price is 320000 MYRFor Vietnam local business, the minimum price is 1 VND and maximum price is 180000000 VNDFor Philippine local business，the minimum price is 0.01PHP and maximum price is 400000PHPFor Singapore local business，the minimum price is 0.01SGD and maximum price is 10000SGPFor Malyasia crossborder business(MYR), the minimum price is 0.01 MRY, and maximum price is 320000 MYRFor Vietnam crossborder business, the minimum price is 1 VND and maximum price is 1000000 VNDFor Philippine crossborder business，the minimum price is 0.01PHP and maximum price is 400000PHPFor Singapore crossborder business，the minimum price is 0.01SGD and maximum price is 400SGDUp to two digits after the decimal point.',
    )
    product_identifier_code: Optional[ProductIdentifierCode1] = None
    outer_sku_id: Optional[str] = Field(
        None, description='This is the outer sku identifier'
    )


class AttributeValue(BaseModel):
    value_id: Optional[str] = Field(
        None,
        description='Only support the input of the product attribute value ID that is provided by the platform（from GetAttribute API）',
    )
    value_name: Optional[str] = Field(
        None,
        description='This field is for you fill in the custom attribute value . Here are some conditions of the field:<br>1. This field cannot fill in mandarin.<br>2. The maximum character is 35.<br>3. This field support submits multiple values , but these custom values cannot be duplicated.',
    )


class ProductAttribute1(BaseModel):
    attribute_id: Optional[str] = Field(
        None,
        description='Only support the input of the product attribute ID that is provided by the platform（from GetAttribute API）',
    )
    attribute_values: Optional[List[AttributeValue]] = None


class ExemptionOfIdentifierCode2(BaseModel):
    exemption_reason: Optional[List[int]] = None


class ProductVideo(BaseModel):
    video_id: Optional[str] = Field(
        None,
        description='Here is the product video section . Please follow this step if you need to upload a video here:<br>1. please upload the video file via API[UploadFile]<br>2. Please get the response information (video id(file id)from API[UploadFile]) and fill the ID in this value.<br>3. this video id only support 1 id string.',
    )


class ApiProductsPutRequest(BaseModel):
    product_id: str = Field(..., description='')
    product_name: str = Field(
        ...,
        description='It is recommended to avoid using Chinese because the copy will be displayed to local users<br>The character length must not exceed 188',
    )
    description: str = Field(
        ...,
        description='Brief rules:<br>Must conform to html syntax<br>Currently only supports <p><img><ul><li> tags<br>Tags cannot be nested<br>You can only use the request parameters of the UploadImg API as the request parameters<br>up to 9 images （please convert the img link via UploadImg API）.<br>This field character limit needs to be within 10000 characters.<br>It is recommended to avoid using Chinese because the copy will be displayed to local users.<br>',
    )
    category_id: str = Field(..., description='Must be a leaf category')
    brand_id: Optional[str] = Field(
        None,
        description='You can only choose from brands that already have qualifications, and you need to ensure that the qualifications are within the validity period',
    )
    images: List[Image2]
    warranty_period: Optional[int] = Field(
        None,
        description='Need to choose among the candidate values provided by the platform:   <br>1:"4 weeks"<br>  2:"2 months"<br>  3:"3 months"<br>  4:"4 months"<br>  5:"5 months"<br>  6:"6 months"<br>  7:"7 months"<br>  8:"8 months"<br>  9:"9 months"<br>  10:"10 months"<br>  11:"11 months"<br>  12:"12 months"<br>  13:"2 years"<br>  14:"3 years"<br>  15:"1 week"<br>  16:"2 weeks"<br>  17:"18 months"<br>  18:"4 years"<br>  19:"5 years"<br>  20:"10 years"<br>  21:"lifetime warranty"<br>',
    )
    warranty_policy: Optional[str] = Field(
        None,
        description='The character length needs to be within 99<br>It is recommended to avoid using Chinese because the copy will be displayed to local users',
    )
    package_length: Optional[int] = Field(
        None,
        description='The unit is cm<br>For cross-border products, length, width and height are required; For local-to-local products, either all length, width and height are not filled in or all are filled in',
    )
    package_height: Optional[int] = Field(
        None,
        description='The unit is cm<br>For cross-border products, length, width and height are required; For local-to-local products, either all length, width and height are not filled in or all are filled in',
    )
    package_width: Optional[int] = Field(
        None,
        description='The unit is cm<br>For cross-border products, length, width and height are required; For local-to-local products, either all length, width and height are not filled in or all are filled in',
    )
    package_weight: str = Field(
        ...,
        description='The unit is kilogram （maximum is 100kg）<br>Up to two digits after the decimal point',
    )
    size_chart: SizeChart1
    product_certifications: List[ProductCertification2]
    is_cod_open: Optional[bool] = Field(
        None,
        description='The category rule determines whether this parameter is required. If the category rule is "true", you can choose to turn on or off the cod, if the category rule is "false", you are not allowed to turn on the cod',
    )
    skus: Optional[List[Sku2]] = None
    delivery_service_ids: Optional[List[str]] = None
    product_attributes: Optional[List[ProductAttribute1]] = None
    exemption_of_identifier_code: Optional[ExemptionOfIdentifierCode2] = None
    package_dimension_unit: Optional[str] = Field(
        None,
        description="This field is for America market(US) only(and this field is mandatory for US，optional for non-US region) .  And it's invalid in other countries.<br>This field indicates the unit of the product package size information. It is an optional field and only supports single selection.<br>If you didn't fill in this field when you creating the product via API, the system will use the metric dimension unit for the product by default. If you select the dimension unit in this field, the system will save the product dimension information according to the unit that selected by this field.<br>Value: imperial, metric",
    )
    product_video: Optional[ProductVideo] = None
    outer_product_id: Optional[str] = Field(
        None, description='This is outer product identifier'
    )


class SalesAttribute2(BaseModel):
    attribute_id: Optional[str] = Field(None, description='')
    value_id: Optional[str] = Field(None, description='')


class Sku3(BaseModel):
    id: Optional[str] = Field(None, description='')
    seller_sku: Optional[str] = Field(None, description='')
    sales_attributes: Optional[List[SalesAttribute2]] = None
    outer_sku_id: Optional[str] = Field(None, description='')


class Data7(BaseModel):
    product_id: Optional[str] = Field(None, description='')
    skus: Optional[List[Sku3]] = None


class ApiProductsPutResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data7] = None


class StockInfo3(BaseModel):
    warehouse_id: Optional[str] = Field(
        None,
        description='if the SKU is using one default warehouse information ,then this warehouse id is optional field. if the SKU is using other warehouse or the SKU has multiple warehouse information ,then this warehouse id and stock information are mandatory when you update stock to certian wharehouse.',
    )
    available_stock: Optional[int] = Field(
        None,
        description='The value should be non-negative numbers（include number 0）And less then 99999',
    )


class Sku4(BaseModel):
    id: Optional[str] = Field(None, description='SKU_ID')
    stock_infos: Optional[List[StockInfo3]] = None


class ApiProductsStocksPutRequest(BaseModel):
    product_id: str = Field(..., description='')
    skus: Optional[List[Sku4]] = None


class FailedSku(BaseModel):
    id: Optional[str] = Field(None, description='')
    failed_warehouse_ids: Optional[List[str]] = None


class Data8(BaseModel):
    failed_skus: Optional[List[FailedSku]] = None


class ApiProductsStocksPutResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data8] = None


class ApiProductsAttributesGetRequest(BaseModel):
    category_id: str = Field(
        ..., description='Only support the input of leaf categories'
    )


class InputType(BaseModel):
    is_mandatory: Optional[bool] = Field(None, description='Is the attribute required')
    is_multiple_selected: Optional[bool] = Field(
        None, description='Whether the attribute value supports multiple selection'
    )
    is_customized: Optional[bool] = Field(
        None, description='Whether the attribute value supports customization'
    )


class Value1(BaseModel):
    id: Optional[int] = Field(None, description='Attributes values ID')
    name: Optional[str] = Field(None, description='Attributes values name')


class Attribute(BaseModel):
    id: Optional[str] = Field(None, description='Attributes name ID')
    name: Optional[str] = Field(
        None,
        description='Attributes name, different names in different operating countries',
    )
    attribute_type: Optional[int] = Field(
        None, description='2-SALES_PROPERTY,<br><br>  3-PRODUCT_PROPERTY'
    )
    input_type: Optional[InputType] = None
    values: Optional[List[Value1]] = None


class Data9(BaseModel):
    attributes: Optional[List[Attribute]] = None


class ApiProductsAttributesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data9] = None


class ApiProductsUploadImgsPostRequest(BaseModel):
    img_data: str = Field(
        ...,
        description='Input image format file. The picture file is a string generated by base64 encoding.<br>Picture files,picture formats support JPG, JPEG, PNG, picture pixels at least 600 \\* 600 and at most 20000 \\* 20000, Max size of original image: 5MB',
    )
    img_scene: int = Field(
        ...,
        description='1:"PRODUCT_IMAGE" The ratio of horizontal and vertical is recommended to be 1:1<br> 2:"DESCRIPTION_IMAGE"<br> 3:"ATTRIBUTE_IMAGE " The ratio of horizontal and vertical is recommended to be 1:1<br> 4:"CERTIFICATION_IMAGE"<br> 5:"SIZE_CHART_IMAGE"',
    )


class Data10(BaseModel):
    img_id: Optional[str] = Field(None, description='image uri')
    img_url: Optional[str] = Field(None, description='image url')
    img_height: Optional[int] = Field(None, description='')
    img_width: Optional[int] = Field(None, description='')
    img_scene: Optional[int] = Field(
        None,
        description='1:"PRODUCT_IMAGE"<br>2:"DESCRIPTION_IMAGE"<br>3:"ATTRIBUTE_IMAGE "<br>4:"CERTIFICATION_IMAGE"<br>5:"SIZE_CHART_IMAGE"',
    )


class ApiProductsUploadImgsPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data10] = None


class ApiProductsInactivatedProductsPostRequest(BaseModel):
    product_ids: List[str]


class Data11(BaseModel):
    failed_product_ids: Optional[List[str]] = None


class ApiProductsInactivatedProductsPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data11] = None


class Sku5(BaseModel):
    id: str = Field(..., description='')
    original_price: str = Field(
        ...,
        description='Indonesian rupiah, the minimum price is 100 ,and maximum price is 100 million.For Indonesia local to local business, please note that products with a discounted price of less than 2000 IDR may lead to a negative balance. For UK local business, the minimum price is 0.01GBP ,and maximum price is 5600 GBP For UK cross-border business, the minimum price is 0.01GBP ,and maximum price is 134.5 GBP Up to two digits after the decimal pointFor Thailand local buiness, the minimum price is 0.01TNB ,and maximum price is 260000TNB For Thailand crossborder buiness, the minimum price is 0.01THB ,and maximum price is 260000THBFor Malyasia local business(MYR), the minimum price is 0.01 MRY, and maximum price is 320000 MYRFor Vietnam local business, the minimum price is 1 VND and maximum price is 180000000 VNDFor Philippine local business，the minimum price is 0.01PHP and maximum price is 400000PHPFor Singapore local business，the minimum price is 0.01SGD and maximum price is 10000SGPFor Malyasia crossborder business(MYR), the minimum price is 0.01 MRY, and maximum price is 320000 MYRFor Vietnam crossborder business, the minimum price is 1 VND and maximum price is 1000000 VNDFor Philippine crossborder business，the minimum price is 0.01PHP and maximum price is 400000PHPFor Singapore crossborder business，the minimum price is 0.01SGD and maximum price is 400SGDUp to two digits after the decimal point.',
    )


class ApiProductsPricesPutRequest(BaseModel):
    product_id: str = Field(..., description='')
    skus: List[Sku5]


class Data12(BaseModel):
    failed_sku_ids: Optional[List[str]] = None


class ApiProductsPricesPutResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data12] = None


class ApiProductsUploadFilesPostRequest(BaseModel):
    file_data: str = Field(
        ...,
        description='Import the file in pdf and mp4 format. The file is a string generated by base64 encoding. If the file type is pdf, the original file size must not exceed 10M. If the file type is mp4, the original file size must not exceed 20M and the video aspect ratio is between 9:16 and 16:9.',
    )
    file_name: str = Field(..., description='')


class Data13(BaseModel):
    file_id: Optional[str] = Field(None, description='')
    file_url: Optional[str] = Field(None, description='File uri')
    file_name: Optional[str] = Field(None, description='')
    file_type: Optional[str] = Field(None, description='')


class ApiProductsUploadFilesPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data13] = None
