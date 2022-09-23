from pydantic import BaseModel
from typing import List
class Subproduct(BaseModel):
    productname_en: str
    price: float
    stock: int
class AddProductInShema(BaseModel):
    productname_en:str
    price:float
    stock:int
    subproduct:List[Subproduct]=[]

class AddProductOutShema(BaseModel):
    status:str
    msg:str=''