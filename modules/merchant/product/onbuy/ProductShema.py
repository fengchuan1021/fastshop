#   timestamp: 2022-12-26T09:07:20+00:00

from __future__ import annotations
from typing import Literal


from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Video(BaseModel):
    label: Optional[str] = None
    url: Optional[str] = None


class Document(BaseModel):
    label: Optional[str] = None
    url: Optional[str] = None


class ProductDatum(BaseModel):
    label: Optional[str] = None
    value: Optional[str] = None
    group: Optional[str] = None


class New(BaseModel):
    sku: Optional[str] = None
    group_sku: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    handling_time: Optional[int] = None
    return_time: Optional[int] = None
    free_returns: Optional[str] = None
    warranty: Optional[int] = None
    delivery_template_id: Optional[int] = None
    sale_price: Optional[float] = None
    sale_start_date: Optional[str] = None
    sale_end_date: Optional[str] = None


class Listings(BaseModel):
    new: Optional[New] = None


class Feature(BaseModel):
    option_id: Optional[int] = None
    name: Optional[str] = None
    hex: Optional[str] = None


class TechnicalDetailItem(BaseModel):
    detail_id: Optional[int] = None
    value: Optional[str] = None
    unit: Optional[str] = None


class Variant1(BaseModel):
    name: Optional[str] = None


class Variant2(BaseModel):
    name: Optional[str] = None


class OnbuyCreateProductShema(BaseModel):
    site_id: int
    category_id: int
    published: Optional[int] = 1
    product_name: str
    mpn: Optional[str] = None
    product_codes: List[str]
    summary_points: Optional[List[str]] = None
    description: Optional[str] = None
    brand_name: str
    brand_id: int
    videos: Optional[List[Video]] = None
    documents: Optional[List[Document]] = None
    default_image: str
    additional_images: Optional[List[str]] = None
    rrp: Optional[float] = None
    product_data: Optional[List[ProductDatum]] = None
    listings: Optional[Listings] = None
    features: Optional[List[Feature]] = None
    technical_detail: Optional[List[TechnicalDetailItem]] = None
    variant_1: Optional[Variant1] = None
    variant_2: Optional[Variant2] = None
    variants: Optional[List[List[Dict[str, Any]]]] = None



