from component.snowFlakeId import snowFlack
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT,INTEGER
from sqlalchemy.orm import relationship, backref
from Models.ModelBase import Base,XTVARCHAR
import typing
if typing.TYPE_CHECKING:
    from Models.User import User

class Merchant(Base):
    __tablename__='merchant'
    merchant_id=Column(INTEGER, primary_key=True, autoincrement=True)
    user_id=Column(BIGINT, index=True)
    merchant_name=Column(XTVARCHAR(32))
    company_name=Column(XTVARCHAR(32),default='')
    company_url=Column(XTVARCHAR(32),default='')
    contacts_firstname=Column(XTVARCHAR(32),default='')
    contacts_lastname=Column(XTVARCHAR(32),default='')
    contacts_tels=Column(XTVARCHAR(32),default='')
    contacts_emial=Column(XTVARCHAR(32),default='')
    User:'User'=relationship('User',uselist=False,
                             primaryjoin='foreign(User.user_id) ==Merchant.user_id',
                             back_populates='Merchant'
                             )#type: ignore

    # tiktok_appid=Column(XTVARCHAR(64),default='')
    # tiktok_secret=Column(XTVARCHAR(128), default='')
    # tiktok_shopid=Column(XTVARCHAR(128),default='')
    # tiktok_token=Column(XTVARCHAR(512),default='')
    #
    # onbuy_key=Column(XTVARCHAR(64),default='')
    # onbuy_secret=Column(XTVARCHAR(64),default='')

