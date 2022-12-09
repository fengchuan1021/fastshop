from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Tuple
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
    usecache = False

    def __init__(self, model: Type[ModelType], usecache: bool = False) -> None:
        self.model = model
        self.usecache = usecache

    def enablecache(self) -> None:
        self.usecache = True

    def disablecache(self) -> None:
        self.usecache = False

    def getpkcachename(self, func, func_args, func_annotations) -> str:  # type: ignore
        # associated listener validredisListerer.py .dont change.
        return f"{cache.get_prefix()}:modelcache:{self.model.__tablename__}:{func_args.arguments.get('id')}"  # type: ignore

    @cache(key_builder='getpkcachename', expire=3600 * 48)  # type: ignore
    async def findByPk(self, dbSession: AsyncSession, id: int, condition: Dict = None) -> Optional[ModelType]:
        if condition:
            w, p = filterbuilder(condition)
            results = await dbSession.execute(select(self.model).where(self.model.id == id).where(text(w)), p)
        else:
            results = await dbSession.execute(select(self.model).where(self.model.id == id))
        return results.scalar_one_or_none()

    async def find(self, db: AsyncSession, filter: Optional[BaseModel | Dict] = None, option: Any = None,
                   offset:int=None,
                   limit:int=None,
                   order_by: Any = '',
                   **kwargs: Dict) -> List[ModelType]:
        where, params = filterbuilder(filter)
        if not option:
            option=[]
        elif not isinstance(option,list):
            option = [option]

        stament = select(self.model).options(*option).where(text(where)).order_by(text(order_by) if isinstance(order_by, str) else order_by)
        if offset!=None:
            stament = stament.offset(offset)
        if limit!=None:
            stament = stament.limit(limit)
        return (await db.execute(stament, params)).scalars().all()

    async def findOne(self, db: AsyncSession, filter: Optional[BaseModel | Dict] = None,option: Any = None) -> Optional[ModelType]:
        results=await self.find(db,filter,option,offset=0,limit=1)
        return results[0] if results else None


    async def create(self, dbSession: AsyncSession, shema_in: BaseModel | Dict) -> ModelType:
        if isinstance(shema_in, dict):
            db_model = self.model(**shema_in)
        else:
            db_model = self.model(**shema_in.dict())
        dbSession.add(db_model)

        return db_model


    async def pagination(self, db: AsyncSession,filter: Optional[BaseModel | Dict] = None ,option:Any=None,pagenum: int = 1, pagesize: int = 20,
                         order_by: str = '', calcTotalNum: bool = False,
                          **kwargs: Dict) -> Tuple[List[ModelType], int]:
        where, params = filterbuilder(filter)

        totalNum=0
        if calcTotalNum:
            totalstatment = select(func.count('*')).select_from(self.model).where(text(where))
            result = await db.execute(totalstatment, params)
            totalNum = result.scalar_one()
        else:
            totalNum = 0

        if not option:
            option=[]
        elif not isinstance(option,list):
            option = [option]

        stament = select(self.model).options(*option).where(text(where))\
            .offset((pagenum - 1) * pagesize).limit(pagesize)\
            .order_by(text(order_by) if isinstance(order_by, str) else order_by)
        results=(await db.execute(stament, params)).scalars().all()
        return results,totalNum

    async def delete(self, dbSession: AsyncSession, model: ModelType) -> None:
        await dbSession.delete(model)

    async def deleteByPk(self, db: AsyncSession, pk: int, condition: Any = None) -> None:
        model = await self.findByPk(db, pk, condition)
        if model:
            await db.delete(model)

    async def updateByPk(self, db: AsyncSession, pk: int, shema_in: BaseModel | Dict) -> None:
        model = await self.findByPk(db, pk)
        if model:
            if not isinstance(shema_in, dict):
                dic = shema_in.dict()
            else:
                dic = shema_in
            for key, value in dic.items():
                setattr(model, key, value)
