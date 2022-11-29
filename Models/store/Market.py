from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from Models.ModelBase import Base, XTVARCHAR
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Models import Store


class Market(Base):
    __tablename__ = 'market'

    market_id = Column(INTEGER, primary_key=True, autoincrement=True)
    market_name = Column(XTVARCHAR(32), unique=True)
    market_country = Column(XTVARCHAR(32), default='')
    market_url = Column(XTVARCHAR(32), default='')

    Store: List['Store'] = relationship("Store", uselist=True,
                                               primaryjoin='foreign(Store.market_id) == Market.market_id',
                                               back_populates='Market', cascade='')
