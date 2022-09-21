
from sqlalchemy.orm import deferred, relationship
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack


class ProductDynamic(Base):
    __tablename__ = 'product_dynamic'
    id = Column(BIGINT(20), ForeignKey('product_static.id'),default=snowFlack.getId,primary_key=True)
    is_hot=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    is_recommend=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    collect_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    sale_cnt=Column(INTEGER,server_default="0",default="0",index=True)

    #parent_id = Column(BIGINT, ForeignKey('product_static.id'))
class ProductStatic(Base):
    __tablename__ = 'product_static'
    price=Column(INTEGER)

    productName_en= deferred(Column(VARCHAR(255),nullable=True), group='en')
    productDescription_en=deferred(Column(TEXT(),nullable=True), group='en')
    brand_en=deferred(Column(VARCHAR(24),nullable=True), group='en')

    productName_cn= deferred(Column(VARCHAR(255),nullable=True), group='cn')
    productDescription_cn=deferred(Column(TEXT(),nullable=True), group='cn')
    brand_cn=deferred(Column(VARCHAR(24),nullable=True), group='cn')

    dynamic:"ProductDynamic" = relationship(ProductDynamic, uselist=False, backref="product_static")




class Category(Base):
    __tablename__ = 'cagetory'
    caegoryName=Column(VARCHAR(255),nullable=True)