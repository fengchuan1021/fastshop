from datetime import timedelta,datetime

from openapi_schema_validator._validators import nullable

import settings
from component.snowFlakeId import snowFlack
from sqlalchemy import Column, DateTime, Float, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, ENUM, INTEGER, VARCHAR,DECIMAL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple
from sqlalchemy.sql import and_, or_
from ..ModelBase import Base
from UserRole import UserRole
from sqlalchemy import select
class Warehouse(Base):
    __tablename__ = 'warehouse'


    warehouse_name = Column(VARCHAR(32),unique=True)

    company_name = Column(VARCHAR(32),nullable=True)
    company_id=Column(BIGINT,nullable=True)
    warehouse_mark=Column(VARCHAR(255),default='',server_default='')

