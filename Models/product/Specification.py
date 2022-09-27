from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack

class PreDefineSpecification(Base):
    __tablename__ = 'predefine_specification'
    name_en =Column(VARCHAR(32),server_default="",default='')
    name_cn=Column(VARCHAR(32),server_default="",default='')

class PreDefineSpecificationValue(Base):
    __tablename__ = 'predefine_specification_value'
    PreDefineSpecification_id=Column(BIGINT,ForeignKey("predefine_specification.id"))

    value_en=Column(VARCHAR(32),server_default="",default='')
    value_cn = Column(VARCHAR(32), server_default="", default='')

class ProductGroupSpecification(Base):
    __tablename__ = 'productgroup_specification'
    specification_id = Column(INTEGER,default=0,server_default="0")
    productgroup_id=Column(INTEGER,)
    specificationname_en=Column(VARCHAR(32))
    specificationname_cn = Column(VARCHAR(32))
    display_order=Column(INTEGER,default=0,server_default="0")