from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack


class ProductAttribute(Base):
    __tablename__ = 'product_attribute'
    product_id = Column(BIGINT,ForeignKey("product.id"))
    attribute_name_en=Column(VARCHAR(32))
    attribute_name_cn = Column(VARCHAR(32))
    attribute_value_en=Column(VARCHAR(32))
    attribute_value_cn = Column(VARCHAR(32))

