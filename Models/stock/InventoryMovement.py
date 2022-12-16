
import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE, TIMESTAMP, TEXT

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import Warehouse
class InventoryMovement(Base):
    __tablename__ = 'inventorymovement'
    inventorymovement_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    warehouse_id=Column(BIGINT(20), index=True)
    number=Column(INTEGER,default=0,server_default="0")
    order_id=Column(INTEGER,default=0,server_default="0",index=True)
    type=Column(INTEGER,default=0,server_default="0",index=True)
    purchase_receipt_id=Column(BIGINT,index=True,default=0,server_default="0")
    note=Column(XTVARCHAR(255),default='', server_default='')

