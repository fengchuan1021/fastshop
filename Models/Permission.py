from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import INTEGER, BIGINT
from sqlalchemy.orm import relationship, foreign

from .ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from .User import User
class Role(Base):
    __tablename__ = 'role'
    role_id=Column(INTEGER,autoincrement=True,primary_key=True)
    role_name=Column(XTVARCHAR(16),server_default='',default='',unique=True)
    note=Column(XTVARCHAR(255),server_default='',default='')
    UserRole: typing.List['UserRole']=relationship("UserRole", back_populates='Role', primaryjoin='foreign(Role.role_id)==UserRole.role_id')
class UserRole(Base):
    __tablename__ = 'user_role'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    role_id=Column(INTEGER,index=True)
    role_name=Column(XTVARCHAR(16),server_default='',default='')
    user_id=Column(BIGINT,index=True)
    Role:'Role'= relationship("Role", back_populates="UserRole",primaryjoin=foreign(Role.role_id)==role_id)
    User:'User' = relationship("User",back_populates="UserRole",primaryjoin="foreign(User.user_id)==UserRole.user_id")

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
