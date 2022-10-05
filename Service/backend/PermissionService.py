import importlib
import os

from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

import Models
import settings

import Service


from Service import CRUDBase
from UserRole import UserRole

from common.filterbuilder import filterbuilder

from component.cache import cache


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

    def getrolemenucachekey(self,func,func_args,func_annotations):
        return f"{cache.get_prefix()}:rolemenu:{func_args.arguments.get('roleid')}"
    @cache(key_builder='getrolemenucachekey')
    async def getroledisplayedmenu(self,db:AsyncSession,roleid:int)->List[Models.Roledisplayedmenu]:
        role_ids = []
        tmpid = roleid
        j = 1
        while tmpid:
            if tmpid & j:
                role_ids.append(j)
                tmpid -= j
            j *= 2

        statment = select(Models.Roledisplayedmenu).where(Models.Roledisplayedmenu.role_id.in_(role_ids))
        result = (await db.execute(statment)).scalars().all()
        return result

if __name__ == '__main__':
    #from modules.backend.permission.PermissionShema import BackendPermissionPermissionlistGetRequest,Filter


    from common.dbsession import getdbsession
    async def testfilter()->None:
        async with getdbsession() as db:
            filter= {"role_id__eq":4}

            #await Service.permissionService.getrolepermissionlist(db,filter=filter)


            results,total=await Service.permissionService.pagination(db, filter=filter)
            print(results)
            print(total)
    import asyncio
    asyncio.run(testfilter())