from openapi_schema_validator._validators import nullable

from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, DECIMAL
from sqlalchemy.orm import relationship

from Models.ModelBase import Base,XTVARCHAR
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

class Country(Base):
    __tablename__ ='country'
    country_id=Column(INTEGER,autoincrement=True,primary_key=True)
    country_code=Column(XTVARCHAR(4),index=True)
    country_name=Column(XTVARCHAR(32))
