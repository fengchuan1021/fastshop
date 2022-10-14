from pydantic import BaseModel
from typing import List, Optional, Literal






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
    key: str
    value: str

class Variant(BaseModel):
    name_en: str
    brand_en: str
    brand_id:str
    status:Literal["ONLINE","OFFLINE","EDITING"]
    price: float
    sku: str
    product_id: Optional[str]
    image:List[str]

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
    specifications: Optional[List[str]]
    subproduct: Optional[List['Variant']]
    image:List[str]
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