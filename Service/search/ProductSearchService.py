import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List, Any
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from XTTOOLS import filterbuilder

from sqlalchemy.orm import undefer_group

from sqlalchemy import select,text
from XTTOOLS import cache

from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from elasticsearchclient import es
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q,Search
class ProductSearchService():
    def __init__(self,*args:Any)->None:
        pass

    async def getproductdata(self)->None:
        pass

if __name__=='__main__':
    s = Search()
    a=MultiMatch(query='python django', fields=['title', 'body'])
    a= Q('bool', must=[Q('match', title='python'), Q('match', body='best')])
    s = Search()
    s = s.filter('terms', tags=['search', 'python']).query(a).post_filter("terms",colour=['blue','red'])
    print(s.to_dict())
    pass