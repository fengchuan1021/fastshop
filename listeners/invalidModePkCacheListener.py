import asyncio
import settings
import Models
from common.globalFunctions import get_token
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from common.dbsession import getdbsession
import Broadcast
import asyncio
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from component.cache import cache

@Broadcast.AfterModelUpdated('*',background=True)
async def invalidmodelpkcache(model:Models.ModelType,db: AsyncSession,token:settings.UserTokenData,reason:str='')->None:

    key=f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
    await cache.delete(key)
