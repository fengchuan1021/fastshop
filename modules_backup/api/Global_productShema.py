#   timestamp: 2022-10-29T02:15:04+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class Sku(BaseModel):
    id: str = Field(..., description='')
    original_price: str = Field(
        ...,
        description='货币为美元，小数点后最多2位<br>-当global商品未发布状态下，价格更新将会只更新global价格。<br>-当global商品已发布至local的状态下，当商家选择调用该接口更新global价格的话，系统直接更新global价格并自动计算并更新local价格（计算公式为系统的默认算价公式）',
    )


class ApiProductGlobalProductsPricesPutRequest(BaseModel):
    global_product_id: int = Field(..., description='')
    skus: List[Sku]


class FailedSku(BaseModel):
    global_sku_id: Optional[int] = Field(None, description='')
    local_sku_id: Optional[int] = Field(None, description='')
    region: Optional[str] = Field(None, description='')
    failed_code: Optional[int] = Field(None, description='')
    failed_msg: Optional[str] = Field(None, description='')


class Data(BaseModel):
    failed_skus: Optional[List[FailedSku]] = None


class ApiProductGlobalProductsPricesPutResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class CategoryListItem(BaseModel):
    id: Optional[int] = Field(None, description='类目ID')
    parent_id: Optional[int] = Field(None, description='父类目ID')
    category_name: Optional[str] = Field(None, description='类目名称')
    is_leaf: Optional[bool] = Field(None, description='该类目是否为叶子类目，是 或 否')


class Data1(BaseModel):
    category_list: Optional[List[CategoryListItem]] = None


class ApiProductGlobalProductsCategoriesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiProductGlobalProductsDeleteRequest(BaseModel):
    global_product_ids: List[str]


class Data2(BaseModel):
    failed_global_product_ids: Optional[List[str]] = None


class ApiProductGlobalProductsDeleteResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None


class ApiProductGlobalProductsCategoriesRulesGetRequest(BaseModel):
    category_id: Optional[str] = Field(None, description='')


class ProductCertification(BaseModel):
    id: Optional[int] = Field(None, description='Product Qualification ID')
    name: Optional[str] = Field(
        None,
        description='The name of the product qualification (that is, the product qualification type, such as SNI, BPOM, etc.)',
    )
    sample: Optional[str] = Field(None, description='')
    is_mandatory: Optional[bool] = Field(
        None,
        description='This field indicates whether the qualification field of the global product under this category is mandatory.<br>The generation logic of whether the product qualification is mandatory:<br>If it is mandatory in all available countries/regions of the seller, the qualification is mandatory when the seller publishes global products;<br>If it is not mandatory in one or more of the countries/regions available to the seller, the qualification is not mandatory when the seller publishes global products.<br>',
    )
    mandatory_regions: Optional[List[str]] = None
    optional_regions: Optional[List[str]] = None


class SizeChartRule(BaseModel):
    is_size_chart_mandatory: Optional[bool] = Field(
        None,
        description='This field indicates whether the size chart is mandatory when creating a global product, true means mandatory, and false means not mandatory.',
    )


class CategoryRule(BaseModel):
    product_certifications: Optional[List[ProductCertification]] = None
    support_size_chart: Optional[bool] = Field(
        None,
        description="This field indicates that global products support the size chart if the size chart is supported in one or more of the seller's available regions.",
    )
    size_chart_rule: Optional[SizeChartRule] = None


class Data3(BaseModel):
    category_rules: Optional[List[CategoryRule]] = None


class ApiProductGlobalProductsCategoriesRulesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data3] = None


class ApiProductGlobalProductsSearchPostRequest(BaseModel):
    status: Optional[int] = Field(
        None,
        description='"1": "Published",<br>  "2": "Created",<br>  "3": "Draft",<br>  "4": "Deleted"',
    )
    seller_sku_list: Optional[List[str]] = None
    page_size: int = Field(..., description='pageSize')
    page_number: int = Field(..., description='pageNumbers')
    update_time_from: Optional[int] = Field(
        None,
        description="1、The most recently updated time of the product, here is a product data time range filtering items (from the time of update_time_from to the time of update_time_to);<br>2、If the seller only enters update_time_from, the TT default time of update_time_to is the current time (i.e. the latest time).<br>3、If the seller only enters update_time_to, the TT default update_time_from time defaults to the seller's opening time.<br>4、we recommend that sellers are best to use a combination of two fields update_time_from and update_time_to to accurately query the product list.<br>5、UTC time must be used.",
    )
    update_time_to: Optional[int] = Field(
        None,
        description="1、The most recently updated time of the product, here is a product data time range filtering items (from the time of update_time_from to the time of update_time_to);.<br>2、If the seller only enters update_time_from, the TT default time of update_time_to is the current time (i.e. the latest time).<br>3、If the seller only enters update_time_to, the TT default update_time_from time defaults to the seller's opening time.<br>4、we recommend that sellers are best to use a combination of two fields update_time_from and update_time_to to accurately query the product list.<br>5、UTC time must be used.",
    )
    create_time_from: Optional[int] = Field(
        None,
        description='The creation time of the product, which is a time range filter for the product data (from the time of create_time_from to the time of create_time_to).<br>If the seller only enters create_time_from, then TT defaults the time of create_time_to to the current time (i.e. the latest time).<br>If the seller only enters create_time_to, the TT default time of create_time_from defaults to the time the seller opened the store.<br>We recommend that sellers better use a combination of two fields create_time_from and create_time_to to accurately query the product list.<br>5、UTC time must be used.<br>',
    )
    create_time_to: Optional[int] = Field(
        None,
        description='The creation time of the product, which is a time range filter for the product data (from the time of create_time_from to the time of create_time_to).<br>If the seller only enters create_time_from, then TT defaults the time of create_time_to to the current time (i.e. the latest time).<br>If the seller only enters create_time_to, the TT default time of create_time_from defaults to the time the seller opened the store.<br>We recommend that sellers better use a combination of two fields create_time_from and create_time_to to accurately query the product list.<br>5、UTC time must be used.<br>',
    )


