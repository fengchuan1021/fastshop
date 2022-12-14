
from sqlalchemy.orm import deferred, relationship, backref
import enum
from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, TEXT, DECIMAL,DATETIME,BOOLEAN
from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List

class WishProduct(Base):
    __tablename__ = 'wishproduct'
    name=Column(XTVARCHAR(128))
    wishproduct_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    market_product_id=Column(XTVARCHAR(32),unique=True,index=True)
    subcategory_id=Column(XTVARCHAR(32),default='')
    market_updatetime=Column(DATETIME(fsp=3))
    created_at=Column(DATETIME(fsp=3))
    num_sold=Column(INTEGER)
    category=Column(XTVARCHAR(250))
    is_promoted=Column(BOOLEAN,default=False)
    status=Column(XTVARCHAR(32))
    description=Column(TEXT)
    tags=Column(XTVARCHAR(255))
    num_saves=Column(INTEGER)
    is_csp_enabled=Column(BOOLEAN,default=False)
    extra_images=Column(XTVARCHAR(512))
    category_experience_eligibility=Column(BOOLEAN,default=False)
    parent_sku=Column(XTVARCHAR(80))
    california_prop65_chemical_names=Column(XTVARCHAR(128))
    main_image=Column(XTVARCHAR(512))
    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)



class WishVariant(Base):
    __tablename__ = 'wishvariant'
    wishvariant_id=Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    wishproduct_id=Column(BIGINT,index=True)
    status=Column(XTVARCHAR(32))
    sku=Column(XTVARCHAR(80))
    market_product_id=Column(XTVARCHAR(32))
    market_variant_id = Column(XTVARCHAR(32), unique=True, index=True)
    price=Column(DECIMAL(10,4))
    currency_code=Column(XTVARCHAR(12))
    cost_price=Column(DECIMAL(10,4))
    cost_currency_code = Column(XTVARCHAR(12))
    gtin=Column(XTVARCHAR(32))

    merchant_id=Column(INTEGER,index=True)
    store_id=Column(INTEGER,index=True)
    warehouse_id=Column(XTVARCHAR(32)) #在wish上的仓库id
    inventory=Column(INTEGER,default=0)#在wish上的仓库库存
    WishProduct:'WishProduct'=relationship('WishProduct',uselist=False,primaryjoin="foreign(WishVariant.wishproduct_id)==WishProduct.wishproduct_id")
