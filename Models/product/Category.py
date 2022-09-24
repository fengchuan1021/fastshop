from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT
from typing import List
from component.snowFlakeId import snowFlack

class Category(Base):
    __tablename__ = 'cagetory'
    caegoryName=Column(VARCHAR(255),nullable=True)
    parent_id = Column(BIGINT, ForeignKey('cagetory.id', ondelete='NO ACTION'))
    #children: List["Category"] = relationship('Category', uselist=True, backref=backref('parent', remote_side='Category.id'),join_depth=2)
    catory_order=Column(INTEGER)
    shop_id=Column(INTEGER,server_default="0")
    description=Column(VARCHAR(512))
    image=Column(VARCHAR(512),server_default="",default='')
    name=Column(VARCHAR(32))

class ProductCategory(Base):
    __tablename__ = 'product_cagetory'
    category_id = Column(INTEGER,)
    product_id=Column(INTEGER,)