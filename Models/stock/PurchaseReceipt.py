from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT,ENUM,FLOAT,INTEGER,DECIMAL
from Models.ModelBase import Base,XTVARCHAR
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import Variant,Supplier,Warehouse

class PurchaseReceipt(Base):
    '''采购单'''
    __tablename__='purchase_receipt'
    purchase_receipt_id=Column(BIGINT, primary_key=True, default=snowFlack.getId,comment="primary key")
    supplier_id = Column(INTEGER, index=True)
    supplier_name=Column(XTVARCHAR(32))

    purchaser_id = Column(BIGINT,index=True)
    purchaser_name = Column(XTVARCHAR(32))
    avgtype=Column(ENUM('AVGNUMBER','AVGMONEY','AVGWEIGHT'))#运费均摊 按数量 按金额 按重量
    warehouse_id=Column(BIGINT,index=True,comment='to warehouse_id')
    to_warehousename=Column(XTVARCHAR(32))
    ordernumber=Column(XTVARCHAR(32))
    mark=Column(XTVARCHAR(512))
    shipfee=Column(DECIMAL(10,2),default=0,server_default='0')
    otherfee=Column(DECIMAL(10,2),default=0,server_default='0')
    productmoney=Column(DECIMAL(10,2),default=0,server_default='0')
    totalmoney=Column(DECIMAL(10,2),default=0,server_default='0',comment='shipfee+otherfee+productmoney')
    arrivein=Column(ENUM('1day','3day','5day','7day','9day','15day'),comment='arrive in n days')

    Supplier:'Supplier'=relationship('Supplier',uselist=False,primaryjoin='foreign(PurchaseReceipt.supplier_id)==Supplier.supplier_id',back_populates='PurchaseReceipt',cascade='')
    Warehouse: 'Warehouse' = relationship('Warehouse',uselist=False, primaryjoin='foreign(PurchaseReceipt.warehouse_id)==Warehouse.warehouse_id',
                                        back_populates='PurchaseReceipt', cascade='')

    PurchaseReceiptItems:List['PurchaseReceiptItems']=relationship('PurchaseReceiptItems',primaryjoin='foreign(PurchaseReceiptItems.purchase_receipt_id)==PurchaseReceipt.purchase_receipt_id',
                                                   uselist=True,back_populates='PurchaseReceipt',cascade=''
                                                   )

class PurchaseReceiptItems(Base):
    '''采购单详情'''
    __tablename__='purchase_receipt_items'
    purchase_receipt_items_id=Column(BIGINT, primary_key=True, default=snowFlack.getId,comment="primary key")

    purchase_receipt_id=Column(BIGINT,index=True)

    variant_id=Column(BIGINT,index=True)
    variant_name=Column(XTVARCHAR(128))
    variant_img=Column(XTVARCHAR(512))
    number=Column(INTEGER,default=0,server_default='0')
    price=Column(DECIMAL(10,2),default='0',server_default='0')
    totalmoney=Column(DECIMAL(10,2),default='0',server_default='0',comment='number*price')

    PurchaseReceipt:'PurchaseReceipt'=relationship('PurchaseReceipt',primaryjoin='foreign(PurchaseReceiptItems.purchase_receipt_id)==PurchaseReceipt.purchase_receipt_id',
                                                   uselist=False,back_populates='PurchaseReceiptItems',cascade=''
                                                   )