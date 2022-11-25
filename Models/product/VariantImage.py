
from sqlalchemy.orm import relationship
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from component.snowFlakeId import snowFlack
from .Product import Variant
import typing
if typing.TYPE_CHECKING:
    from ..store.Merchant import Merchant
    from ..store.Store import Store
class VariantImage(Base):
    __tablename__ = 'variant_image'
    __table_args__ = (Index('product_id_order_index', "variant_id", "image_order"),)
    variant_image_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)

    variant_id = Column(BIGINT,server_default="0")
    image_url=Column(XTVARCHAR(512))
    image_alt=Column(XTVARCHAR(255))
    image_order=Column(INTEGER,server_default="0")
    Variant:'Variant' = relationship('Variant', uselist=False,
                           primaryjoin='foreign(Variant.variant_id) == VariantImage.variant_id',
                           back_populates='VariantImage',viewonly=True
                                     )
    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)
    Merchant:'Merchant'=relationship('Merchant', uselist=False,
                           primaryjoin='foreign(Merchant.merchant_id) == VariantImage.merchant_id',viewonly=True
                           )#back_populates='VariantImage'
    Store:'Store'=relationship('Store', uselist=False,
                           primaryjoin='foreign(Store.store_id) == VariantImage.store_id',viewonly=True
                           )#back_populates='VariantImage'

# class ProductImgLog(Base):
#     __tablename__ = 'product_image_log'
#     product_image_log_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
#     product_id = Column(BIGINT, server_default="0",index=True)
#     image_url = Column(XTVARCHAR(512))