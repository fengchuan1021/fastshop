
from sqlalchemy.orm import deferred, relationship
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .ProductImage import ProductImage

class ProductDynamic(Base):
    __tablename__ = 'product_dynamic'

    is_hot=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    is_recommend=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    collect_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    sale_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    price=Column(INTEGER,server_default="0")
    min_price=Column(INTEGER,server_default="0")
    max_price=Column(INTEGER,server_default="0")
    qty=Column(INTEGER,server_default="0")

class ProductStatic(Base):
    __tablename__ = 'product_static'

    sku=Column(VARCHAR(512))
    barcode=Column(VARCHAR(32))
    hscode=Column(VARCHAR(32))
    group_id=Column(BIGINT,server_default="0")
    productName_en= deferred(Column(VARCHAR(255),nullable=True), group='en')
    productDescription_en=deferred(Column(TEXT(),nullable=True), group='en')
    brand_en=deferred(Column(VARCHAR(24),nullable=True), group='en')

    productName_cn= deferred(Column(VARCHAR(255),nullable=True), group='cn')
    productDescription_cn=deferred(Column(TEXT(),nullable=True), group='cn')
    brand_cn=deferred(Column(VARCHAR(24),nullable=True), group='cn')

    #dynamic:"ProductDynamic" = relationship(ProductDynamic, uselist=False, backref="product_static")
    images:List[ProductImage] = relationship('ProductImage', backref='Product',uselist=True)


