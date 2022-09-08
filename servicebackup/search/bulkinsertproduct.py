#type: ignore
import asyncio
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
es=AsyncElasticsearch()

async def insertallproducts():
    async def getproductdata():
        pass
    resp=await async_bulk(es,getproductdata())