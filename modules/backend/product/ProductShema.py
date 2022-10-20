from pydantic import BaseModel
from typing import List, Optional, Literal, Dict, Any


class ProductImage(BaseModel):
    image_url:str
    image_alt:str
    image_order:int


class BackendProductAddproductimgPostRequest(BaseModel):
    file: bytes



class BackendProductAddproductimgPostResponse(BaseModel):
    status: Literal['success','failed']
    fileurl: str



class BackendProductPrefetchproductidGetResponse(BaseModel):
    status: Literal['success','failed']
    product_id: str




class Attribute(BaseModel):
    name: str
    value: str

class Image(BaseModel):
    image_url:str
    image_alt:Optional[str]=''
class Variant(BaseModel):
    name_en: str
    brand_en: Optional[str]
    brand_id:Optional[str]
    status:Optional[Literal["ONLINE","OFFLINE","EDITING"]]
    price: float
    sku: str
    product_id: Optional[str]
    image:List[Image]
class Specification(BaseModel):
    name:str
    value:List[str]
class BackendProductAddproductPostRequest(BaseModel):
    name_en: str
    description_en: Optional[str]
    brand_en: str
    brand_id:str
    status:Literal["ONLINE","OFFLINE","EDITING"]
    price: float
    sku: str

    attributes: Optional[List[Attribute]] = None
    product_id: Optional[str]
    specifications: Optional[List[Specification]]
    subproducts: Optional[List['Variant']]
    image:List[Image]
    video:Optional[str]



class Product(BaseModel):
    id: int
    productName: str
    price: float
    barcode: str
    skuId: int


class BackendProductAddproductPostResponse(BaseModel):
    status: Literal['success','skunotfound']
    product: Optional[Product]
    msg:Optional[str]

class BackendProductProductlistGetRequest(BaseModel):
    pagenum: int
    pagesize: int
    filter: Dict[str, Any]



class Datum(BaseModel):
    product_id: str
    name_en: str
    brand_en: str
    variant: Optional[List[Dict[str, Any]]] = None
    class Config:
        orm_mode = True

class BackendProductProductlistGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None

class BackendProductPreviewproductbyvariantidVariantidGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Any