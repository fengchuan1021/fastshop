from typing import Dict, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import Service
from fastapi import UploadFile

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token

router = APIRouter()
@router.post('/uploadimg')
async def uploadimg(file: UploadFile,
    container_name: Optional[str] = 'tmp',
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
    )->Dict:
    data = await file.read()
    flag,fileurl=await Service.uploadService.uploadimg(data, container_name)#type: ignore
    if flag:
        return {'status':'success','fileurl':fileurl}
    else:
        return {'status':'failed','msg':fileurl}
