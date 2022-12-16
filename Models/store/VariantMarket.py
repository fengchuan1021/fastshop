from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from Models import Base
from component.snowFlakeId import snowFlack


# class VariantMarket(Base):
#     __tablename__ = 'variant_market'
#     variant_market_id=Column(BIGINT,primary_key=True, default=snowFlack.getId, comment="primary key")
#     variant_id=Column(BIGINT,index=True)
#     market_id=Column(INTEGER,index=True)