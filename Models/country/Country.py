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

    country_name=Column(XTVARCHAR(80))
    country_code2 = Column(CHAR(2), index=True)
    country_code3=Column(CHAR(3), index=True)
    currency_name=Column(XTVARCHAR(20))
    currency_code=Column(XTVARCHAR(8),index=True)
    currency_symbol=Column(XTVARCHAR(4))
