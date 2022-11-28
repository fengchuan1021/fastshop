from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT,ENUM,FLOAT,INTEGER
from Models.ModelBase import Base,XTVARCHAR
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import Variant

class Supplier(Base):
    __tablename__='supplier'
    supplier_id=Column(INTEGER,autoincrement=True,primary_key=True)
    name=Column(XTVARCHAR(32),nullable=False)
    url=Column(XTVARCHAR(32),nullable=True,comment="主页网址")
    address=Column(XTVARCHAR(32),nullable=True,comment="公司地址")
    mark = Column(XTVARCHAR(255), nullable=True, comment="备注信息")
    Settlement=Column(ENUM("deliver against payment","cash on delivery","Payment in account period","every week",'every half month','every month'),comment="结算方式：款到发货 货到付款 账期结算 周结 半月结 月结")
    contactname=Column(XTVARCHAR(32),nullable=True,comment="联系人")
    contactphone=Column(XTVARCHAR(32),nullable=True,comment="联系电话")
    contactemail=Column(XTVARCHAR(32),nullable=True,comment="联系邮箱")
    contactqq=Column(XTVARCHAR(32),nullable=True,comment="联系QQ")
    bankname=Column(XTVARCHAR(32),nullable=True,comment="供货商银行名称")
    bankaccount=Column(XTVARCHAR(32),nullable=True,comment="供货商银行账号")
    paymethod=Column(ENUM("bank transfer",'cash'),nullable=True,comment="付款方式 银行转账 现金")
    drawee=Column(XTVARCHAR(32),nullable=True,comment="付款人")

    SupplierVariant:List['SupplierVariant']=relationship('SupplierVariant',primaryjoin="foreign(SupplierVariant.supplier_id)==Supplier.supplier_id",cascade='',back_populates='Supplier')
class SupplierVariant(Base):
    __tablename__='suppliervariant'
    __table_args__ = (UniqueConstraint('supplier_id', "variant_id", name="suppliervariant"),)
    suppliervariant_id=Column(BIGINT, primary_key=True, default=snowFlack.getId,comment="primary key")
    supplier_id=Column(INTEGER)
    variant_id=Column(BIGINT)
    Supplier:'Supplier'=relationship('Supplier',primaryjoin="foreign(SupplierVariant.supplier_id)==Supplier.supplier_id",cascade='',back_populates='SupplierVariant')
    Variant: 'Variant' = relationship('Variant',
                                        primaryjoin="foreign(SupplierVariant.variant_id)==Variant.variant_id",
                                        cascade='', back_populates='SupplierVariant')