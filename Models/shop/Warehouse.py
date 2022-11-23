from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT,ENUM,FLOAT
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from Models.User import User
    from .Shop import Shop
class Warehouse(Base):
    __tablename__ = 'warehouse'

    warehouse_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    name = Column(XTVARCHAR(32))
    code= Column(XTVARCHAR(32))
    status=Column(ENUM('ENABLE',"DISABLE"),default='ENBALE',server_default='ENABLE')
    description=Column(XTVARCHAR(255),default='')
    latitude=Column(FLOAT())
    longitude=Column(FLOAT())
    low_stock_notification=Column(XTVARCHAR(255))
    contact_name=Column(XTVARCHAR(255))
    contact_email=Column(XTVARCHAR(255))
    contact_phone=Column(XTVARCHAR(255))
    address_country=Column(XTVARCHAR(255))
    address_state=Column(XTVARCHAR(255))
    address_city=Column(XTVARCHAR(255))
    address_street1=Column(XTVARCHAR(255))
    address_srreet2=Column(XTVARCHAR(255))
    address_postcode=Column(XTVARCHAR(255))
    user_id=Column(BIGINT,index=True)

    User:'User'=relationship('User',uselist=False,
                             primaryjoin='foreign(User.user_id) ==Warehouse.user_id',
                             back_populates='Warehouse'
                             )#type: ignore

    Shop:typing.List['Shop']=relationship('Shop',uselist=True,
                             primaryjoin='foreign(Warehouse.warehouse_id) ==Shop.warehouse_id',
                             back_populates='Warehouse'
                             )#type: ignore
