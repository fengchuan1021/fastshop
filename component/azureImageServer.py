import os, uuid
import datetime
import time

from fastapi import APIRouter, UploadFile, Query
import cv2
import numpy as np
import settings
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__, PublicAccess

from component.cache import cache
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)#type: ignore
for containername in settings.AZCONTAINER_NAMES.__args__:#type: ignore
    try:
        container_client = blob_service_client.get_container_client(containername)
        container_client.get_container_properties()
    except Exception as e:
        container_client = blob_service_client.create_container(containername, public_access=PublicAccess.BLOB)



async def upload(imgbyte: bytes,container_name:str='commonfile',astmpfile:bool=False):#type: ignore
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)#type: ignore
    mainfilename = str(uuid.uuid4()) + ".jpg"
    filenames = [container_name+'/'+mainfilename]
    if container_name in settings.AZCONTAINER_CONFIG:

        nparr = np.frombuffer(imgbyte, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print('resize?')
        for w,h in settings.AZCONTAINER_CONFIG[container_name]['resize']:
            print('resize?111')
            tmpimg=cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
            tmpfilename=f'{mainfilename[0:-4]}_{w}*{h}.jpg'
            try:
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=tmpfilename)
                blob_client.upload_blob(tmpimg.tobytes())
                filenames.append(container_name+'/'+tmpfilename)
            except Exception as e:
                print(e)
                pass
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=mainfilename )
        blob_client.upload_blob(imgbyte)
    except Exception as e:
        return {'status':'failed','msg':str(e)}
    finally:
        if astmpfile:
            tomorrow = int(time.time()) + 3600*24
            mapdata={f:tomorrow for f in filenames}
            await cache.redis.zadd('aztmpfiles',mapdata)

    return {'url':f'{os.getenv("azimgserver")}/{container_name}/{mainfilename}','status':'success'}
