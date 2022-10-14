from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import  DATETIME, ENUM, INTEGER
class Brand(Base):
    __tablename__ = 'brand'
    brand_id=Column(INTEGER, primary_key=True,autoincrement=True)
    brand_en=Column(XTVARCHAR(16),index=True)