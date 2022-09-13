import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from common.filterbuilder import filterbuilder

from sqlalchemy.orm import undefer_group

from sqlalchemy import select,text
from component.cache import cache

from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
es=AsyncElasticsearch()

class ProductSearchService():
    def __init__(self,*args):
        pass

    async def getproductdata(self):
        pass
    resp=await async_bulk(es,getproductdata())