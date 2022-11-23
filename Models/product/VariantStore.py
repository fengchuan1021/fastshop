import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL

from component.snowFlakeId import snowFlack
if typing.TYPE_CHECKING:
    from .Product import Variant,Product
    from ..store.Store import Store
    from ..store.Warehouse import Warehouse
class VariantStore(Base):
    __tablename__ = 'variant_store'
    variant_store_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)


    store_name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10,2))
    qty=Column(INTEGER)
    status = Column(ENUM("ONLINE", "OFFLINE"), server_default="OFFLINE", default="OFFLINE")

    warehouse_name = Column(XTVARCHAR(32))
    variant_id=Column(BIGINT(20),index=True)
    store_id = Column(INTEGER, index=True)
    product_id=Column(BIGINT(20),index=True)
    #warehouse_id = Column(BIGINT(20), index=True)
    Variant:'Variant'=relationship("Variant",uselist=False,primaryjoin='foreign(VariantStore.variant_id) == Variant.variant_id',back_populates='VariantStore')
    Store:'Store'=relationship('Store',uselist=False,primaryjoin='foreign(VariantStore.store_id) ==Store.store_id',back_populates='VariantStore')

    #Warehouse:'Warehouse'=relationship('Warehouse',uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) ==VariantStore.warehouse_id')

    # Product: 'Product' = relationship('Product', uselist=False,
    #                                       primaryjoin='foreign(Product.product_id) ==Product.product_id',
    #                                       back_populates='VariantStore')
