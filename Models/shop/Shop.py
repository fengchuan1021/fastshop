
import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from ..ModelBase import Base,XTVARCHAR

class Shop(Base):
    __tablename__ = 'shop'

    shop_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    shop_name = Column(XTVARCHAR(32),unique=True)
    domainname=Column(XTVARCHAR(64),unique=True,index=True)
    company_name = Column(XTVARCHAR(32),nullable=True)
    company_id=Column(BIGINT,nullable=True)
    warehouse_id=Column(BIGINT,index=True)
    warehouse_name=Column(XTVARCHAR(32))
    warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Shop.warehouse_id',backref=backref('shops'))
