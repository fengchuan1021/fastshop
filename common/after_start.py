import asyncio
import os

from elasticsearch import AsyncElasticsearch
from sqlalchemy.ext.asyncio import AsyncSession

import elasticsearchclient
import settings
from Service import thirdmarketService
from component.cache import cache
from component.dbsession import getdbsession
from component.snowFlakeId import snowFlack


async def after_start(db:AsyncSession=None)->None:
    loop = asyncio.get_event_loop()
    cache.init(prefix=settings.CACHE_PREFIX, expire=settings.DEFAULT_CACHE_EXPIRE, enable=settings.ENABLE_CACHE,
               writeurl=settings.REDISURL,
               readurl=settings.SLAVEREDISURL,
               ignore_arg_types=[settings.UserTokenData],
               loop=loop
               )
    snowFlack.init(settings.NODEID)
    if db:
        await thirdmarketService.init(db)
    else:
        async with getdbsession() as db:
            await thirdmarketService.init(db)#type: ignore


    elasticsearchclient.es = AsyncElasticsearch([settings.ELASTICSEARCHURL])
