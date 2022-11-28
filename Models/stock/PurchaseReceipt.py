from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT,ENUM,FLOAT,INTEGER
from Models.ModelBase import Base,XTVARCHAR
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import Variant

class PurchaseReceipt(Base):
    __tablename__='purchase_receipt'
    purchase_receipt_id=Column(BIGINT, primary_key=True, default=snowFlack.getId,comment="primary key")


class PurchaseReceiptItems(Base):
    __tablename__='purchase_receipt_items'
    purchase_receipt_items_id=Column(BIGINT, primary_key=True, default=snowFlack.getId,comment="primary key")

    supplier_id=Column(INTEGER,index=True)
    purchaser=Column(XTVARCHAR(32))
    warehouse_id=Column(BIGINT,index=True)