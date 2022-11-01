from component.snowFlakeId import snowFlack
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref

from typing import Any, Dict, Generic, List
from Models.ModelBase import Base,XTVARCHAR
class App(Base):
    __tablename__ = 'app'

    app_id = Column(INTEGER, primary_key=True, autoincrement=True)
    app_name=Column(XTVARCHAR(32))
    user_id=Column(BIGINT,index=True)
