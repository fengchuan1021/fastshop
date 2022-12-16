from functools import wraps
from typing import Dict, Callable, Any, TypeVar, cast

import orjson

import Models



class LogisticsRuleService():


    async def hasSpecificPhoneNumber(self,item:Dict,order:Models.Order)->bool:

        return True

    async def normal(self,item:Dict,order:Models.Order)->Any:
        modelname, attribute = item['key'].split('.')
        if modelname=='order':
            model=order
        column = getattr(model, attribute)
        if item['oprator'] == 'bt':
            if item['value'][0] <= column <= item['value'][1]:
                return True
        elif item['oprator'] == 'in':
            if column in item['value']:
                return True
        elif item['oprator'] == 'lte':
            if column<=item['value']:
                return True
        elif item['oprator'] == 'gte':
            if column>=item['value']:
                return True
        return False
    async def validRule(self,rule:Models.ReviewOrderRule,order:Models.Order)->Any:
        items=orjson.loads(rule.items)#type: ignore
        for item in items:
            if item['type']=='normal':
                result=await self.normal(item,order)
            else:
                func=getattr(self,item['type'])
                result=await func(item,order)
            if not result:
                return False
        return True


    async def getRuleList(self)->Any:
        rules=[
            {"name_en":"order amount","name_cn":"订单金额",'options':['bt','lte','gte'],'key':'order.base_grand_total','value':10000,'type':'normal'},
            {"name_en": "full adress", "name_cn": "收货地址包含", 'options': ['contains'],
             'key': '.full_address', 'value': '新疆','type':'normal'},#新疆不发货
        ]

if __name__ == "__main__":
    from common import cmdlineApp
    async def test(db):#type: ignore
        (await LogisticsRuleService()).getRules()
    cmdlineApp(test)()