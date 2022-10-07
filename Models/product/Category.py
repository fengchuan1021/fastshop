from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column,text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT,DECIMAL
from typing import List
from component.snowFlakeId import snowFlack

class Category(Base):
    __tablename__ = 'category'
    category_id=Column(BIGINT(20), primary_key=True,default=snowFlack.getId)
    category_name=Column(VARCHAR(32))
    parent_id = Column(BIGINT,index=True)
    parent_name = Column(VARCHAR(32),server_default='',default='')
    category_order=Column(INTEGER,default=0,server_default='0')
    shop_id=Column(INTEGER,server_default="0")
    description=Column(VARCHAR(512))
    category_image=Column(VARCHAR(512),server_default="",default='')
    #use virtual foreign key.
    children=relationship("Category",uselist=True,primaryjoin='foreign(Category.parent_id) == Category.category_id',backref=backref('parent', remote_side='Category.category_id'))


class ProductCategory(Base):
    __tablename__ = 'product_category'
    product_category_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    category_id = Column(INTEGER,)
    product_id=Column(INTEGER,)