

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from .Market import Market
    from ..User import User
    from Models import VariantShop

class Shop(Base):
    __tablename__ = 'shop'

    shop_id = Column(INTEGER, primary_key=True, autoincrement=True)
    shop_name = Column(XTVARCHAR(32),unique=True)
    appid=Column(XTVARCHAR(512),default='')

    appkey=Column(XTVARCHAR(512),default='')
    appsecret=Column(XTVARCHAR(512),default='')
    token=Column(XTVARCHAR(512),default='')
    lang=Column(ENUM(*[i.value for i in settings.SupportLang]),server_default='en',default='en')
    warehouse_id=Column(BIGINT,index=True)
    user_id=Column(BIGINT,index=True)
    warehouse_name=Column(XTVARCHAR(32))
    warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Shop.warehouse_id',backref=backref('Shop'))

    market_id=Column(INTEGER,index=True)
    Market:'Market'=relationship("Market",uselist=False,primaryjoin='foreign(Market.market_id) == Shop.market_id',backref=backref('Shop'))

    User: 'User' = relationship("User", uselist=False, primaryjoin='foreign(User.user_id) == Shop.user_id',
                                    backref=backref('Shop'))
    VariantShop:'VariantShop'= relationship("VariantShop", uselist=True, primaryjoin='foreign(VariantShop.shop_id) == Shop.shop_id',
                                    backref=backref('Shop'))
    # Variants: 'VariantSite' = relationship('VariantSite', uselist=True,

    #                                    primaryjoin='foreign(VariantSite.site_id) == Site.site_id',
    #                                    backref=backref('Site'))
