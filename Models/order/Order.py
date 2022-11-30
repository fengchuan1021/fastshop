import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import OrderShipment,Product,Variant


class Order(Base):
    __tablename__ = 'order'
    order_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    market_id = Column(INTEGER, default=0,index=True)
    market_name = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    merchant_id = Column(INTEGER, default=0,index=True)
    merchant_name = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    status = Column(
        ENUM("PENDING", "PROCESSING", "SHIPPED", "COMPLETE", "REFUNDED", "PART_REFUNDED", "PART_SHIPPED", "HOLDED"),
        server_default='PENDING', default='PENDING',
        comment="待付款 / 待处理 / 已发货 / 完成 / 退款 / 部分退款 / 部分发货 / 暂停")
    order_currency_code = Column(XTVARCHAR(20), nullable=False, default='', server_default='')
    global_currency_code = Column(XTVARCHAR(20), nullable=False, default='', server_default='')
    currency_rate = Column(DECIMAL(10, 4))
    customer_email = Column(XTVARCHAR(32), nullable=False, default='', server_default='')
    customer_firstname = Column(XTVARCHAR(32), default='', server_default='')
    customer_lastname = Column(XTVARCHAR(32), default='', server_default='')
    customer_middlename = Column(XTVARCHAR(32), default='', server_default='')
    #order_number = Column(BIGINT(20), autoincrement=True)
    market_order_number = Column(XTVARCHAR(32), default='', server_default='',index=True)
    coupon_code = Column(XTVARCHAR(32), default='', server_default='')
    customer_id = Column(XTVARCHAR(32), default='', server_default='')
    payment_method = Column(XTVARCHAR(32), default='', server_default='')
    shipping_method = Column(XTVARCHAR(32), default='', server_default='')
    base_discount_amount = Column(DECIMAL(10, 4))
    base_shipping_amount = Column(DECIMAL(10, 4))
    base_grand_total = Column(DECIMAL(10, 4))
    base_tax_amount = Column(DECIMAL(10, 4))
    base_grand_total_refunded = Column(DECIMAL(10, 4))
    base_shipping_refunded = Column(DECIMAL(10, 4))
    base_tax_refunded = Column(DECIMAL(10, 4))
    tax_refunded = Column(DECIMAL(10, 4))
    shipping_refunded = Column(DECIMAL(10, 4))
    grand_refunded = Column(DECIMAL(10, 4))
    discount_amount = Column(DECIMAL(10, 4))
    shipping_amount = Column(DECIMAL(10, 4))
    grand_total = Column(DECIMAL(10, 4))
    tax_amount = Column(DECIMAL(10, 4))
    total_item_count = Column(INTEGER, default=0)
    customer_note = Column(XTVARCHAR(255), default='', server_default='')
    #created_at = Column(DATETIME) have create in baseclass.
    #updated_at = Column(DATETIME)
    OrderAddress: List['OrderAddress']=relationship('OrderAddress',uselist=True,primaryjoin='foreign(OrderAddress.order_id)==Order.order_id',back_populates='Order',cascade='')
    OrderItem: List['OrderItem'] = relationship('OrderItem', uselist=True,
                                                      primaryjoin='foreign(OrderItem.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')

    OrderStatusHistory: List['OrderStatusHistory'] = relationship('OrderStatusHistory', uselist=True,
                                                      primaryjoin='foreign(OrderStatusHistory.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')
    OrderShipment: List['OrderShipment'] = relationship('OrderShipment', uselist=True,
                                                      primaryjoin='foreign(OrderShipment.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')
class OrderAddress(Base):
    __tablename__ = 'order_address'
    order_address_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    customer_id = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    region = Column(XTVARCHAR(64), nullable=False, default='', server_default='')
    region_id = Column(INTEGER, default=0)
    postcode = Column(XTVARCHAR(64), nullable=False)

    firstname = Column(XTVARCHAR(32), default='', server_default='')
    lastname = Column(XTVARCHAR(32), default='', server_default='')
    middlename = Column(XTVARCHAR(32), default='', server_default='')

    street = Column(XTVARCHAR(255), default='', server_default='')
    city = Column(XTVARCHAR(64), default='', server_default='')
    telephone = Column(XTVARCHAR(32), default='', server_default='')
    country_id = Column(INTEGER, default=0)
    country = Column(XTVARCHAR(32), default='', server_default='')
    address_type = Column(ENUM("BILLING", "SHIPPING"), comment="账单地址 / 收货地址")
    company = Column(XTVARCHAR(255), default='', server_default='')
    #updated_at = Column(DATETIME)
    Order:'Order'=relationship('Order',uselist=False,primaryjoin='foreign(OrderAddress.order_id)==Order.order_id',back_populates='OrderAddress',cascade='')

class OrderItem(Base):

    __tablename__ = 'order_item'
    order_item_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    product_id = Column(BIGINT, default=0)
    variant_id = Column(BIGINT, default=0)
    sku = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    name = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    qty_ordered = Column(INTEGER, default=0)
    qty_invoiced = Column(INTEGER, default=0)
    qty_refunded = Column(INTEGER, default=0)
    qty_shipped = Column(INTEGER, default=0)
    price = Column(DECIMAL(10, 4))
    base_price = Column(DECIMAL(10, 4))
    original_price = Column(DECIMAL(10, 4))
    base_original_price = Column(DECIMAL(10, 4))
    discount_amount = Column(DECIMAL(10, 4))
    base_discount_amount = Column(DECIMAL(10, 4))
    cost = Column(DECIMAL(10, 4))
    base_cost = Column(DECIMAL(10, 4))
    row_total = Column(DECIMAL(10, 4))
    base_row_total = Column(DECIMAL(10, 4))
    Order:'Order'=relationship('Order',uselist=False,primaryjoin='foreign(OrderItem.order_id)==Order.order_id',back_populates='OrderItem',cascade='')
    Product:'Product'=relationship('Product',uselist=False,primaryjoin='foreign(OrderItem.product_id)==Product.product_id',cascade='')
    Variant: 'Variant' = relationship('Variant', uselist=False,
                                      primaryjoin='foreign(OrderItem.variant_id)==Product.variant_id', cascade='')



class OrderStatusHistory(Base):

    __tablename__ = 'order_status_history'
    order_status_history_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    is_customer_notified = Column(ENUM("YES", "NO"), comment="通知用户 / 不通知用户")
    status = Column(
        ENUM("PENDING", "PROCESSING", "SHIPPED", "COMPLETE", "REFUNDED", "PART_REFUNDED", "PART_SHIPPED", "HOLDED"),
        server_default='PENDING', default='PENDING',
        comment="待付款 / 待处理 / 已发货 / 完成 / 退款 / 部分退款 / 部分发货 / 暂停")
    comment = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    entity_name = Column(
        ENUM("ORDER", "INVOICE", "SHIPMENT", "REFUND"),
        server_default='ORDER', default='ORDER',
        comment="订单 / 发票 / 发货 / 退款")
    #created_at = Column(DATETIME)
    Order: 'Order' = relationship('Order', uselist=False, primaryjoin='foreign(OrderStatusHistory.order_id)==Order.order_id',
                                  back_populates='OrderStatusHistory', cascade='')




