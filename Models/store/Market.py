

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from .Shop import Shop

class Market(Base):
    __tablename__ = 'market'

    market_id= Column(INTEGER, primary_key=True, autoincrement=True)
    market_name = Column(XTVARCHAR(32),unique=True)
    market_country=Column(XTVARCHAR(32),default='')
    market_url = Column(XTVARCHAR(32), default='')

    Shop:typing.List['Shop']=relationship("Shop",uselist=True,primaryjoin='foreign(Market.market_id) == Shop.market_id',back_populates='Market')