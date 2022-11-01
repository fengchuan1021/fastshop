from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from ..ModelBase import Base,XTVARCHAR
from ..User import User

class Enterprise(Base):
    __tablename__='enterprise'
    enterprise_id=Column(BIGINT, primary_key=True, default=snowFlack.getId)
    user_id=Column(BIGINT, index=True)
    enterprise_name=Column(XTVARCHAR(32))
    UserModel:'User'=relationship('User',uselist=False,
                             primaryjoin='foreign(User.user_id) ==Enterprise.enterprise_id',
                             backref=backref('Enterprise')
                             )#type: ignore

    tiktok_appid=Column(XTVARCHAR(64),default='')
    tiktok_secret=Column(XTVARCHAR(128), default='')
    tiktok_shopid=Column(XTVARCHAR(128),default='')
    tiktok_token=Column(XTVARCHAR(512),default='')

