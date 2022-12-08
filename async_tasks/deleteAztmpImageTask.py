import os

from celery_app import celery_app
from common.globalFunctions import cmdlineApp
from component.cache import cache
from azure.storage.blob import BlobServiceClient
import time
from collections import defaultdict

@celery_app.task
@cmdlineApp
async def deleteAztmpfile():#type: ignore
    tm=int(time.time())
    files=await cache.redis.zrange('aztmpfiles',0,tm)
    print(f'{files=}')
    dl=defaultdict(list)
    for f in files:
        container_name,file_name=f.decode().split('/',1)
        dl[container_name].append(file_name)
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    for container_name in dl:

        print(f'{container_name=}')
        print(f'{dl[container_name]=}')
        container_client = blob_service_client.get_container_client(container_name)
        container_client.delete_blobs(*(dl[container_name]),delete_snapshots='include')


# @celery_app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs)->None:  # type: ignore
#     sender.add_periodic_task(10, deleteAztmpfile.s(), name='deleteAztmpfile')

# async def test():

#     await cache.redis.zadd('xxx',{'1':1,'2':3})
# loop=asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(test())
#deleteAzfile('productimage',['1813b157-b4b0-405e-81b6-b7de329cdbe4.jpg', '1813b157-b4b0-405e-81b6-b7de329cdbe4_100*100.jpg', '1813b157-b4b0-405e-81b6-b7de329cdbe4_50*50.jpg'])
