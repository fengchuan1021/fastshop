import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List, Any
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
from elasticsearchclient import es

class ProductSearchService():
    def __init__(self,*args:Any)->None:
        pass

    async def getproductdata(self)->None:
        pass
