import importlib
import os

from pathlib import Path
from typing import Dict, List, Any

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

import Models
import settings

import Service


from Service import CRUDBase


from component.cache import cache


class PermissionService(CRUDBase[Models.Permission]):
    async def getroutelist(self,*args:Any)->Dict:
        tree={'label':'backend','children':{},'key':'backend'}
        def addchildren(arrname:Any,children:Any)->None:

            nonlocal tree
            tmppath=tree
            for name in arrname:
                if name not in tmppath['children']:
                    tmppath['children'][name]={'label':name,'children':{}}#type: ignore
                    tmppath=tmppath['children'][name]#type: ignore
            tmppath['children']=children
        for f in Path(settings.BASE_DIR).joinpath('modules', 'backend').rglob('*.py'):
            if f.__fspath__().endswith('Controller.py'):
                filepath=f.relative_to(Path(settings.BASE_DIR).joinpath('modules', 'backend')).with_suffix('').__str__()
                arr=filepath.split('\\')
                #*tmparr,controllername=arr

                _filename=str(f.relative_to(settings.BASE_DIR)).replace(os.sep, '.')[0:-3]
                controller = importlib.import_module(_filename)
                #addchildren(arr,{i:route.name for i,route in enumerate(controller.router.routes)})
                addchildren(arr, {route.name: {'label':route.name,'key':f'{_filename.replace("modules.","")}.{route.name}'} for route in controller.router.routes})
                #addchildren(arr,{0:[{'label':route.name} for route in controller.router.routes]})
        return tree

    async def setUserRolePermission(self,db:AsyncSession,roleid:int,apis:List[str])->None:
        rolemodel=await Service.roleService.findByPk(db,roleid)
        oldpermissions=await self.getList(db,filters={'roleid':roleid})
        for oldpermission in oldpermissions:
            if oldpermission.api_name not in apis:
                await db.delete(oldpermission)
        sql = insert(Models.Permission).prefix_with("ignore").values([{'role_id': roleid,'role_name':rolemodel.role_name,'api_name':api} for api in apis])
        await db.execute(sql)



    def getrolemenucachekey(self,func,func_args,func_annotations)->str:#type: ignore
        return f"{cache.get_prefix()}:rolemenu:{func_args.arguments.get('roleid')}"
    @cache(key_builder='getrolemenucachekey')#type: ignore
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
    async def setRoleDisplayedMenu(self,db:AsyncSession,role_id:int,menus:List[str]=[])->None:
        rolemodel=await Service.roleService.findByPk(db,role_id)
        role_name = rolemodel.role_name
        newmenu = []
        def addparentmenu(path:str)->None:
            nonlocal newmenu
            parent, _ = path.rsplit('/', 1)
            if parent:
                newmenu.append(parent)
                addparentmenu(parent)

        if menus:
            newmenu = menus.copy()
            for m in menus:
                addparentmenu(m)

        sqloldmenus = select(Models.Roledisplayedmenu).filter(Models.Roledisplayedmenu.role_id == role_id)
        results = (await db.execute(sqloldmenus)).scalars().all()
        for result in results:
            if result.menu_path not in newmenu:
                await db.delete(result)

        sql = insert(Models.Roledisplayedmenu).prefix_with('ignore').values(
            [{'role_id': role_id, 'role_name': role_name, 'menu_path': menu_path} for menu_path in newmenu])
        await db.execute(sql)
        print('delet:',f"{cache.get_prefix()}:rolemenu:{role_id}")
        await cache.delete(f"{cache.get_prefix()}:rolemenu:{role_id}")
if __name__ == '__main__':
    #from modules.backend.permission.PermissionShema import BackendPermissionPermissionlistGetRequest,Filter


    from component.dbsession import getdbsession
    async def testfilter()->None:
        async with getdbsession() as db:
            filter= {"role_id__eq":4}

            results=await Service.permissionService.getroutelist(db)


            #results,total=await Service.permissionService.pagination(db, filter=filter)
            print(results)
            #print(total)
    import asyncio
    asyncio.run(testfilter())