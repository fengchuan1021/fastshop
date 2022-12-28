import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE,TIMESTAMP

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import OrderShipment,Product,Variant


class Order(Base):
    __tablename__ = 'order'
    order_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    market_id = Column(INTEGER, default=0,index=True)
    market_name = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    market_order_id = Column(XTVARCHAR(32), default='', server_default='', index=True)
    merchant_id = Column(INTEGER, default=0,index=True)
    store_id=Column(INTEGER,default=0,index=True)
    store_name=Column(XTVARCHAR(32),default='',server_default='')
    merchant_name = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    # status = Column(
    #     ENUM("PENDING", "PROCESSING", "SHIPPED", "COMPLETE", "REFUNDED", "PART_REFUNDED", "PART_SHIPPED", "HOLDED"),
    #     server_default='PENDING', default='PENDING',
    #     comment="待付款 / 待处理 / 已发货 / 完成 / 退款 / 部分退款 / 部分发货 / 暂停")
    status=Column(XTVARCHAR(32),default='',server_default='')
    order_currency_code = Column(XTVARCHAR(20), nullable=False, default='', server_default='')
    global_currency_code = Column(XTVARCHAR(20), nullable=False, default='', server_default='')
    currency_rate = Column(DECIMAL(10, 4))
    customer_email = Column(XTVARCHAR(32), nullable=False, default='', server_default='')
    customer_firstname = Column(XTVARCHAR(64), default='', server_default='')
    customer_lastname = Column(XTVARCHAR(32), default='', server_default='')
    customer_middlename = Column(XTVARCHAR(32), default='', server_default='')
    #order_number = Column(BIGINT(20), autoincrement=True)

    coupon_code = Column(XTVARCHAR(32), default='', server_default='')
    customer_id = Column(XTVARCHAR(32), default='', server_default='')
    payment_method = Column(XTVARCHAR(32), default='', server_default='')
    paied_time=Column(DATETIME(fsp=3))
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
    market_updatetime=Column(DATETIME(fsp=3))
    market_createtime=Column(DATETIME(fsp=3))
    market_delivery_option=Column(XTVARCHAR(32), default='', server_default='')#配送方式
    #created_at = Column(DATETIME) have create in baseclass.
    #updated_at = Column(DATETIME)
    ShipOrderAddress: 'ShipOrderAddress'=relationship('ShipOrderAddress',uselist=False,primaryjoin='foreign(ShipOrderAddress.order_id)==Order.order_id',back_populates='Order',cascade='')
    BillOrderAddress: 'BillOrderAddress'=relationship('BillOrderAddress',uselist=False,primaryjoin='foreign(BillOrderAddress.order_id)==Order.order_id',back_populates='Order',cascade='')

    OrderItem: List['OrderItem'] = relationship('OrderItem', uselist=True,
                                                      primaryjoin='foreign(OrderItem.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')

    OrderStatusHistory: List['OrderStatusHistory'] = relationship('OrderStatusHistory', uselist=True,
                                                      primaryjoin='foreign(OrderStatusHistory.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')
    OrderShipment: List['OrderShipment'] = relationship('OrderShipment', uselist=True,
                                                      primaryjoin='foreign(OrderShipment.order_id)==Order.order_id',
                                                      back_populates='Order', cascade='')
class BillOrderAddress(Base):
    __tablename__ = 'billorder_address'
    billorder_address_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    customer_id = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    region = Column(XTVARCHAR(64), nullable=False, default='', server_default='')
    region_id = Column(INTEGER, default=0)
    postcode = Column(XTVARCHAR(64), nullable=False)

    firstname = Column(XTVARCHAR(64), default='', server_default='')
    lastname = Column(XTVARCHAR(32), default='', server_default='')
    middlename = Column(XTVARCHAR(32), default='', server_default='')

    street = Column(XTVARCHAR(255), default='', server_default='')
    district=Column(XTVARCHAR(64), default='', server_default='')
    city = Column(XTVARCHAR(64), default='', server_default='')
    telephone = Column(XTVARCHAR(32), default='', server_default='')
    country_id = Column(INTEGER, default=0)
    country_code=Column(XTVARCHAR(3), default='',server_default='')
    country = Column(XTVARCHAR(80), default='', server_default='')
    company = Column(XTVARCHAR(255), default='', server_default='')
    full_address=Column(XTVARCHAR(255),default='',server_default='')
    #updated_at = Column(DATETIME)
    Order:'Order'=relationship('Order',uselist=False,primaryjoin='foreign(BillOrderAddress.order_id)==Order.order_id',back_populates='BillOrderAddress',cascade='')
    is_tmp=Column(ENUM("Y","N"),default='Y',server_default='Y')#临时使用 以后删除，来自第三方市场的地址没有id 一段时间后自动删除

class ShipOrderAddress(Base):
    __tablename__ = 'shiporder_address'
    shiporder_address_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    customer_id = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    region = Column(XTVARCHAR(64), nullable=False, default='', server_default='')
    region_id = Column(INTEGER, default=0)
    postcode = Column(XTVARCHAR(64), nullable=False)

    firstname = Column(XTVARCHAR(64), default='', server_default='')
    lastname = Column(XTVARCHAR(32), default='', server_default='')
    middlename = Column(XTVARCHAR(32), default='', server_default='')

    street = Column(XTVARCHAR(255), default='', server_default='')
    district=Column(XTVARCHAR(64), default='', server_default='')
    city = Column(XTVARCHAR(64), default='', server_default='')
    telephone = Column(XTVARCHAR(32), default='', server_default='')
    country_id = Column(INTEGER, default=0)
    country_code=Column(XTVARCHAR(3), default='',server_default='')
    country = Column(XTVARCHAR(80), default='', server_default='')
    company = Column(XTVARCHAR(255), default='', server_default='')
    full_address=Column(XTVARCHAR(255),default='',server_default='')
    #updated_at = Column(DATETIME)
    Order:'Order'=relationship('Order',uselist=False,primaryjoin='foreign(ShipOrderAddress.order_id)==Order.order_id',back_populates='ShipOrderAddress',cascade='')
    is_tmp=Column(ENUM("Y","N"),default='Y',server_default='Y')#临时使用 以后删除，来自第三方市场的地址没有id 一段时间后自动删除

class OrderItem(Base):

    __tablename__ = 'order_item'
    order_item_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    order_id = Column(BIGINT, default=0,index=True)
    product_id = Column(BIGINT, default=0)
    variant_id = Column(BIGINT, default=0)
    market_product_id=Column(XTVARCHAR(32),default='')
    market_variant_id=Column(XTVARCHAR(32), default='')
    sku = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    product_name = Column(XTVARCHAR(255), default='', server_default='')
    variant_name = Column(XTVARCHAR(255), default='', server_default='')
    image=Column(XTVARCHAR(255), nullable=False,default='', server_default='')
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
                                      primaryjoin='foreign(OrderItem.variant_id)==Variant.variant_id', cascade='')



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




