
from datetime import timedelta,datetime


from jose import jwt
from openapi_schema_validator._validators import nullable

import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from sqlalchemy.sql import and_, or_
from .ModelBase import Base
from UserRole import UserRole
from sqlalchemy import select
# class Role(Base):
#     __tablename__ = 'role'
#     id=Column(INTEGER,autoincrement=True,primary_key=True)
#     role_name=Column(VARCHAR(16),server_default='',default='',unique=True)
#     note=Column(VARCHAR(255),server_default='',default='')
# class UserRole(Base):
#     __tablename__ = 'user_role'
#     id = Column(INTEGER, autoincrement=True, primary_key=True)
#     role_id=Column(INTEGER,ForeignKey("role.id"))
#     role_name=Column(VARCHAR(16),server_default='',default='')
#     user_id=Column(BIGINT,ForeignKey("user.id"))
#     role = relationship("Role", back_populates="users")
#     user = relationship("User",back_populates="roles")

class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = (UniqueConstraint('role_id', "api_name", name="roleapi"),)
    id = Column('permission_id',INTEGER, autoincrement=True, primary_key=True)
    role_id=Column(INTEGER,index=True)
    role_name=Column(VARCHAR(32))
    api_name=Column(VARCHAR(255),comment="routes array the role has permission to access. ")

class Roledisplayedmenu(Base):
    __tablename__ = 'roledisplayedmenu'
    __table_args__ = (UniqueConstraint('role_id', "menu_path", name="roledispplayedmenu"),)
    id = Column('roledisplayedmenu_id',INTEGER, autoincrement=True, primary_key=True)
    role_id = Column(INTEGER, index=True)
    role_name = Column(VARCHAR(32))

    menu_path = Column(VARCHAR(32))
