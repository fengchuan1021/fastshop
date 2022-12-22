#   timestamp: 2022-12-22T05:12:03+00:00

from __future__ import annotations
from typing import Literal


from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class CategoryLink(BaseModel):
    position: Optional[int] = None
    category_id: Optional[str] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class ProductLink(BaseModel):
    id: Optional[str] = None
    sku: Optional[str] = None
    option_id: Optional[int] = None
    qty: Optional[int] = None
    position: Optional[int] = None
    is_default: Optional[bool] = None
    price: Optional[int] = None
    price_type: Optional[int] = None
    can_change_quantity: Optional[int] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class BundleProductOption(BaseModel):
    option_id: Optional[int] = None
    title: Optional[str] = None
    required: Optional[bool] = None
    type: Optional[str] = None
    position: Optional[int] = None
    sku: Optional[str] = None
    product_links: Optional[List[ProductLink]] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class StockItem(BaseModel):
    item_id: int
    product_id: int
    stock_id: int
    qty: int
    is_in_stock: bool
    is_qty_decimal: bool
    show_default_notification_message: bool
    use_config_min_qty: bool
    min_qty: int
    use_config_min_sale_qty: int
    min_sale_qty: int
    use_config_max_sale_qty: bool
    max_sale_qty: int
    use_config_backorders: bool
    backorders: int
    use_config_notify_stock_qty: bool
    notify_stock_qty: int
    use_config_qty_increments: bool
    qty_increments: int
    use_config_enable_qty_inc: bool
    enable_qty_increments: bool
    use_config_manage_stock: bool
    manage_stock: bool
    low_stock_date: str
    is_decimal_divided: bool
    stock_status_changed_auto: int
    extension_attributes: Dict[str, Any]


class DiscountData(BaseModel):
    amount: int
    base_amount: int
    original_amount: int
    base_original_amount: int


class Discount(BaseModel):
    discount_data: Optional[DiscountData] = None
    rule_label: Optional[str] = None
    rule_id: Optional[int] = None


class LinkFileContent(BaseModel):
    file_data: str
    name: str
    extension_attributes: Dict[str, Any]


class SampleFileContent(BaseModel):
    file_data: str
    name: str
    extension_attributes: Dict[str, Any]


class DownloadableProductLink(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    sort_order: Optional[int] = None
    is_shareable: Optional[int] = None
    price: Optional[int] = None
    number_of_downloads: Optional[int] = None
    link_type: Optional[str] = None
    link_file: Optional[str] = None
    link_file_content: Optional[LinkFileContent] = None
    link_url: Optional[str] = None
    sample_type: Optional[str] = None
    sample_file: Optional[str] = None
    sample_file_content: Optional[SampleFileContent] = None
    sample_url: Optional[str] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class SampleFileContent1(BaseModel):
    file_data: str
    name: str
    extension_attributes: Dict[str, Any]


class DownloadableProductSample(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    sort_order: Optional[int] = None
    sample_type: Optional[str] = None
    sample_file: Optional[str] = None
    sample_file_content: Optional[SampleFileContent1] = None
    sample_url: Optional[str] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class GiftcardAmount(BaseModel):
    attribute_id: Optional[int] = None
    website_id: Optional[int] = None
    value: Optional[int] = None
    website_value: Optional[int] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class Value(BaseModel):
    value_index: Optional[int] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class ConfigurableProductOption(BaseModel):
    id: Optional[int] = None
    attribute_id: Optional[str] = None
    label: Optional[str] = None
    position: Optional[int] = None
    is_use_default: Optional[bool] = None
    values: Optional[List[Value]] = None
    extension_attributes: Optional[Dict[str, Any]] = None
    product_id: Optional[int] = None


class ExtensionAttributes(BaseModel):
    website_ids: List[int]
    category_links: List[CategoryLink]
    bundle_product_options: List[BundleProductOption]
    stock_item: StockItem
    discounts: List[Discount]
    downloadable_product_links: List[DownloadableProductLink]
    downloadable_product_samples: List[DownloadableProductSample]
    giftcard_amounts: List[GiftcardAmount]
    configurable_product_options: List[ConfigurableProductOption]
    configurable_product_links: List[int]


class ExtensionAttributes1(BaseModel):
    qty: int


class ProductLink1(BaseModel):
    sku: Optional[str] = None
    link_type: Optional[str] = None
    linked_product_sku: Optional[str] = None
    linked_product_type: Optional[str] = None
    position: Optional[int] = None
    extension_attributes: Optional[ExtensionAttributes1] = None


class Value1(BaseModel):
    title: Optional[str] = None
    sort_order: Optional[int] = None
    price: Optional[int] = None
    price_type: Optional[str] = None
    sku: Optional[str] = None
    option_type_id: Optional[int] = None


class Option(BaseModel):
    product_sku: Optional[str] = None
    option_id: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    sort_order: Optional[int] = None
    is_require: Optional[bool] = None
    price: Optional[int] = None
    price_type: Optional[str] = None
    sku: Optional[str] = None
    file_extension: Optional[str] = None
    max_characters: Optional[int] = None
    image_size_x: Optional[int] = None
    image_size_y: Optional[int] = None
    values: Optional[List[Value1]] = None
    extension_attributes: Optional[Dict[str, Any]] = None


class Content(BaseModel):
    base64_encoded_data: str
    type: str
    name: str


class VideoContent(BaseModel):
    media_type: str
    video_provider: str
    video_url: str
    video_title: str
    video_description: str
    video_metadata: str


class ExtensionAttributes2(BaseModel):
    video_content: VideoContent


class MediaGalleryEntry(BaseModel):
    id: Optional[int] = None
    media_type: Optional[str] = None
    label: Optional[str] = None
    position: Optional[int] = None
    disabled: Optional[bool] = None
    types: Optional[List[str]] = None
    file: Optional[str] = None
    content: Optional[Content] = None
    extension_attributes: Optional[ExtensionAttributes2] = None


class ExtensionAttributes3(BaseModel):
    percentage_value: int
    website_id: int


class TierPrice(BaseModel):
    customer_group_id: Optional[int] = None
    qty: Optional[int] = None
    value: Optional[int] = None
    extension_attributes: Optional[ExtensionAttributes3] = None


class CustomAttribute(BaseModel):
    attribute_code: Optional[str] = None
    value: Optional[str] = None


class MagentoProductShema(BaseModel):
    sku: str
    name: str
    attribute_set_id: Optional[int] = None
    price: float
    status: int
    visibility: int
    type_id: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    weight: Optional[int] = None
    extension_attributes: Optional[ExtensionAttributes] = None
    product_links: Optional[List[ProductLink1]] = None
    options: Optional[List[Option]] = None
    media_gallery_entries: Optional[List[MediaGalleryEntry]] = None
    tier_prices: Optional[List[TierPrice]] = None
    custom_attributes: Optional[List[CustomAttribute]] = None



