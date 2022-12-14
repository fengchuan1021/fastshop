from functools import wraps
from typing import Dict, Callable, Any, TypeVar, cast

import Models
from common import cmdlineApp

F = TypeVar('F', bound=Callable[..., Any])
from collections import defaultdict
rules=defaultdict(list)
def orderrule(group:str='',name_en:str='',name_cn:str='')->Callable[[F], F]:
    def decorator(func: F) -> F:
        rules[group].append({'name_cn':name_cn,'name_en':name_en,'func':func.__name__})
        @wraps(func)
        async def inner(*args: Any, **kwargs: Any) -> Any:
            return await func(*args,**kwargs)
        return cast(F, inner)
    return decorator
class ReviewOrderService():
    async def getRules(self)->Any:
        global rules
        print(rules)
        return rules
    async def platformInSpecificMarket(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        pass

    @orderrule('logistics', 'has specific receiver telphone ', '包含特定电话')
    async def hasSpecificPhoneNumber(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.telephone in data['data']:
            return False
        return True
    @orderrule('logistics','has specific receiver name ','包含特定收件人')
    async def Address_receivernameIn(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.firstname in data['data']:
            return False
        return True
    @orderrule('logistics', 'has specific receiver address ', '包含特定收件地址')
    async def Address_receiverphoneIn(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.telephone in data['data']:
            return False
        return True
    @orderrule('order', 'from specific platform ', '来自特定平台')
    async def orderfromspecificplatform(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.telephone in data['data']:
            return False
        return True
    @orderrule('order', 'from specific shop', '来自特定商店')
    async def orderfromspecificshop(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.telephone in data['data']:
            return False
        return True
    @orderrule('order', 'order amount ', '订单金额')
    async def orderamount(self,order:Models.Order,address:Models.OrderAddress,data:Dict)->bool:
        if address.telephone in data['data']:
            return False
        return True
if __name__ == "__main__":
    async def test(db):#type: ignore
        (await ReviewOrderService()).getRules()
    cmdlineApp(test)()