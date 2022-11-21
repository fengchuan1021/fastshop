import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL

from component.snowFlakeId import snowFlack
if typing.TYPE_CHECKING:
    from .Product import Variant

class VariantShop(Base):
    __tablename__ = 'variant_shop'
    variant_shop_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    variant_id=Column(BIGINT(20),index=True)
    product_id=Column(BIGINT(20),index=True)
    shop_id=Column(INTEGER,index=True)
    shop_name=Column(XTVARCHAR(32))
    price=Column(DECIMAL(10,2))
    qty=Column(INTEGER)
    status = Column(ENUM("ONLINE", "OFFLINE"), server_default="OFFLINE", default="OFFLINE")
    warehouse_id=Column(BIGINT(20), index=True)
    warehouse_name = Column(XTVARCHAR(32))
    Variant:'Variant'=relationship("Variant",uselist=True,primaryjoin='foreign(VariantShop.variant_id) == Variant.variant_id',back_populates='VariantShop')
