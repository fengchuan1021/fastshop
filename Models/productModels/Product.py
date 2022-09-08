from openapi_schema_validator._validators import nullable

from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR
class Product(Base):
    __tablename__ = 'product'
    productName=Column(VARCHAR(256),nullable=True)

class Category(Base):
    __tablename__ = 'cagetory'
    caegoryName=Column(VARCHAR(255),nullable=True)