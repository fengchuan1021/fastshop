
from sqlalchemy.orm import deferred, relationship, backref
import enum
from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, TEXT, DECIMAL,DATETIME,BOOLEAN
from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List

class TiktokProduct(Base):
    __tablename__ = 'tiktokproduct'
    tiktokproduct_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    name=Column(XTVARCHAR(128))
    brand_id=Column(XTVARCHAR(32))
    brand_name=Column(XTVARCHAR(32))
    category_ids=Column(XTVARCHAR(512))
    category_names = Column(XTVARCHAR(512))
    market_create_time=Column(DATETIME(fsp=3))
    description=Column(TEXT)
    images=Column(TEXT)
    package_height=Column(INTEGER)
    package_length = Column(INTEGER)
    package_weight = Column(XTVARCHAR(32))
    package_width= Column(INTEGER)


    market_product_id=Column(XTVARCHAR(32),unique=True,index=True)



    market_updated_at=Column(DATETIME(fsp=3))

    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)

    status=Column(INTEGER,default=0)

class TiktokVariant(Base):
    __tablename__ = 'tiktokvariant'
    tiktokvariant_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    tiktokproduct_id=Column(BIGINT,index=True)
    market_product_id = Column(XTVARCHAR(32))
    sku=Column(XTVARCHAR(80))
    price=Column(DECIMAL(10,4))
    currency_code=Column(XTVARCHAR(12))
    market_varant_id=Column(XTVARCHAR(32),unique=True,index=True)
    #tiktok_id=Column(XTVARCHAR(32),unique=True,index=True)
    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)

