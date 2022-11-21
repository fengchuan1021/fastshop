

import settings
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER
from sqlalchemy.orm import relationship, backref
from .Warehouse import Warehouse
from Models.ModelBase import Base,XTVARCHAR


class Shop(Base):
    __tablename__ = 'shop'

    shop_id = Column(INTEGER, primary_key=True, autoincrement=True)
    shop_name = Column(XTVARCHAR(32),unique=True)

    lang=Column(ENUM(*[i.value for i in settings.SupportLang]),server_default='en',default='en')
    warehouse_id=Column(BIGINT,index=True)
    warehouse_name=Column(XTVARCHAR(32))
    warehouse:'Warehouse'=relationship("Warehouse",uselist=False,primaryjoin='foreign(Warehouse.warehouse_id) == Site.warehouse_id',backref=backref('sites'))
    # Variants: 'VariantSite' = relationship('VariantSite', uselist=True,
    #                                    primaryjoin='foreign(VariantSite.site_id) == Site.site_id',
    #                                    backref=backref('Site'))
