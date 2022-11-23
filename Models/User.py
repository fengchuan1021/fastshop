from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL
from sqlalchemy.orm import relationship, backref

from typing import List
from .ModelBase import Base,XTVARCHAR

import typing
if typing.TYPE_CHECKING:
    from .store.Store import Store
    from .store.Merchant import Merchant
    from .store.Warehouse import Warehouse
    from .Permission import UserRole
class User(Base):
    __tablename__ = 'user'

    user_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    username = Column(XTVARCHAR(32), nullable=True, unique=True)
    email = Column(XTVARCHAR(32),nullable=True,unique=True)
    nickname=Column(XTVARCHAR(32),default='',server_default=text("''"))
    #is_banned=Column(ENUM('normal', 'banned'),default='normal',server_default=text("'normal'"),index=True)
    #ban_enddate=Column(DateTime,index=True)
    phone = Column(XTVARCHAR(16), nullable=True,unique=True)
    balance = Column(DECIMAL(10,2), server_default=text("'0'"))
    password = Column(XTVARCHAR(512), nullable=False)
    gender = Column(ENUM('man', 'woman'))
    #userrole = Column(INTEGER(11),nullable=False,default=0,server_default=text("'0'"))

    mark=Column(XTVARCHAR(512))

    #parent_id = Column(BIGINT,index=True)
    #children:List["User"] = relationship('User',uselist=True, primaryjoin='foreign(User.parent_id) == User.user_id',backref=backref('parent', remote_side='User.user_id'))

    Merchant:'Merchant'=relationship('Merchant',uselist=False,primaryjoin='foreign(User.user_id)==Merchant.user_id',back_populates='User',viewonly=True)
    # Store: 'Store' = relationship('Store', uselist=True,
    #                                     primaryjoin='foreign(User.user_id)==Store.user_id', back_populates='User')
    Warehouse: 'Warehouse' = relationship('Warehouse', uselist=False,
                                        primaryjoin='foreign(User.user_id)==Warehouse.user_id', back_populates='User',viewonly=True)

    UserRole: List['UserRole'] = relationship("UserRole", back_populates="User", primaryjoin="foreign(User.user_id)==UserRole.user_id",viewonly=True)

    # def is_admin(self)->int:
    #     if not self.userrole:
    #         self.userrole =0
    #     return self.userrole & UserRole.admin.value
    #
    # def set_admin(self, value:bool)->None:
    #     if not self.userrole:
    #         self.userrole = 0
    #     if value:
    #         self.userrole = self.userrole | UserRole.admin.value
    #     else:
    #         self.userrole=self.userrole & (UserRole.admin.value-1)