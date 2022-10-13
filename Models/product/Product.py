from sqlalchemy.orm import deferred, relationship


from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR, TEXT, DECIMAL

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List

class Product(Base):
    __tablename__ = 'product'
    product_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    sku = Column(XTVARCHAR(80))
    brand_id =Column(INTEGER,index=True,server_default='0',default=0)
    name_en= deferred(Column(XTVARCHAR(255),nullable=False,default='',server_default=''), group='en')
    description_en=deferred(Column(TEXT(),nullable=False,default='',server_default=''), group='en')
    brand_en=deferred(Column(XTVARCHAR(24),nullable=False,default='',server_default=''), group='en')

    name_cn= deferred(Column(XTVARCHAR(255),nullable=False,default='',server_default=''), group='cn')
    description_cn=deferred(Column(TEXT(),nullable=False,default='',server_default=''), group='cn')
    brand_cn=deferred(Column(XTVARCHAR(24),nullable=False,default='',server_default=''), group='cn')
    status=Column(ENUM("ONLINE","OFFLINE","EDITING"),server_default="OFFLINE",default='EDITING')
    image=Column(XTVARCHAR(512),nullable=True,comment="product image.when any of variants are not chosed.can set as same as the defualt variant's fisrt image.")
    video=Column(XTVARCHAR(512),nullable=True)
    price=Column(DECIMAL(10,2))


class VariantDynamic(Base):
    __tablename__ = 'variant_dynamic'
    variant_dynamic_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    is_hot=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    is_recommend=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    collect_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    sale_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    price=Column(INTEGER,server_default="0")
    min_price=Column(INTEGER,server_default="0")
    max_price=Column(INTEGER,server_default="0")
    stock=Column(INTEGER,server_default="0")
    status = Column(ENUM("ONLINE", "OFFLINE","EDITING"), server_default="OFFLINE", default='EDITING')
class VariantStatic(Base):
    __tablename__ = 'variant_static'
    variant_static_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    sku=Column(XTVARCHAR(80))
    barcode=Column(XTVARCHAR(32))
    hscode=Column(XTVARCHAR(32))
    group_id=Column(BIGINT,server_default="0")

    specification_en=Column(XTVARCHAR(12),server_default='')
    specification_cn = Column(XTVARCHAR(12), server_default='')

    name_en= deferred(Column(XTVARCHAR(255),nullable=True), group='en')
    description_en=deferred(Column(TEXT(),nullable=True), group='en')
    brand_en=deferred(Column(XTVARCHAR(24),nullable=True), group='en')

    name_cn= deferred(Column(XTVARCHAR(255),nullable=True), group='cn')
    description_cn=deferred(Column(TEXT(),nullable=True), group='cn')
    brand_cn=deferred(Column(XTVARCHAR(24),nullable=True), group='cn')

    #dynamic:"ProductDynamic" = relationship(ProductDynamic, uselist=False, backref="product_static")
    #images:List[ProductImage] = relationship('ProductImage', backref='Product',uselist=True)


