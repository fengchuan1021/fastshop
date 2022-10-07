from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack


class ProductAttribute(Base):
    __tablename__ = 'product_attribute'
    product_attribute_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    product_id = Column(BIGINT,index=True)
    attribute_name_en=Column(VARCHAR(32))
    attribute_name_cn = Column(VARCHAR(32))
    attribute_value_en=Column(VARCHAR(32))
    attribute_value_cn = Column(VARCHAR(32))
    product=relationship('Product',uselist=False,primaryjoin='foreign(Product.product_id) == ProductAttribute.product_id',backref=backref('Attributes'))

