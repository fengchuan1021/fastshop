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
from component.fastQL import fastQuery,fastAdd,fastDel
from component.sqlparser import parseSQL
import orjson
router = APIRouter()

@router.post('/graphql/{modelname:str}')
async def create(modelname:str,body:Dict=Body(...),
           db: AsyncSession = Depends(get_webdbsession),
           token: settings.UserTokenData = Depends(get_token),
           )->Any:
    await fastAdd(db,modelname,body,token)
    return {'status': 'success'}

    # if service:=getattr(Service,modelname+'Service',None):
    #     await service.create(db,body)
    #     await db.commit()
    #     return {'status':'success'}
    # else:
    #     return Common500Response(status='validateerror',msg='model no exists')

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


class InShema(BaseModel):
    query:str
    id:Optional[int]=0
    pagesize: Optional[int] =0
    pagenum: Optional[int] =0
    filter: Optional[Dict] = {}
    orderby:str=''
    returntotal:bool=False
#queryparams:InShema=InShema(),

@router.post('/graphql')
async def postquery(
        inshema:InShema,
        db: AsyncSession = Depends(get_webdbsession),
        token: settings.UserTokenData = Depends(get_token),
)->Any:

    if inshema.id:
        modelname=inshema.query if (pos:=inshema.query.find('{'))==-1 else inshema.query[0:pos]
        _filter[f'{modelname.lower()}_id']=id#type: ignore
    result=await fastQuery(db,inshema.query,inshema.filter,inshema.pagenum,inshema.pagesize,inshema.orderby,inshema.returntotal,token,id)
    if id:
        return CommonResponse(status='success',data=result)
    if inshema.returncount:
        return CommonResponse(status='success',data=result[0],total=result[1])
    else:
        return CommonResponse(status='success',data=result)


@router.get('/graphql/{query:str}/{id:int}')
@router.get('/graphql/{query:str}')
async def get(query:str,id:int=0,pagenum:int=0,pagesize:int=0,orderby:str='',returntotal:bool=False,filter:str='{}',
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:
    _filter=orjson.loads(filter if filter else '{}')
    if id:
        modelname=query if (pos:=query.find('{'))==-1 else query[0:pos]
        _filter[f'{modelname.lower()}_id']=id#type: ignore
    result=await fastQuery(db,query,_filter,pagenum,pagesize,orderby,returntotal,token,id)
    if id:
        return CommonResponse(status='success',data=result)
    if returntotal:
        return CommonResponse(status='success',data=result[0],total=result[1])
    else:
        return CommonResponse(status='success',data=result)

@router.delete('/graphql/{modelname:str}/{id:str}')
async def delete(modelname:str,id:str,
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:
    status=await fastDel(db,modelname,id,token)
    if status:
        return {'status':'success'}
    else:
        return Common500Response(status='validateerror',msg='model no exists')
