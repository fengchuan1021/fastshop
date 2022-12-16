#   timestamp: 2022-12-16T07:17:27+00:00

from __future__ import annotations
from typing import Literal


from typing import List, Optional

from pydantic import BaseModel


class DefaultShippingPrice1(BaseModel):
    amount: int
    currency_code: str


class DefaultShippingPrice(BaseModel):
    default_shipping_price: DefaultShippingPrice1
    warehouse_id: str


class Price(BaseModel):
    amount: int
    currency_code: str


class AdditionalPrice(BaseModel):
    amount: int
    currency_code: str


class Override(BaseModel):
    is_enabled: Optional[bool] = None
    price: Optional[Price] = None
    destination: Optional[str] = None
    max_delivery_days: Optional[int] = None
    additional_price: Optional[AdditionalPrice] = None


class AdditionalPrice1(BaseModel):
    amount: int
    currency_code: str


class Price1(BaseModel):
    amount: int
    currency_code: str


class ShippingDetail(BaseModel):
    is_enabled: Optional[bool] = None
    max_delivery_days: Optional[int] = None
    overrides: List[Override]
    destination: str
    additional_price: Optional[AdditionalPrice1] = None
    price: Optional[Price1] = None


class WarehouseToShipping(BaseModel):
    shipping_details: List[ShippingDetail]
    warehouse_id: str


class Msrp(BaseModel):
    amount: int
    currency_code: str


class Video(BaseModel):
    url: str


class Attribute(BaseModel):
    name: str
    value: Optional[List[str]] = None


class MainImage(BaseModel):
    url: str
    variation_skus: Optional[List[str]] = None
    is_clean_image: bool


class Price2(BaseModel):
    amount: int
    currency_code: str


class Cost(BaseModel):
    amount: int
    currency_code: str


class Attribute1(BaseModel):
    name: str
    value: Optional[List[str]] = None


class Inventory(BaseModel):
    inventory: Optional[int] = None
    warehouse_id: Optional[str] = None


class Option(BaseModel):
    name: str
    value: str


class CustomsDeclaredValue(BaseModel):
    amount: int
    currency_code: str


class LogisticsDetails(BaseModel):
    origin_country: Optional[str] = None
    weight: Optional[int] = None
    customs_hs_code: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
    length: Optional[int] = None
    pieces: Optional[int] = None
    declared_name: Optional[str] = None
    customs_declared_value: Optional[CustomsDeclaredValue] = None
    restricted_flags: Optional[List[str]] = None
    declared_local_name: Optional[str] = None


class Variation(BaseModel):
    sku: str
    quantity_value: Optional[int] = None
    price: Price2
    cost: Optional[Cost] = None
    gtin: Optional[str] = None
    attributes: Optional[List[Attribute1]] = None
    inventories: List[Inventory]
    options: Optional[List[Option]] = None
    logistics_details: Optional[LogisticsDetails] = None


class ExtraImage(BaseModel):
    url: Optional[str] = None
    variation_skus: Optional[List[str]] = None
    is_clean_image: Optional[bool] = None


class WishCreateProduct(BaseModel):
    california_prop65_chemical_names: Optional[List[str]] = None
    default_shipping_prices: List[DefaultShippingPrice]
    description: str
    tags: Optional[List[str]] = None
    subcategory_id: Optional[int] = None
    california_prop65_warning_type: Optional[str] = None
    max_quantity: Optional[int] = None
    reference_value: Optional[int] = None
    warehouse_to_shippings: List[WarehouseToShipping]
    msrp: Optional[Msrp] = None
    video: Optional[Video] = None
    condition: str
    brand_id: Optional[str] = None
    attributes: List[Attribute]
    parent_sku: str
    unit: Optional[str] = None
    name: str
    main_image: MainImage
    variations: List[Variation]
    extra_images: Optional[List[ExtraImage]] = None

