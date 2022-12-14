import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE, TIMESTAMP, TEXT

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
class ReviewOrderRule(Base):
    __tablename__ = 'revieworder'
    revieworder_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    merchant_id=Column(INTEGER,index=True)
    priority=Column(INTEGER,default=0)#优先级大的优先执行
    status=Column(XTVARCHAR(32),default='')
    content=Column(TEXT)
