
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from ..ModelBase import Base


class Warehouse(Base):
    __tablename__ = 'warehouse'

    warehouse_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    warehouse_name = Column(VARCHAR(32),unique=True)

    company_name = Column(VARCHAR(32),nullable=True)
    company_id=Column(BIGINT,nullable=True)
    warehouse_mark=Column(VARCHAR(255),default='',server_default='')

