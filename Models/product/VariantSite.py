
from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT,DECIMAL

from XTTOOLS import snowFlack
from .Product import Variant
class VariantSite(Base):
    __tablename__ = 'variant_site'
    variant_site_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    variant_id=Column(BIGINT(20),index=True)
    product_id=Column(BIGINT(20),index=True)
    site_id=Column(INTEGER,index=True)
    site_name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10,2))
    qty=Column(INTEGER)
    status = Column(ENUM("ONLINE", "OFFLINE"), server_default="OFFLINE", default="OFFLINE")
    warehouse_id=Column(BIGINT(20), index=True)
    warehouse_name = Column(XTVARCHAR(32))