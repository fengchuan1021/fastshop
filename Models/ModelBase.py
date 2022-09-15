
from common.filterbuilder import filterbuilder
from component.snowFlakeId import snowFlack
from datetime import datetime
from sqlalchemy.orm import deferred
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, String, Text, text, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.ext.declarative import declared_attr
from typing import TYPE_CHECKING
from sqlalchemy.future import select
if TYPE_CHECKING:
    from .User import User
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple

class MyBase(object):

    id = Column(BIGINT(20), primary_key=True,default=snowFlack.getId)
    @declared_attr
    def created_at(self)->Column[DateTime]:
        return Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
        #return deferred(Column(DateTime, server_default=text("CURRENT_TIMESTAMP")))

    @declared_attr
    def updated_at(self)->Column[DateTime]:
        return Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


    def as_dict(self)->Dict[str,Any]:
        return {key:value for key,value in self.__dict__.items() if not key.startswith('_')}#type: ignore


Base = declarative_base(cls=MyBase)