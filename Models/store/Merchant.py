from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship
from Models.ModelBase import Base, XTVARCHAR
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Models.User import User
    from ..product.Product import Product
    from ..product.Product import Variant
    from .Store import Store
    from Models.stock.Warehouse import Warehouse


class Merchant(Base):
    __tablename__ = 'merchant'
    merchant_id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, index=True)
    merchant_name = Column(XTVARCHAR(32))
    company_name = Column(XTVARCHAR(32), default='')
    company_url = Column(XTVARCHAR(32), default='')
    contacts_firstname = Column(XTVARCHAR(32), default='')
    contacts_lastname = Column(XTVARCHAR(32), default='')
    contacts_tels = Column(XTVARCHAR(32), default='')
    contacts_emial = Column(XTVARCHAR(32), default='')
    User: 'User' = relationship('User', uselist=False,
                                primaryjoin='foreign(Merchant.user_id) ==User.user_id',
                                back_populates='Merchant', cascade=''
                                )
    Product: List['Product'] = relationship('Product', uselist=True,
                                            primaryjoin='foreign(Product.merchant_id) ==Merchant.merchant_id',
                                            back_populates='Merchant', cascade=''
                                            )

    Variant: List['Variant'] = relationship('Variant', uselist=True,
                                            primaryjoin='foreign(Variant.merchant_id) ==Merchant.merchant_id',
                                            back_populates='Merchant', cascade=''
                                            )
    Store: List['Store'] = relationship('Store', uselist=True,
                                        primaryjoin='foreign(Store.merchant_id) ==Merchant.merchant_id',
                                        back_populates='Merchant', cascade=''
                                        )
    Warehouse: 'Warehouse' = relationship('Warehouse', uselist=True,
                                          primaryjoin='foreign(Warehouse.merchant_id) ==Merchant.merchant_id',
                                          back_populates='Merchant', cascade=''
                                          )  # type: ignore
    # tiktok_appid=Column(XTVARCHAR(64),default='')
    # tiktok_secret=Column(XTVARCHAR(128), default='')
    # tiktok_shopid=Column(XTVARCHAR(128),default='')
    # tiktok_token=Column(XTVARCHAR(512),default='')
    #
    # onbuy_key=Column(XTVARCHAR(64),default='')
    # onbuy_secret=Column(XTVARCHAR(64),default='')
