from fastapi import UploadFile

from fastapi import APIRouter

router=APIRouter(prefix='/apidesign')

from devtools.generatefromopenapi import mymain
@router.post('/importapifox')
async def importfromapifox(file: UploadFile)->None:
    contents = await file.read()
    mymain(contents)
