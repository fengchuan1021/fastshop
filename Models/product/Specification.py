from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack


class ProductGroupSpecification(Base):
    __tablename__ = 'productgroup_specification'
    specification_id = Column(INTEGER,default=0,server_default="0")
    productgroup_id=Column(INTEGER,)
    specificationname_en=Column(VARCHAR(32))
    specificationname_cn = Column(VARCHAR(32))
    display_order=Column(INTEGER,default=0,server_default="0")
