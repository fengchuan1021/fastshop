import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL

from component.snowFlakeId import snowFlack
if typing.TYPE_CHECKING:
    from .Product import Variant,Product
    from ..store.Store import Store


class VariantStore(Base):
    __tablename__ = 'variant_store'
    variant_store_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)


    store_name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10,2))
    qtyshare = Column(ENUM("YES", "NO"), server_default="YES", default="YES")
    qty=Column(INTEGER,default=0,server_default='0')
    status = Column(ENUM("ONLINE", "OFFLINE"), server_default="OFFLINE", default="OFFLINE")#上下架 状态
    # 产品在第三方市场的状态 已审核 被市场删除...
    market_variant_status=Column(ENUM("PENDING_REVIEW" ,"APPROVED" ,"REJECTED" ,"REMOVED_BY_WISH" ,"REMOVED_BY_MERCHANT"), server_default="APPROVED", default="APPROVED")

    #warehouse_name = Column(XTVARCHAR(32))

    variant_id=Column(BIGINT(20),index=True)
    store_id = Column(INTEGER, index=True)
    product_id=Column(BIGINT(20),index=True)
    merchant_id = Column(INTEGER, default=0)

    warehouse_ids=Column(XTVARCHAR(512),default='',server_default='',comment="use which warehouse,if empty use all warehouse")#该店铺的此商品从哪几个仓库发货，为空表示所有仓库
    deliver_strategy=Column(XTVARCHAR(512),default='',server_default='',comment="deliver stratege,use ',' delimiter")#发货策略
    #warehouse_id = Column(BIGINT(20), index=True)
    Variant:'Variant'=relationship("Variant",uselist=False,primaryjoin='foreign(VariantStore.variant_id) == Variant.variant_id',back_populates='VariantStore',cascade='')
    Store:'Store'=relationship('Store',uselist=False,primaryjoin='foreign(VariantStore.store_id) ==Store.store_id',back_populates='VariantStore',cascade='')
    Product: 'Product' = relationship('Product', uselist=False,
                                          primaryjoin='foreign(VariantStore.product_id) ==Product.product_id',
                                          back_populates='VariantStore',cascade='')
    #Warehouse:'Warehouse'=relationship('Warehouse',uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) ==VariantStore.warehouse_id')

    # Product: 'Product' = relationship('Product', uselist=False,
    #                                       primaryjoin='foreign(Product.product_id) ==Product.product_id',
    #                                       back_populates='VariantStore')
