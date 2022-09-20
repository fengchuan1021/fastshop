import os
import re

import settings
import uuid
from azure.storage.blob import BlobServiceClient,BlobClient,PublicAccess
from azure.core.exceptions import ResourceNotFoundError
import Service
from azure.storage.blob import ContentSettings

class UploadService():
    async def createcontainer(self,name:str)->None:
        blob_service_client = BlobServiceClient.from_connection_string(settings.AZ_BLOB_CONNSTR)#type: ignore
        blob_service_client.create_container(name, public_access=PublicAccess.BLOB)

    async def uploadimg(self,imgata:bytes,containername:str='tmp')->str:
        containername=containername if containername.endswith(settings.MODE) else containername+settings.MODE
        uuidname=str(uuid.uuid4()) + '.jpg'
        client=BlobClient.from_connection_string(conn_str=settings.AZ_BLOB_CONNSTR, container_name=containername, blob_name=uuidname)
        try:
            CS = ContentSettings(content_type='image/jpg')
            client.upload_blob(imgata,content_settings=CS,overwrite=True,tags={"tmpimg":"1"})#type: ignore
            azurehost=re.findall(r'BlobEndpoint=(.*?);',settings.AZ_BLOB_CONNSTR)[0]
            outputhost=os.getenv('CDN_IMGHOST','') or azurehost
            return f"{outputhost}{containername}/{uuidname}"
        except ResourceNotFoundError:
            await self.createcontainer(containername)
            return await self.uploadimg(imgata,containername)




if __name__ == '__main__':
    async def testupload()->None:
        with open(r'd:\1.png','rb') as f:
            data=f.read()
            print(await Service.uploadService.uploadimg(data,'product'))

    import asyncio
    asyncio.run(testupload())