from typing import Dict

from fastapi import APIRouter
import Service
from fastapi import FastAPI, File, UploadFile
router = APIRouter()
@router.post('/uploadimg')
async def uploadimg(file: UploadFile)->Dict:
    data = await file.read()
    flag,fileurl=await Service.uploadService.uploadimg(data, 'product')
    if flag:
        return {'status':'success','fileurl':fileurl}
    else:
        return {'status':'failed','msg':fileurl}
