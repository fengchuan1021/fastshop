import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE

from component.snowFlakeId import snowFlack

if typing.TYPE_CHECKING:
    from ..store.Store import Store


class OrderShipment(Base):
    __tablename__ = 'order_shipment'
    order_shipment_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(INTEGER, default=0)
    total_weight = Column(DECIMAL(10, 4))
    total_qty = Column(DECIMAL(10, 4))
    shipping_address_id = Column(INTEGER, default=0)
    billing_address_id = Column(INTEGER, default=0)
    shipment_number = Column(XTVARCHAR(255), default='', server_default='')
    carrier_name = Column(XTVARCHAR(64), default='', server_default='')
    carrier_code = Column(XTVARCHAR(64), default='', server_default='')
    track_number = Column(XTVARCHAR(64), default='', server_default='')
    description = Column(XTVARCHAR(64), default='', server_default='')
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)

class OrderShipmentItem(Base):
    __tablename__ = 'order_shipment_item'
    order_shipment_item_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(INTEGER, default=0)
    order_shipment_id = Column(INTEGER, default=0)
    order_item_id = Column(INTEGER, default=0)
    product_id = Column(INTEGER, default=0)
    variant_id = Column(INTEGER, default=0)
    qty = Column(INTEGER, default=0)
    weight = Column(INTEGER, default=0)
    name = Column(XTVARCHAR(255), default='', server_default='')
    sku = Column(XTVARCHAR(64), default='', server_default='')
    warehouse_id = Column(INTEGER, default=0)







