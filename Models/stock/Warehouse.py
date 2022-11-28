from sqlalchemy.orm import relationship

from component.snowFlakeId import snowFlack
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT,ENUM,FLOAT,INTEGER
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from Models.User import User
    from Models.store.Store import Store
    from Models.store.Merchant import Merchant
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
    #user_id=Column(BIGINT,index=True)
    merchant_id=Column(INTEGER,index=True)
    # User:'User'=relationship('User',uselist=False,
    #                          primaryjoin='foreign(Warehouse.user_id) ==User.user_id',
    #                          back_populates='Warehouse',cascade=''
    #                          )#type: ignore

    Merchant:'Merchant'=relationship('Merchant',uselist=False,
                             primaryjoin='foreign(Warehouse.merchant_id) ==Merchant.merchant_id',
                             back_populates='Warehouse',cascade=''
                             )#type: ignore
    # Store:typing.List['Store']=relationship('Store',uselist=True,
    #                          primaryjoin='foreign(Store.warehouse_id) ==Warehouse.warehouse_id',
    #                          back_populates='Warehouse',cascade=''
    #                          )#type: ignore
