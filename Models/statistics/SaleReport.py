import typing

from sqlalchemy.orm import relationship

from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL, DATETIME, DATE, TIMESTAMP, TEXT

from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING,List
if TYPE_CHECKING:
    from Models import Store
class SaleReport(Base):
    __tablename__='salereport'
    salereport_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId)


    date=Column(DATE,index=True)

    order_amount=Column(DECIMAL(10,4),default=0,server_default="0")#总下单金额 包含未付款的
    order_count=Column(INTEGER)#总下单数量 包含未付款的
    total_paid = Column(DECIMAL(10, 4), default=0, server_default="0")
    order_paid=Column(INTEGER,default=0, server_default="0")
    refund_money=Column(DECIMAL(10, 4), default=0,server_default="0")
    refund_ordercnt=Column(INTEGER,default=0, server_default="0")

    store_id = Column(INTEGER, index=True)
    store_name=Column(XTVARCHAR(32))
    Store:'Store'=relationship('Store',uselist=False,primaryjoin="foreign(SaleReport.store_id)==Store.store_id",cascade='')
    #user_id=Column(BIGINT,index=True,default=0,server_default="0")#客户对应的user_id,
    merchant_id=Column(INTEGER,index=True)
