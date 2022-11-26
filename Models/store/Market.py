

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from .Store import Store

class Market(Base):
    __tablename__ = 'market'

    market_id= Column(INTEGER, primary_key=True, autoincrement=True)
    market_name = Column(XTVARCHAR(32),unique=True)
    market_country=Column(XTVARCHAR(32),default='')
    market_url = Column(XTVARCHAR(32), default='')

    Store:typing.List['Store']=relationship("Store",uselist=True,primaryjoin='foreign(Store.market_id) == Market.market_id',back_populates='Market',cascade='')