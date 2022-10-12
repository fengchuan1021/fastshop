from pydantic import BaseModel
from typing import List, Optional, Literal


class AddProductOutShema(BaseModel):
    status:str
    msg:str=''



class Attribute(BaseModel):
    name:str
    value:str
class ProductImage(BaseModel):
    image_url:str
    image_alt:str
    image_order:int
class SingleProduct(BaseModel):
    name_en: str
    description_en: Optional[str]
    brand_en: Optional[str]
    price: float
    stock: int
    sku: str
    attributes: Optional[List[Attribute]]
    images:Optional[List[ProductImage]]
class AddProductInShema(BaseModel):
    name_en: str
    description_en: str
    brand_en: str
    price: float
    sku:str
    stock:int
    # attributes:List[Attribute]
    # subproducts: List[SingleProduct] = []
    # images: List[ProductImage] = []

class BackendProductAddproductimgPostRequest(BaseModel):
    file: bytes



class BackendProductAddproductimgPostResponse(BaseModel):
    status: Literal['success','failed']
    fileurl: str



class BackendProductPrefetchproductidGetResponse(BaseModel):
    status: Literal['success','failed']
    product_id: str
