import abc
from typing import Tuple, Dict, List, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

import Models
import Service
from Service.thirdpartmarket.Shema import Shipinfo
from common.CommonError import ResponseException
from component.fastQL import fastQuery


class Market:
    market_id:int
    market_name:str
    @abc.abstractmethod
    async def getProductList(self,db:AsyncSession,store:Models.Store)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def getProductDetail(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        raise NotImplementedError
    @abc.abstractmethod
    async def deleteProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        raise NotImplementedError
    @abc.abstractmethod
    async def offlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def onlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def updatePrice(self, db: AsyncSession, store: Models.Store, sku: str, price: float) -> Any:
        raise NotImplementedError
    @abc.abstractmethod
    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def shiPackage(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo,order:Models.Order,ordershipmentitems:List[Models.OrderShipmentItem])->Any:
        raise NotImplementedError

    @abc.abstractmethod
    async def updateStock(self,db:AsyncSession,store:Models.Store,sku:str,num:int)->Any:
        raise NotImplementedError







    @abc.abstractmethod
    async def getOrderDetail(self, db: AsyncSession, store:Models.Store,market_order_id:str)->Any:
        raise NotImplementedError