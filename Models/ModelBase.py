import orjson
from sqlalchemy.orm import deferred
from sqlalchemy import Column, DateTime,text
import settings
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.declarative import declared_attr

from typing import Any, Dict, List, Optional
from sqlalchemy.ext.hybrid import hybrid_property

import sqlalchemy.types as types
import os
if os.getenv('migratedb',''):
    from sqlalchemy.dialects.mysql import VARCHAR as XTVARCHAR#type: ignore
else:
    class XTVARCHAR(types.TypeDecorator):#type: ignore
        impl = types.String
        cache_ok = True
        def process_bind_param(self, value:str, dialect:Any)->str:#type: ignore
            if settings.AUTO_TRUNCATE_COLUMN:
                return value[:self.impl.length]
            else:
                return value

        def copy(self, **kwargs:Any)->'XTVARCHAR':#type: ignore
            return XTVARCHAR(self.impl.length)#type: ignore


class MyBase(object):

    @hybrid_property
    def id(self):#type: ignore
        return getattr(self,f'{self.__tablename__}_id')
    @declared_attr
    def created_at(self)->Column[DateTime]:
        return Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
        #return deferred(Column(DateTime, server_default=text("CURRENT_TIMESTAMP")))

    @declared_attr
    def updated_at(self)->Column[DateTime]:
        return Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


    def dict(self,resolved:List['MyBase']=[])->Dict[str,Any]:
        dic={}
        if self not in resolved:
            resolved.append(self)
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                continue
            if isinstance(value,Base):
                if value not in resolved:
                    dic[key]=value.dict()
            else:
                dic[key]=value
        return dic
    def json(self)->str:

        return orjson.dumps(self.dict()).decode()

Base = declarative_base(cls=MyBase)