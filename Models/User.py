
from datetime import timedelta,datetime


from jose import jwt

import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from sqlalchemy.sql import and_, or_
from .ModelBase import Base
from UserRole import UserRole
from sqlalchemy import select
class User(Base):
    __tablename__ = 'user'


    username = Column(VARCHAR(32), nullable=False, unique=True)
    email = Column(VARCHAR(32), index=True)
    nickname=Column(VARCHAR(32),default='',server_default=text("''"))
    is_banned=Column(ENUM('normal', 'banned'),default='normal',server_default=text("'normal'"),index=True)
    ban_enddate=Column(DateTime,index=True)
    phone = Column(VARCHAR(16), index=True,server_default=text("''"),default='')
    balance = Column(Float(asdecimal=True), server_default=text("'0'"))
    password = Column(VARCHAR(512), nullable=False)
    gender = Column(ENUM('man', 'woman'))
    userrole = Column(INTEGER(11),nullable=False,default=0,server_default=text("'0'"))
    nickname=Column(VARCHAR(32))
    mark=Column(VARCHAR(512))

    parent_id = Column(BIGINT, ForeignKey('user.id',ondelete='NO ACTION'))
    children:List["User"] = relationship('User',uselist=True, backref=backref('parent', remote_side='User.id'),join_depth=2)
    #pddaccounts=relationship("UserPddAccount")

    @property
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

    @classmethod
    async def getUserByPhoneOrUsername(cls,db: AsyncSession,usernameOrPhone:str)->Optional['User']:
        query=select(cls).filter(or_(cls.username==usernameOrPhone,cls.phone==usernameOrPhone))
        results = await db.execute(query)
        return results.scalar_one_or_none()

    @classmethod
    async def authenticate(cls,dbSession: AsyncSession, username: str, password: str)->Optional['User']:
        user = await cls.getUserByPhoneOrUsername(dbSession,username)
        print('user:',user)
        if not user:
            return None
        print(user.password,password)
        if user.password!=password:
            return None
        return user

    @classmethod
    def create_access_token(cls,data:'User', expires_delta: Union[timedelta, None] = None)->str:
        to_encode = settings.UserTokenData.from_orm(data).dict()
        print(f'{to_encode=}')
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
