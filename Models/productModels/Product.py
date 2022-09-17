
from sqlalchemy.orm import deferred
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

class Category(Base):
    __tablename__ = 'cagetory'
    caegoryName=Column(VARCHAR(255),nullable=True)