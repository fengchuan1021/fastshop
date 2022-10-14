from openapi_schema_validator._validators import nullable

import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from ..ModelBase import Base,XTVARCHAR

class Site(Base):
    __tablename__ = 'site'

    site_id = Column(INTEGER, primary_key=True, autoincrement=True)
    site_name = Column(XTVARCHAR(32),unique=True)
    domainname=Column(XTVARCHAR(64),unique=True,index=True)

    warehouse_id=Column(BIGINT,index=True)
    warehouse_name=Column(XTVARCHAR(32))
    warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Site.warehouse_id',backref=backref('sites'))
