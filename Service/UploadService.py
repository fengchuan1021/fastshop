import os
import re
from typing import Tuple, Optional

import settings
import uuid
from azure.storage.blob import BlobServiceClient,BlobClient,PublicAccess
from azure.core.exceptions import ResourceNotFoundError
import Service
import datetime
from azure.storage.blob import ContentSettings
from pathlib import Path
class UploadService():
    async def storelocal(self,imgdata:bytes,containername:str='tmp')->Tuple[int,str]:
        try:
            dir=Path(settings.BASE_DIR).joinpath('img',containername,datetime.datetime.now().strftime("%Y-%m-%d"))
            dir.mkdir(parents=True, exist_ok=True)
            uuidname = str(uuid.uuid4()) + '.jpg'
            filepath=dir.joinpath(uuidname)
            with open(str(filepath),'wb') as f:
                f.write(imgdata)
            return 1,os.getenv('LOCAL_IMG_HOST','')+str(filepath.relative_to(settings.BASE_DIR)).replace('\\','/')
        except Exception as e:
            return 0,str(e)

    async def createcontainer(self,name:str)->None:
        blob_service_client = BlobServiceClient.from_connection_string(settings.AZ_BLOB_CONNSTR)#type: ignore
        blob_service_client.create_container(name, public_access=PublicAccess.BLOB)

    async def storeazure(self,imgata:bytes,containername:str='tmp')->Tuple[int,str]:
        containername=containername if containername.endswith(settings.MODE) else containername+settings.MODE
        uuidname=str(uuid.uuid4()) + '.jpg'
        client=BlobClient.from_connection_string(conn_str=settings.AZ_BLOB_CONNSTR, container_name=containername, blob_name=uuidname)
        try:
            CS = ContentSettings(content_type='image/jpg')
            client.upload_blob(imgata,content_settings=CS,overwrite=True,tags={"tmpimg":"1"})#type: ignore
            azurehost=re.findall(r'BlobEndpoint=(.*?);',settings.AZ_BLOB_CONNSTR)[0]
            outputhost=os.getenv('CDN_IMGHOST','') or azurehost
            return 1,f"{outputhost}{containername}/{uuidname}"
        except ResourceNotFoundError:
            await self.createcontainer(containername)
            return await self.uploadimg(imgata,containername)
        except Exception as e:

            return 0,str(e)

    async def uploadimg(self,imgata:bytes,containername:str='tmp')->Tuple[int,str]:
        if not settings.AZ_BLOB_CONNSTR:#store in localdriver if not has azure storage key
            return await self.storelocal(imgata,containername)
        else:
            return await self.storeazure(imgata,containername)
