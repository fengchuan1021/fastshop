import typing

from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT,DECIMAL
import enum
if typing.TYPE_CHECKING:
    from .Product import Product
from XTTOOLS import snowFlack


class PreAttrSpecification(Base):
    __tablename__ = 'preattrspecific'
    preattrspecific_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    name_en =Column(XTVARCHAR(32),server_default="",default='')
    name_cn=Column(XTVARCHAR(32),server_default="",default='')
    value_en=Column(TEXT,default='')
    value_cn = Column(TEXT, default='')
    type=Column(ENUM('specification','attribute'),index=True)
    singlefield=Column(INTEGER,default=1,server_default="1")


class ProductAttribute(Base):
    __tablename__ = 'product_attribute'
    product_attribute_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    preattrspecific_id=Column(BIGINT(20),default=0,index=True,server_default='0')
    product_id = Column(BIGINT,index=True)
    attributename_en=Column(XTVARCHAR(32))
    attributename_cn = Column(XTVARCHAR(32))
    attributevalue_en=Column(XTVARCHAR(32))
    attributevalue_cn = Column(XTVARCHAR(32))
    display_order = Column(INTEGER, default=0, server_default="0")
    product:'Product'=relationship('Product',uselist=False,primaryjoin='foreign(Product.product_id) == ProductAttribute.product_id',backref=backref('Attributes'))

class ProductSpecification(Base):
    __tablename__ = 'product_specification'
    product_specification_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    preattrspecific_id=Column(BIGINT(20),default=0,index=True,server_default='0')
    product_id=Column(BIGINT,index=True)
    specificationname_en=Column(XTVARCHAR(32))
    specificationname_cn = Column(XTVARCHAR(32))
    specificationvalue_en=Column(XTVARCHAR(32))
    specificationvalue_cn = Column(XTVARCHAR(32))
    display_order=Column(INTEGER,default=0,server_default="0")
    product:'Product' = relationship('Product', uselist=False,
                           primaryjoin='foreign(Product.product_id) == ProductSpecification.product_id',
                           backref=backref('Specifications'))