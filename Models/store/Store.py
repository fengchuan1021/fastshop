

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR

from typing import List,TYPE_CHECKING
if TYPE_CHECKING:
    from .Market import Market
    from ..User import User
    from ..product.VariantStore import VariantStore
    from .Merchant import Merchant
    from ..product.Category import Category
    from ..product.Product import Product,Variant
class Store(Base):
    __tablename__ = 'store'

    store_id = Column(INTEGER, primary_key=True, autoincrement=True)
    store_name = Column(XTVARCHAR(32),unique=True)
    appid=Column(XTVARCHAR(512),default='')

    appkey=Column(XTVARCHAR(512),default='')
    appsecret=Column(XTVARCHAR(512),default='')
    token=Column(XTVARCHAR(512),default='')
    lang=Column(ENUM(*[i.value for i in settings.SupportLang]),server_default='en',default='en')
    warehouse_id=Column(BIGINT,index=True)
    #user_id=Column(BIGINT,index=True)
    merchant_id=Column(INTEGER,index=True)
    warehouse_name=Column(XTVARCHAR(32))
    Warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Store.warehouse_id',back_populates='Store')

    market_id=Column(INTEGER,index=True)
    Market:'Market'=relationship("Market",uselist=False,primaryjoin='foreign(Market.market_id) == Store.market_id',back_populates='Store')

    # User: 'User' = relationship("User", uselist=False, primaryjoin='foreign(User.user_id) == Shop.user_id',
    #                                 back_populates='Shop')

    Merchant: 'Merchant' = relationship("Merchant", uselist=False, primaryjoin='foreign(Merchant.merchant_id) == Store.merchant_id',
                                    back_populates='Store')

    VariantStore:List['VariantStore']= relationship("VariantStore", uselist=True, primaryjoin='foreign(VariantStore.store_id) == Store.store_id',
                                    back_populates='Store')
    Category: List['Category']=relationship("Category", uselist=True, primaryjoin='foreign(Store.store_id) == Category.store_id', back_populates='Store')
    Product: List['Product'] = relationship("Product", uselist=True,
                                              primaryjoin='foreign(Store.store_id) == Product.store_id',
                                              back_populates='Store')

    Variant: List['Variant'] = relationship("Variant", uselist=True,
                                              primaryjoin='foreign(Store.store_id) == Variant.store_id',
                                              back_populates='Store')
    # Variants: 'VariantSite' = relationship('VariantSite', uselist=True,

    #                                    primaryjoin='foreign(VariantSite.site_id) == Site.site_id',
    #                                    back_populates='Site')
