from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, ENUM, FLOAT, INTEGER
from Models.ModelBase import Base, XTVARCHAR
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Models import Variant, Warehouse


class VariantWarehouse(Base):
    __tablename__ = 'variant_warehouse'
    variant_warehouse_id = Column(BIGINT, primary_key=True, default=snowFlack.getId, comment="primary key")
    warehouse_id = Column(BIGINT, index=True)
    variant_id = Column(BIGINT, index=True)
    qty = Column(INTEGER, default=0, server_default='0', index=True)

    Warehouse: Warehouse = relationship('Warehouse',
                                        primaryjoin='foreign(VariantWarehouse.warehouse_id)==Warehouse.warehouse_id',
                                        uselist=False, back_populates='VariantWarehouse',
                                        cascade=''
                                        )
    # Variant:'Variant'=relationship('VariantWarehouse',uselist=False,primaryjoin='foreign(VariantWarehouse.variant_id)==Variant.variant_id',back_populates='VariantWarehouse',cascade='')

    warehouse_name = Column(XTVARCHAR(32))
