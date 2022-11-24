
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from Models import Base
from sqlalchemy.future import select
from sqlalchemy import text, func
from common import filterbuilder
ModelType = TypeVar("ModelType", bound=Base)
from sqlalchemy.orm import defer
import Models
from component.cache import cache

class CRUDBase(Generic[ModelType]):
    usecache=False

    def __init__(self, model: Type[ModelType],usecache:bool=False)->None:
        self.model = model
        self.usecache = usecache

    def enablecache(self)->None:
        self.usecache=True

    def disablecache(self)->None:
        self.usecache=False

    def getpkcachename(self,func,func_args,func_annotations)->str:#type: ignore
        # associated listener validredisListerer.py .dont change.
        return f"{cache.get_prefix()}:modelcache:{self.model.__tablename__}:{func_args.arguments.get('id')}"#type: ignore

    @cache(key_builder='getpkcachename',expire=3600*48)#type: ignore
    async def findByPk(self,dbSession: AsyncSession,id: int) -> Optional[ModelType]:
        results=await dbSession.execute(select(self.model).where(self.model.id==id))
        return results.scalar_one_or_none()
    async def findOne(self,dbSession: AsyncSession,filter:BaseModel | Dict={})->Optional[ModelType]:
        where, params = filterbuilder(filter)
        txtwhere=text(where)
        statment=select(self.model).where(txtwhere)
        results = await dbSession.execute(statment,params)
        return results.scalar_one_or_none()

    async def create(self,dbSession: AsyncSession,shema_in:BaseModel|Dict) -> ModelType:
        if isinstance(shema_in,dict):

            db_model = self.model(**shema_in)
        else:
            print('what??', shema_in)
            print('what?',shema_in.dict())
            db_model = self.model(**shema_in.dict())
        dbSession.add(db_model)

        return db_model

    async def getList(self,dbSession: AsyncSession,offset:int=0,limit:int=0,filter:BaseModel | Dict={},order_by:Any='',options:list=[],**kwargs:Dict)->List[ModelType]:
        if not order_by:
             order_by=self.model.id.desc()
        where,params=filterbuilder(filter)
        txtwhere = text(where)
        stament=select(self.model).options(*options).where(txtwhere).order_by(text(order_by) if isinstance(order_by,str) else order_by)
        if offset:
            stament=stament.offset(offset)
        if limit:
            stament=stament.limit(limit)
        results=await dbSession.execute(stament,params)

        return results.scalars().all()

    async def pagination(self,dbSession: AsyncSession,pagenum:int=1,pagesize:int=20,filter:BaseModel | Dict={},order_by:str='',calcTotalNum:bool=False,options:list=[],**kwargs:Dict)->Tuple[List[ModelType],int]:
        where,params=filterbuilder(filter)
        txtwhere=text(where)
        if not order_by:
            txtorderby=text(f"{self.model.__tablename__}.{self.model.__tablename__}_id desc")#type: ignore
        else:
            txtorderby = text(order_by)
        if calcTotalNum:
            totalstatment=select(func.count('*')).select_from(self.model).where(txtwhere)
            result=await dbSession.execute(totalstatment,params)
            totalNum=result.scalar_one()
        else:
            totalNum = 0

        stament=select(self.model).options(*options).where(txtwhere).offset((pagenum-1)*pagesize).limit(pagesize).order_by(txtorderby)
        results=await dbSession.execute(stament,params)
        return results.scalars().all(),totalNum


    async def delete(self,dbSession: AsyncSession, model:ModelType)->None:
        await dbSession.delete(model)

    async def deleteByPk(self,db: AsyncSession,pk:int)->None:
        model=await self.findByPk(db,pk)
        if model:
            await db.delete(model)

    async def updateByPk(self,db:AsyncSession,pk:int|str,shema_in:BaseModel | Dict)->None:
        model=await self.findByPk(db,pk)
        if model:
            if not isinstance(shema_in, dict):
                dic=shema_in.dict()
            else:
                dic=shema_in
            for key,value in dic.items():
                setattr(model,key,value)

