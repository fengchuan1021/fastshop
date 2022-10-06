
from datetime import timedelta,datetime


from jose import jwt

import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from sqlalchemy.sql import and_, or_
from .ModelBase import Base
from UserRole import UserRole
from sqlalchemy import select
class User(Base):
    __tablename__ = 'user'


    username = Column(VARCHAR(32), nullable=True, unique=True)
    email = Column(VARCHAR(32),nullable=True,unique=True)
    nickname=Column(VARCHAR(32),default='',server_default=text("''"))
    #is_banned=Column(ENUM('normal', 'banned'),default='normal',server_default=text("'normal'"),index=True)
    #ban_enddate=Column(DateTime,index=True)
    phone = Column(VARCHAR(16), nullable=True,unique=True)
    balance = Column(DECIMAL(10,2), server_default=text("'0'"))
    password = Column(VARCHAR(512), nullable=False)
    gender = Column(ENUM('man', 'woman'))
    userrole = Column(INTEGER(11),nullable=False,default=0,server_default=text("'0'"))

    mark=Column(VARCHAR(512))

    parent_id = Column(BIGINT, ForeignKey('user.user_id',ondelete='NO ACTION'))
    children:List["User"] = relationship('User',uselist=True, backref=backref('parent', remote_side='User.id'),join_depth=2)



    def is_admin(self)->int:
        if not self.userrole:
            self.userrole =0
        return self.userrole & UserRole.admin.value

    def set_admin(self, value:bool)->None:
        if not self.userrole:
            self.userrole = 0
        if value:
            self.userrole = self.userrole | UserRole.admin.value
        else:
            self.userrole=self.userrole & (UserRole.admin.value-1)