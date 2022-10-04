import importlib
import os
import re
from pathlib import Path
from typing import Dict

from pydantic import BaseModel
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

import Models
import settings
import uuid
from azure.storage.blob import BlobServiceClient,BlobClient,PublicAccess
from azure.core.exceptions import ResourceNotFoundError
import Service
from azure.storage.blob import ContentSettings
from collections import defaultdict

from Service import CRUDBase
from UserRole import UserRole
from common.dbsession import getdbsession
from common.filterbuilder import filterbuilder
from modules.backend.permission.PermissionShema import BackendPermissionPermissionlistGetRequest


class PermissionService(CRUDBase[Models.Permission]):
    async def getroutelist(self):
        tree={'label':'backend','children':{}}
        def addchildren(arrname,children):

            nonlocal tree
            tmppath=tree
            for name in arrname:
                if name not in tmppath['children']:
                    tmppath['children'][name]={'label':name,'children':{}}
                    tmppath=tmppath['children'][name]
            tmppath['children']=children
        for f in Path(settings.BASE_DIR).joinpath('modules', 'backend').rglob('*.py'):
            if f.__fspath__().endswith('Controller.py'):
                filepath=f.relative_to(Path(settings.BASE_DIR).joinpath('modules', 'backend')).with_suffix('').__str__()
                arr=filepath.split('\\')
                #*tmparr,controllername=arr


                controller = importlib.import_module(
                    str(f.relative_to(settings.BASE_DIR)).replace(os.sep, '.')[0:-3]

                )
                addchildren(arr,{i:route.name for i,route in enumerate(controller.router.routes)})

        return tree

    async def setUserRolePermission(self,db:AsyncSession,roleid:int,apis:str):
        sql = insert(Models.Permission).prefix_with("ignore").values([{'role_id': roleid,'role_name':UserRole(roleid).name,'api_name':api} for api in apis])
        await db.execute(sql)

    async def getrolepermissionlist(self,db:AsyncSession,pagenum:int=1,pagesize:int=30,filter:BaseModel | Dict={}):

        where,params=filterbuilder(filter)
        statment=select(Models.Permission).where(text(where))
        result=await db.execute(statment,params)
        print(result.scalars().all())
        pass

if __name__ == '__main__':
    from modules.backend.permission.PermissionShema import BackendPermissionPermissionlistGetRequest,Filter
    async def testfilter()->None:
        async with getdbsession() as db:
            filter= {"role_id__eq":4}

            #await Service.permissionService.getrolepermissionlist(db,filter=filter)


            results,total=await Service.permissionService.pagination(db, filter=filter)
            print(results)
            print(total)
    import asyncio
    asyncio.run(testfilter())