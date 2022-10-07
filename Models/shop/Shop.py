
import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref

from ..ModelBase import Base

class Shop(Base):
    __tablename__ = 'shop'

    shop_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    shop_name = Column(VARCHAR(32),unique=True)
    company_name = Column(VARCHAR(32),nullable=True)
    company_id=Column(BIGINT,nullable=True)
    warehouse_id=Column(BIGINT,index=True)
    warehouse_name=Column(VARCHAR(32))
    Warehouse=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Shop.warehouse_id',backref=backref('shops'))
