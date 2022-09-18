
from sqlalchemy.orm import deferred, relationship
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT
class Product(Base):
    __tablename__ = 'product'
    price=Column(INTEGER)

    productName_en= deferred(Column(VARCHAR(255),nullable=True), group='en')
    productDescription_en=deferred(Column(TEXT(),nullable=True), group='en')
    brand_en=deferred(Column(VARCHAR(24),nullable=True), group='en')

    productName_cn= deferred(Column(VARCHAR(255),nullable=True), group='cn')
    productDescription_cn=deferred(Column(TEXT(),nullable=True), group='cn')
    brand_cn=deferred(Column(VARCHAR(24),nullable=True), group='cn')

    dynamic:"Product_dynamic" = relationship("Product_dynamic", uselist=False, backref="product")

class Product_dynamic(Base):
    __tablename__ = 'product_dynamic'
    is_hot=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    is_recommend=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
    collect_cnt=Column(INTEGER,server_default="0",default="0",index=True)
    sale_cnt=Column(INTEGER,server_default="0",default="0",index=True)

    parent_id = Column(BIGINT, ForeignKey('product.id'))


class Category(Base):
    __tablename__ = 'cagetory'
    caegoryName=Column(VARCHAR(255),nullable=True)