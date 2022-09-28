
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from Models import Base
from sqlalchemy.future import select
from sqlalchemy import text, func
from common.filterbuilder import filterbuilder
ModelType = TypeVar("ModelType", bound=Base)
from sqlalchemy.orm import defer
import Models
from component.cache import cache

class CRUDBase(Generic[ModelType]):
    usecache=True

    def __init__(self, model: Type[ModelType],usecache:bool=True)->None:
        self.model = model
        self.usecache = usecache

    def enablecache(self)->None:
        self.usecache=True

    def disablecache(self)->None:
        self.usecache=False

    def getpkcachename(self,func,funcsig,func_args)->str:#type: ignore
        # associated listener validredisListerer.py .dont change.
        return f"{cache.get_prefix()}:modelcache:{self.model.__tablename__}:{func_args.arguments.get('id')}"#type: ignore

    @cache(key_builder='getpkcachename',expire=3600*48)
    async def findByPk(self,dbSession: AsyncSession,id: int) -> Optional[ModelType]:
        results=await dbSession.execute(select(self.model).where(self.model.id==id))
        return results.scalar_one_or_none()

    async def create(self,dbSession: AsyncSession,shema_in:BaseModel) -> ModelType:
        db_model = self.model(**shema_in.dict())
        dbSession.add(db_model)
        return db_model

    async def getList(self,dbSession: AsyncSession,offset:int=0,limit:int=0,filter:list=[],order_by:str='')->List[ModelType]:

        #filter.append(Models.User.is_deleted==0)
        stament=select(self.model).filter(*filter).order_by(text(order_by))
        if offset:
            stament=stament.offset(offset)
        if limit:
            stament=stament.limit(limit)
        results=await dbSession.execute(stament)

        return results.scalars().all()

    async def pagination(self,dbSession: AsyncSession,pageNum:int=1,pageSize:int=20,filter:list=[],order_by:str='',calcTotalNum:bool=True,options:list=[])->Tuple[List[ModelType],int]:

        if calcTotalNum:
            totalstatment=select(func.count('*')).select_from(self.model).where(text(filterbuilder(filter)))
            result=await dbSession.execute(totalstatment)
            totalNum=result.scalar_one()
        else:
            totalNum = 0

        stament=select(self.model).options(*options).where(text(filterbuilder(filter))).limit(pageSize).offset((pageNum-1)*pageSize).order_by(text(order_by))
        results=await dbSession.execute(stament)
        return results.scalars().all(),totalNum


    async def delete(self,dbSession: AsyncSession, model:ModelType)->None:
        await dbSession.delete(model)

