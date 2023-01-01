import settings
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER,DATETIME,TIMESTAMP
from sqlalchemy.orm import relationship
from Models.stock.Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR

from typing import List,TYPE_CHECKING

from component.snowFlakeId import snowFlack


class StoreWarehouse(Base):
    __tablename__ = 'store_warehouse'
    __table_args__ = (UniqueConstraint('store_id', "warehouse_id", name="storewarehouse"),)
    store_warehouse_id = Column(INTEGER, primary_key=True, autoincrement=True)
    store_id=Column(INTEGER)
    warehouse_id=Column(BIGINT)
    merchant_id=Column(INTEGER,index=True)
class variant_store_warehouse(Base):
    __tablename__ = 'variant_store_warehouse'
    __table_args__ = (UniqueConstraint('variant_id','store_id', "warehouse_id", name="storewarehouse"),)
    variant_store_warehouse_id=Column(BIGINT, primary_key=True, default=snowFlack.getId, comment="primary key")
    variant_id=Column(BIGINT)
    store_id=Column(INTEGER)
    warehouse_id=Column(BIGINT)
    merchant_id = Column(INTEGER, index=True)
    qty=Column(INTEGER,default=0)