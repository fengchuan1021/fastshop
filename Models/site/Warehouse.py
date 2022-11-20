
from component.snowFlakeId import snowFlack
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from ..ModelBase import Base,XTVARCHAR


class Warehouse(Base):
    __tablename__ = 'warehouse'

    warehouse_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    warehouse_name = Column(XTVARCHAR(32),unique=True)

    company_name = Column(XTVARCHAR(32),default='',server_default='')
    company_id=Column(BIGINT,default=0,server_default='0')
    warehouse_mark=Column(XTVARCHAR(255),default='',server_default='')

