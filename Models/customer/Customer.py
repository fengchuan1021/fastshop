from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE, TIMESTAMP, CHAR

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    pass


class Customer(Base):
    __tablename__ ='customer'
    customer_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    email=Column(XTVARCHAR(64),index=True)
    full_name=Column(XTVARCHAR(64))
    country=Column(XTVARCHAR(64))
    country_code=Column(CHAR(3),index=True)
    order_amount=Column(DECIMAL(10,4),default=0,server_default="0")#总下单金额 包含未付款的
    total_paid=Column(DECIMAL(10, 4),default=0,server_default="0")
    order_count=Column(INTEGER)