class Sku1(BaseModel):
    id: Optional[str] = Field(None, description='')
    seller_sku: Optional[str] = Field(None, description='')


class GlobalProduct(BaseModel):
    id: Optional[str] = Field(None, description='')
    name: Optional[str] = Field(None, description='')
    status: Optional[int] = Field(
        None,
        description='{<br>  "1": "Published",<br>  "2": "Created",<br>  "3": "Draft",<br>  "4": "Deleted"<br>}',
    )
    skus: Optional[List[Sku1]] = None
    create_time: Optional[int] = Field(None, description='Create time of this product')
    update_time: Optional[int] = Field(None, description='Update time of this product')


class Data4(BaseModel):
    total: Optional[int] = Field(None, description='')
    global_products: Optional[List[GlobalProduct]] = None


class ApiProductGlobalProductsSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data4] = None


class GlobalProductSkuItem(BaseModel):
    id: int = Field(..., description='Global商品SKU ID')
    original_price: Optional[str] = Field(
        None,
        description='1.非必填<br>2.商家可以根据具体情况自行写入该Global SKU 发布在local店铺中的SKU原价。<br>3.如果商家未填写SKU原价，则系统默认按照公式进行换算（此处逻辑和fans商品管理端的价格换算一致：local price=global price*VAT税率*市场汇率+预估运费）<br>4.各个区域的币种：<br>GB：英镑<br>ID：印尼盾<br>TH：泰铢<br>MY：马来西亚令吉<br>PH：菲律宾比索',
    )
    warehouse_id: Optional[int] = Field(None, description='仓库ID<br>如果未填写，默认填入默认仓库')
    available_stock: int = Field(
        ...,
        description='1.商家可以根据具体情况自行写入该Global SKU 发布在local店铺中的SKU的库存量。<br>2.库存量不做加总校验，即，如果local商品库存大于Global库存，则直接更新global库存=所有local库存和即可。<br>',
    )


class PublishableShop(BaseModel):
    region: str = Field(
        ..., description='枚举：<br>"GB",<br> "ID",<br> "MY",<br> "TH",<br> "PH"'
    )
    global_product_sku: List[GlobalProductSkuItem]


class ApiProductGlobalProductsPublishPostRequest(BaseModel):
    global_product_id: int = Field(..., description='global商品的product ID')
    publishable_shops: List[PublishableShop]


class LocalSaleAttribute(BaseModel):
    attribute_id: Optional[int] = Field(None, description='local SKU id对应的销售属性ID')
    value_id: Optional[int] = Field(None, description='local SKU id对应的销售属性值ID')


class Sku2(BaseModel):
    global_sku_id: Optional[int] = Field(None, description='global商品SKU id')
    local_sku_id: Optional[int] = Field(None, description='发布到local所生成的local SKU id')
    local_seller_sku: Optional[str] = Field(
        None, description='local SKU id对应的seller SKU'
    )
    local_sale_attributes: Optional[List[LocalSaleAttribute]] = None


class PublishListItem(BaseModel):
    shop_region: Optional[str] = Field(
        None, description='目标发布店铺所属区域( "GB","ID", "TH","MY","PH")<br>'
    )
    shop_id: Optional[int] = Field(None, description='目标发布店铺ID')
    local_product_publish_result: Optional[int] = Field(
        None, description='local商品发布结果<br>0：成功<br>1：存草稿<br>2：失败'
    )
    local_product_id: Optional[int] = Field(
        None, description='local商品发布结果<br>0：成功<br>1：存草稿<br>2：失败'
    )
    skus: Optional[List[Sku2]] = None


class Data5(BaseModel):
    publish_list: Optional[List[PublishListItem]] = None


class ApiProductGlobalProductsPublishPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data5] = None


class ApiProductGlobalProductsAttributesGetRequest(BaseModel):
    category_id: int = Field(..., description='仅支持叶子类目ID')


class InputType(BaseModel):
    is_mandatory: Optional[bool] = Field(
        None, description='是否必填，返回是或者否<br>指商品创建、编辑接口的sale_attributes里边是否必填这个属性'
    )
    mandatory_regions: Optional[List[str]] = None
    is_multiple_selected: Optional[bool] = Field(None, description='属性值是否支持多选')
    is_customized: Optional[bool] = Field(None, description='属性值是否支持自定义输入')


class Value(BaseModel):
    id: Optional[int] = Field(None, description='属性值ID(平台提供的属性值)')
    name: Optional[str] = Field(None, description='属性名')


class Attribute(BaseModel):
    id: Optional[int] = Field(None, description='属性ID')
    name: Optional[str] = Field(None, description='属性名称')
    attribute_type: Optional[int] = Field(
        None,
        description='{<br>  "2": "SALES_PROPERTY",<br>  "3": "PRODUCT_PROPERTY"<br>}',
    )
    input_type: Optional[InputType] = None
    values: Optional[List[Value]] = None


class Data6(BaseModel):
    attributes: Optional[List[Attribute]] = None


class ApiProductGlobalProductsAttributesGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data6] = None
