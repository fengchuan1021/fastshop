
from sqlalchemy.orm import deferred, relationship, backref
from Models.ModelBase import Base
from sqlalchemy import Column, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT,DECIMAL

from component.snowFlakeId import snowFlack

class VariantImage(Base):
    __tablename__ = 'variant_image'
    __table_args__ = (Index('product_id_order_index', "variant_id", "image_order"),)
    variant_image_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)

    variant_id = Column(BIGINT,server_default="0")
    image_url=Column(VARCHAR(512))
    image_alt=Column(VARCHAR(255))
    image_order=Column(INTEGER,server_default="0")
    Variant = relationship('VariantStatic', uselist=False,
                           primaryjoin='foreign(VariantStatic.variant_static_id) == VariantImage.variant_id',
                           backref=backref('Images'))

