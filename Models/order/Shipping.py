

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE

from component.snowFlakeId import snowFlack
from typing import List,TYPE_CHECKING
if TYPE_CHECKING:
    from Models import Order,Product,Variant,Warehouse


class OrderShipment(Base):
    __tablename__ = 'order_shipment'
    order_shipment_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    market_order_id = Column(XTVARCHAR(32), default='', server_default='')
    total_weight = Column(DECIMAL(10, 4))
    total_qty = Column(DECIMAL(10, 4))
    shipping_address_id = Column(BIGINT, default=0)
    billing_address_id = Column(BIGINT, default=0)
    #shipment_number = Column(XTVARCHAR(255), default='', server_default='')
    carrier_name = Column(XTVARCHAR(64), default='', server_default='')
    carrier_code = Column(XTVARCHAR(64), default='', server_default='')
    track_number = Column(XTVARCHAR(64), default='', server_default='')
    description = Column(XTVARCHAR(64), default='', server_default='')
    market_package_id=Column(XTVARCHAR(64), default='', server_default='')
    market_updatetime=Column(DATETIME(fsp=3))
    package_status=Column(INTEGER,default=0, server_default='0')
    #created_at = Column(DATETIME)
    #updated_at = Column(DATETIME)
    Order: 'Order' = relationship('Order', uselist=False, primaryjoin='foreign(OrderShipment.order_id)==Order.order_id',
                                  back_populates='OrderShipment', cascade='')
    OrderShipmentItem: List['OrderShipmentItem'] = relationship('OrderShipmentItem', uselist=True, primaryjoin='foreign(OrderShipmentItem.order_shipment_id)==OrderShipment.order_shipment_id',
                                  back_populates='OrderShipment', cascade='')
class OrderShipmentItem(Base):
    __tablename__ = 'order_shipment_item'
    order_shipment_item_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_shipment_id = Column(BIGINT, default=0, index=True)
    order_id = Column(BIGINT, default=0,index=True)
    market_order_id=Column(XTVARCHAR(32),default='',server_default='')
    market_sku_id=Column(XTVARCHAR(32),default='',server_default='')

    order_item_id = Column(BIGINT, default=0)
    product_id = Column(INTEGER, default=0)
    variant_id = Column(INTEGER, default=0)
    qty = Column(INTEGER, default=0)
    weight = Column(INTEGER, default=0)
    name = Column(XTVARCHAR(255), default='', server_default='')
    sku = Column(XTVARCHAR(64), default='', server_default='')
    warehouse_id = Column(BIGINT, default=0)

    OrderShipment: 'OrderShipment' = relationship('OrderShipment', uselist=False, primaryjoin='foreign(OrderShipmentItem.order_shipment_id)==OrderShipment.order_shipment_id',
                                  back_populates='OrderShipmentItem', cascade='')

    Product: 'Product' = relationship('Product', uselist=False, primaryjoin='foreign(OrderShipmentItem.product_id)==Product.product_id',cascade='')
    Variant: 'Variant' = relationship('Variant', uselist=False,
                                      primaryjoin='foreign(OrderShipmentItem.variant_id)==Variant.variant_id',
                                      cascade='')
    Warehouse: 'Warehouse' = relationship('Warehouse', uselist=False,
                                      primaryjoin='foreign(OrderShipmentItem.warehouse_id)==Warehouse.warehouse_id',
                                      cascade='')







