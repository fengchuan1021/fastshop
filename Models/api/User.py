from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from Models.ModelBase import Base,XTVARCHAR
class App(Base):
    __tablename__ = 'app'

    app_id = Column(INTEGER, primary_key=True, autoincrement=True)
    app_name=Column(XTVARCHAR(32))
    user_id=Column(BIGINT,index=True)
