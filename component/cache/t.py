#type: ignore
from typing import Dict,Type,_BaseGenericAlias
import typing
async def getporductByid(id:int)->Dict:
    print('in function execute!!')
    return {"id":id,"name":"iphone",'description':"rediphone"}

print(getporductByid.__annotations__.get('return')==typing._SpecialGenericAlias)