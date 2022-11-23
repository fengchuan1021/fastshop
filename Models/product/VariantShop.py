import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL

from component.snowFlakeId import snowFlack
if typing.TYPE_CHECKING:
    from .Product import Variant,Product
    from Models.shop.Shop import Shop
    from Models.shop.Warehouse import Warehouse
class VariantShop(Base):
    __tablename__ = 'variant_shop'
    variant_shop_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)


    shop_name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10,2))
    qty=Column(INTEGER)
    status = Column(ENUM("ONLINE", "OFFLINE"), server_default="OFFLINE", default="OFFLINE")

    warehouse_name = Column(XTVARCHAR(32))
    variant_id=Column(BIGINT(20),index=True)
    shop_id = Column(INTEGER, index=True)
    product_id=Column(BIGINT(20),index=True)
    warehouse_id = Column(BIGINT(20), index=True)
    Variant:'Variant'=relationship("Variant",uselist=False,primaryjoin='foreign(VariantShop.variant_id) == Variant.variant_id',back_populates='VariantShop')
    Shop:'Shop'=relationship('Shop',uselist=False,primaryjoin='foreign(VariantShop.shop_id) == Shop.shop_id',back_populates='VariantShop')

    Warehouse:'Warehouse'=relationship('Warehouse',uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) ==VariantShop.warehouse_id')

    # Product: 'Product' = relationship('Product', uselist=False,
    #                                       primaryjoin='foreign(Product.product_id) ==Product.product_id',
    #                                       back_populates='VariantShop')
