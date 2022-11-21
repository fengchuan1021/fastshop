from __future__ import annotations
from typing import Any, Dict, Optional
from fastapi import APIRouter, Depends,Body

from pydantic import BaseModel
from sqlalchemy import text, func
from sqlalchemy.ext.asyncio import AsyncSession
import Service
import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import Common500Response, CommonResponse, filterbuilder
from component.fastQL import fastQL
from component.sqlparser import parseSQL
import orjson
router = APIRouter()

@router.post('/graphql/{modelname:str}')
async def create(modelname:str,body:Dict=Body(...),
           db: AsyncSession = Depends(get_webdbsession),
           token: settings.UserTokenData = Depends(get_token),
           )->Any:
    if service:=getattr(Service,modelname+'Service',None):
        await service.create(db,body)
        await db.commit()
        return {'status':'success'}
    else:
        return Common500Response(status='validateerror',msg='model no exists')

@router.patch('/graphql/{modelname:str}/{id:str}')
async def update(modelname:str,id:str,body:Dict=Body(...),
           db: AsyncSession = Depends(get_webdbsession),
           token: settings.UserTokenData = Depends(get_token),
           )->Any:
    if service:=getattr(Service,modelname+'Service',None):

        await service.updateByPk(db,id,body)
        await db.commit()
        return {'status':'success'}
    else:
        return Common500Response(status='validateerror',msg='model no exists')


# class InShema(BaseModel):
#     query:Optional[str]=''
#     pagesize: Optional[int] =None
#     pagenum: Optional[int] =None
#     filter: Optional[Dict] = {}
#     orderby:str=''
#     returncount:bool=False
#queryparams:InShema=InShema(),


@router.get('/graphql/{query:str}/{id:int}')
@router.get('/graphql/{query:str}')
async def get(query:str,id:int=0,pagenum:int=0,pagesize:int=0,orderby:str='',returntotal:bool=False,filter:str='{}',
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:
    _filter=orjson.loads(filter)
    result=fastQL(db,query,id,filter,pagenum,pagesize,orderby,returntotal,token,False)
    return CommonResponse(status='success',data=result.data,total=result.total)

@router.delete('/graphql/{modelname:str}/{id:str}')
async def delete(modelname:str,id:str,
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:
    if service:=getattr(Service,modelname+'Service',None):
        model=await service.deleteByPk(db,id)
        return {'status':'success'}
    else:
        return Common500Response(status='validateerror',msg='model no exists')
