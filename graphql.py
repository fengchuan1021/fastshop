from __future__ import annotations
from typing import Any, Dict, Optional
from fastapi import APIRouter, Depends,Body
from sqlalchemy.ext.asyncio import AsyncSession
import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import cache,snowFlack,Common500Response, TokenException, PermissionException,XTJsonResponse,CommonQueryShema,CommonResponse

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

@router.get('/graphql/{modelname:str}/{id:str}')
async def retrive(modelname:str,id:str,field:str='*',
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:

    if service:=getattr(Service,modelname+'Service',None):
        model=await service.findByPk(db,id)
        return {'status':'success','data':model}
    else:
        return Common500Response(status='validateerror',msg='model no exists')


@router.get('/graphql/{modelname:str}')
async def lists(modelname:str,queryparams:CommonQueryShema=CommonQueryShema(),
            db: AsyncSession = Depends(get_webdbsession),
            token: settings.UserTokenData = Depends(get_token),
            )->Any:

    if service:=getattr(Service,modelname+'Service',None):
        result,total=await service.pagination(db,calcTotalNum=True,**queryparams.dict())
        return {'status':'success','data':result,'total':total}
    else:
        return Common500Response(status='validateerror',msg='model no exists')

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
