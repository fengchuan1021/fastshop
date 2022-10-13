from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text, Index, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from .ModelBase import Base,XTVARCHAR

# class Role(Base):
#     __tablename__ = 'role'
#     id=Column(INTEGER,autoincrement=True,primary_key=True)
#     role_name=Column(XTVARCHAR(16),server_default='',default='',unique=True)
#     note=Column(XTVARCHAR(255),server_default='',default='')
# class UserRole(Base):
#     __tablename__ = 'user_role'
#     id = Column(INTEGER, autoincrement=True, primary_key=True)
#     role_id=Column(INTEGER,ForeignKey("role.id"))
#     role_name=Column(XTVARCHAR(16),server_default='',default='')
#     user_id=Column(BIGINT,ForeignKey("user.id"))
#     role = relationship("Role", back_populates="users")
#     user = relationship("User",back_populates="roles")

class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = (UniqueConstraint('role_id', "api_name", name="roleapi"),)
    permission_id = Column(INTEGER, autoincrement=True, primary_key=True)
    role_id=Column(INTEGER,index=True)
    role_name=Column(XTVARCHAR(32))
    api_name=Column(XTVARCHAR(255),comment="routes array the role has permission to access. ")

class Roledisplayedmenu(Base):
    __tablename__ = 'roledisplayedmenu'
    __table_args__ = (UniqueConstraint('role_id', "menu_path", name="roledispplayedmenu"),)
    roledisplayedmenu_id = Column(INTEGER, autoincrement=True, primary_key=True)
    role_id = Column(INTEGER, index=True)
    role_name = Column(XTVARCHAR(32))

    menu_path = Column(XTVARCHAR(32))
