from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, ENUM, FLOAT, INTEGER, DECIMAL, DATETIME
from Models.ModelBase import Base, XTVARCHAR
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Models import Variant, Warehouse,WarehouseShelve


class VariantWarehouseRedeploy(Base):
    __tablename__ = 'variant_warehouse_redeploy'
    variant_warehouse_redeploy_id = Column(BIGINT, primary_key=True, default=snowFlack.getId, comment="primary key")
    merchant_id = Column(INTEGER, index=True)
    receive_warehouse_id=Column(BIGINT,index=True)
    dispatch_warehouse_id=Column(BIGINT,index=True)
    dispatcher_name=Column(XTVARCHAR(32),default='',server_default='')
    redeployment_fees=Column(DECIMAL(10, 4),default='0',server_default='0')
    other_fees=Column(DECIMAL(10, 4),default='0',server_default='0')
    expected_arrival_time=Column(DATETIME)
    note=Column(XTVARCHAR(255),default='',server_default='')




    ReceiveWarehouse: 'Warehouse' = relationship('Warehouse',
                                        primaryjoin='foreign(VariantWarehouseRedeploy.receive_warehouse_id)==Warehouse.warehouse_id',
                                        uselist=False,
                                        cascade=''
                                        )
    DispatcherWarehouse: 'Warehouse' = relationship('Warehouse',
                                        primaryjoin='foreign(VariantWarehouseRedeploy.dispatch_warehouse_id)==Warehouse.warehouse_id',
                                        uselist=False,
                                        cascade=''
                                        )


class VariantWarehouseRedeployItem(Base):
    __tablename__ = 'variant_warehouse_redeploy_item'
    variant_warehouse_redeploy_item_id = Column(BIGINT, primary_key=True, default=snowFlack.getId, comment="primary key")
    variant_warehouse_redeploy_id =Column(BIGINT, index=True)

    merchant_id = Column(INTEGER, index=True)
    variant_id= Column(BIGINT)
    redeploy_qty=Column(INTEGER,default=0,server_default='0')
    Variant:Variant=relationship("Variant",primaryjoin="foreign(VariantWarehouseRedeployItem.variant_id)==Variant.variant_id",uselist=False,cascade='')

class Package(Base):
    __tablename__ ='package'
    package_id=Column(BIGINT,primary_key=True, default=snowFlack.getId, comment="primary key")
    name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10, 4),default=0,server_default="0")
    length=Column(INTEGER)
    width = Column(INTEGER)
    height = Column(INTEGER)
    weight = Column(INTEGER)

    note=Column(XTVARCHAR(255),default='', server_default='')