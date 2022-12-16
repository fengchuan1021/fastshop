from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL,CHAR
from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

class Country(Base):
    __tablename__ ='country'
    country_id=Column(INTEGER,autoincrement=True,primary_key=True)

    name_en=Column(XTVARCHAR(80))
    name_cn=Column(XTVARCHAR(80))

    country_code2 = Column(CHAR(3), index=True)
    country_code3=Column(CHAR(3), index=True,default='',server_default='')
    continent=Column(ENUM('Europe','North America','South America','Asia','Oceania','Africa','Other'))
    currency_code=Column(XTVARCHAR(8),index=True)
    currency_symbol=Column(XTVARCHAR(4))
    smt_code=Column(CHAR(3))
    is_hot=Column(ENUM("Y","N"),default='N',server_default='N')
