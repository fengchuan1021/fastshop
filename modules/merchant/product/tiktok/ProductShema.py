#   timestamp: 2022-12-16T05:24:55+00:00

from __future__ import annotations
from typing import Literal


from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class SalesAttribute(BaseModel):
    attribute_id: Optional[str] = None
    attribute_name: Optional[str] = None
    value_id: Optional[str] = None
    custom_value: Optional[str] = None


class StockInfo(BaseModel):
    warehouse_id: str
    available_stock: int


class Sku(BaseModel):
    sales_attributes: Optional[List[SalesAttribute]] = None
    stock_infos: Optional[List[StockInfo]] = None
    seller_sku: Optional[str] = Field(None, max_length=50)
    original_price: str
    outer_sku_id: Optional[str] = None


class AttributeValue(BaseModel):
    value_id: Optional[str] = None
    value_name: Optional[str] = None


class ProductAttribute(BaseModel):
    attribute_id: Optional[str] = None
    attribute_values: Optional[List[AttributeValue]] = None


class ProductVideo(BaseModel):
    video_id: Optional[str] = None


class TiktokCreateproductShema(BaseModel):
    product_name: str = Field(..., max_length=255, min_length=25)
    description: str = Field(..., max_length=10000)
    category_id: str
    brand_id: Optional[str] = None
    images: Dict[str, Any]
    warranty_period: Optional[int] = None
    warranty_policy: Optional[str] = Field(None, max_length=99)
    package_length: Optional[int] = None
    package_width: Optional[int] = None
    package_height: Optional[int] = None
    package_weight: str
    is_cod_open: Optional[bool] = False
    skus: List[Sku]
    delivery_service_ids: Optional[List[str]] = None
    product_attributes: Optional[List[ProductAttribute]] = None
    package_dimension_unit: Optional[str] = None
    product_video: Optional[ProductVideo] = None
    outer_product_id: Optional[str] = None



