
from sqlalchemy.orm import deferred, relationship
from Models.ModelBase import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, text, Index
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,TEXT

from component.snowFlakeId import snowFlack

class ProductImage(Base):
    __tablename__ = 'product_image'
    __table_args__ = (Index('product_id_order_index', "product_id", "image_order"),)
    product_id=Column(BIGINT,ForeignKey('variant_static.variant_static_id'),server_default="0")
    image_url=Column(VARCHAR(512))
    image_alt=Column(VARCHAR(255))
    image_order=Column(INTEGER,server_default="0")

