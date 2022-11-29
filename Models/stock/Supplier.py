from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, ENUM, FLOAT, INTEGER
from Models.ModelBase import Base, XTVARCHAR
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Models import Variant, PurchaseReceipt


class Supplier(Base):
    __tablename__ = 'supplier'
    supplier_id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(XTVARCHAR(32), nullable=False)
    url = Column(XTVARCHAR(32), nullable=True, comment="Web Url")
    address = Column(XTVARCHAR(32), nullable=True, comment="Company Address")
    mark = Column(XTVARCHAR(255), nullable=True, comment="Note info")
    Settlement = Column(ENUM("deliver against payment", "cash on delivery", "Payment in account period", "every week",
                             'every half month', 'every month'),
                        comment="checkout: Cash on delivery / Cash on delivery / Account settlement / Weekly / Semi-monthly / Monthly")
    contactname = Column(XTVARCHAR(32), nullable=True, comment="Contacts")
    contactphone = Column(XTVARCHAR(32), nullable=True, comment="Contacts Phone")
    contactemail = Column(XTVARCHAR(32), nullable=True, comment="Contacts Email")
    bankname = Column(XTVARCHAR(32), nullable=True, comment="Name of supplier bank")
    bankaccount = Column(XTVARCHAR(32), nullable=True, comment="Supplier's bank account")
    paymethod = Column(ENUM("bank transfer", 'cash'), nullable=True, comment="Payment method: Bank transfer / Cash")

    PurchaseReceipt: List['PurchaseReceipt'] = relationship('PurchaseReceipt', uselist=True,
                                                            primaryjoin='foreign(PurchaseReceipt.supplier_id)==Supplier.supplier_id',
                                                            back_populates='Supplier', cascade=''
                                                            )

    SupplierVariant: List['SupplierVariant'] = relationship('SupplierVariant',
                                                            primaryjoin="foreign(SupplierVariant.supplier_id)==Supplier.supplier_id",
                                                            cascade='', back_populates='Supplier')


class SupplierVariant(Base):
    __tablename__ = 'suppliervariant'
    __table_args__ = (UniqueConstraint('supplier_id', "variant_id", name="suppliervariant"),)
    suppliervariant_id = Column(BIGINT, primary_key=True, default=snowFlack.getId, comment="primary key")
    supplier_id = Column(INTEGER)
    variant_id = Column(BIGINT)
    Supplier: 'Supplier' = relationship('Supplier',
                                        primaryjoin="foreign(SupplierVariant.supplier_id)==Supplier.supplier_id",
                                        cascade='', back_populates='SupplierVariant')
    Variant: 'Variant' = relationship('Variant',
                                      primaryjoin="foreign(SupplierVariant.variant_id)==Variant.variant_id",
                                      cascade='', back_populates='SupplierVariant')
