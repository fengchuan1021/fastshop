from sqlalchemy.orm import relationship, backref
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from component.snowFlakeId import snowFlack
import typing
if typing.TYPE_CHECKING:
    from .Product import Product
    from ..store.Store import Store
class Category(Base):
    '产品分类表 以store_id 表示数据哪个店铺的分类'
    __tablename__ = 'category'
    category_id=Column(BIGINT(20), primary_key=True,default=snowFlack.getId)
    category_name=Column(XTVARCHAR(32))
    parent_id = Column(BIGINT,index=True)
    #parent_name = Column(XTVARCHAR(32),server_default='',default='')
    category_order=Column(INTEGER,default=0,server_default='0')

    merchant_id=Column(INTEGER,default=0,index=True)
    description=Column(XTVARCHAR(512))
    #category_image=Column(XTVARCHAR(512),server_default="",default='')
    #use virtual foreign key.

    Children:'Category'=relationship("Category",uselist=True,primaryjoin='foreign(Category.parent_id) == Category.category_id',backref=backref('Parent', remote_side='Category.category_id'),cascade='save-update, delete')
    #Store:'Store'=relationship("Store",uselist=False,primaryjoin='foreign(Category.store_id) == Store.store_id',back_populates="Category",cascade='')
    ProductCategory:typing.List['ProductCategory']=relationship("ProductCategory",uselist=True,primaryjoin='foreign(ProductCategory.category_id) == Category.category_id',back_populates="Category",cascade='')
class ProductCategory(Base):
    '产品和分类的对应关系'
    __tablename__ = 'product_category'
    __table_args__ = (UniqueConstraint('category_id', "product_id", name="categoryproduct"),)
    product_category_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    category_id = Column(BIGINT,index=True)
    product_id=Column(BIGINT,index=True)
    Product:'Product'=relationship("Product",uselist=False,primaryjoin='foreign(ProductCategory.product_id) == Product.product_id',back_populates='ProductCategory',cascade='')
    Category: 'Category' = relationship("Category", uselist=False,
                                      primaryjoin='foreign(ProductCategory.category_id) == Category.category_id',back_populates='ProductCategory',cascade='')
    merchant_id=Column(INTEGER,default=0)
    #store_id=Column(INTEGER,default=0)
