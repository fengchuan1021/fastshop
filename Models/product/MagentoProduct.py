
from sqlalchemy.orm import deferred, relationship, backref
import enum
from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, TEXT, DECIMAL,DATETIME,BOOLEAN
from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List

class MagentoProduct(Base):
    __tablename__ = 'magentoproduct'

    magentoproduct_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    magento_id=Column(XTVARCHAR(32),unique=True,index=True)
    sku=Column(XTVARCHAR(80),index=True)
    name = Column(XTVARCHAR(128))
    price=Column(DECIMAL(10,4),default=0)
    status=Column(INTEGER)
    visibility=Column(INTEGER)
    market_created_at=Column(DATETIME)
    market_updated_at=Column(DATETIME)
    description=Column(TEXT)
    url_key=Column(XTVARCHAR(255))
    main_image=Column(XTVARCHAR(512))
    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)
