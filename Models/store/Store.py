

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER,DATETIME,TIMESTAMP
from sqlalchemy.orm import relationship
from Models.stock.Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR

from typing import List,TYPE_CHECKING
if TYPE_CHECKING:
    from Models import Market,VariantStore,Category,Variant,Merchant

class Store(Base):
    __tablename__ = 'store'

    store_id = Column(INTEGER, primary_key=True, autoincrement=True)
    store_name = Column(XTVARCHAR(32))
    appid=Column(XTVARCHAR(512),default='')

    appkey=Column(XTVARCHAR(512),default='')

    appsecret=Column(XTVARCHAR(512),default='')
    token=Column(XTVARCHAR(512),default='')
    refreshtoken=Column(XTVARCHAR(512),default='')
    token_expiration=Column(INTEGER)
    refreshtoken_expiration = Column(INTEGER)
    #lang=Column(ENUM(*[i.value for i in settings.SupportLang]),server_default='en',default='en')
    shop_id=Column(XTVARCHAR(32),default='',server_default='')
    #warehouse_id=Column(BIGINT,index=True)
    #user_id=Column(BIGINT,index=True)
    merchant_id=Column(INTEGER,index=True)
    merchant_name=Column(XTVARCHAR(32),default='',server_default='')
    status=Column(INTEGER,default='1',server_default='1',index=True)#可用为1 token过期 商户未续费等原因为0 不可用
    #warehouse_name=Column(XTVARCHAR(32))
    #Warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Store.warehouse_id) == Warehouse.warehouse_id',back_populates='Store',cascade='')

    market_id=Column(INTEGER,index=True)
    Market:'Market'=relationship("Market",uselist=False,primaryjoin='foreign(Store.market_id) == Market.market_id',back_populates='Store',cascade='')

    # User: 'User' = relationship("User", uselist=False, primaryjoin='foreign(User.user_id) == Shop.user_id',
    #                                 back_populates='Shop')

    Merchant: 'Merchant' = relationship("Merchant", uselist=False, primaryjoin='foreign(Store.merchant_id) == Merchant.merchant_id',
                                    back_populates='Store',cascade='')

    VariantStore:List['VariantStore']= relationship("VariantStore", uselist=True, primaryjoin='foreign(VariantStore.store_id) == Store.store_id',
                                    back_populates='Store',cascade='')
    Category: List['Category']=relationship("Category", uselist=True, primaryjoin='foreign(Category.store_id) == Store.store_id', back_populates='Store',cascade='')
    # Product: List['Product'] = relationship("Product", uselist=True,
    #                                           primaryjoin='foreign(Product.store_id) == Store.store_id',
    #                                           back_populates='Store',cascade='')

    Variant: List['Variant'] = relationship("Variant", uselist=True,
                                              primaryjoin='foreign(Variant.store_id) == Store.store_id',
                                              back_populates='Store',cascade='')
    # Variants: 'VariantSite' = relationship('VariantSite', uselist=True,

    #                                    primaryjoin='foreign(VariantSite.site_id) == Site.site_id',
    #                                    back_populates='Site')
