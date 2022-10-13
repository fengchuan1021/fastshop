
from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT,DECIMAL

from component.snowFlakeId import snowFlack
from .Product import VariantStatic
class VariantImage(Base):
    __tablename__ = 'variant_image'
    __table_args__ = (Index('product_id_order_index', "variant_id", "image_order"),)
    variant_image_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)

    variant_id = Column(BIGINT,server_default="0")
    image_url=Column(XTVARCHAR(512))
    image_alt=Column(XTVARCHAR(255))
    image_order=Column(INTEGER,server_default="0")
    Variant:'VariantStatic' = relationship('VariantStatic', uselist=False,
                           primaryjoin='foreign(VariantStatic.variant_static_id) == VariantImage.variant_id',
                           backref=backref('Images'))

class ProductImgLog(Base):
    __tablename__ = 'product_image_log'
    product_image_log_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    product_id = Column(BIGINT, server_default="0",index=True)
    image_url = Column(XTVARCHAR(512))