from typing import Any, Dict, Optional

from sqlalchemy import text, func
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import filterbuilder, PermissionException, findModelByName
from component.sqlparser import parseSQL
from typing import List
from component.cache import cache
@cache
async def getAuthorizedColumns(db:AsyncSession,modelname:str,role:int,method:str='read')->Any:
    permission=Service.graphpermissionService.getList(db,filter={"model_name":modelname,"role_id":role})

    columns=getattr(permission,f'{method}_columns')
    extra=getattr(permission,f'{method}_extra')
    return columns.split(',') if columns else [],extra.split(',') if extra else []

async def fastQuery(db: AsyncSession,
           query:str,
           filter:Dict={},
           pagenum:int=0,
           pagesize:int=0,
           orderby:str='',
           returntotal:bool=False,
           context:Optional[settings.UserTokenData]=None,
           returnsingleobj:bool=False,
            )->Any:
    if query[-1] != '}':
        query = query + '{}'

    where, params = filterbuilder(filter)
    statment=parseSQL(query).where(text(where))
    total=None
    if returntotal:
        count_statment=statment.with_only_columns([func.count()],maintain_column_froms=True)
        total=(await db.execute(count_statment,params)).scalar()
    if pagesize and pagenum:
        statment=statment.offset((pagenum-1)*pagesize).limit(pagesize)
    if orderby:
        statment=statment.order_by(text(orderby))

    results=await db.execute(statment,params)
    data=results.scalars().all()

    if returnsingleobj:
        return data[0] if data else None
    if returntotal==False:
        return data
    return data,total



async def fastAdd(db: AsyncSession,modelname:str,data:Dict,context:Optional[settings.UserTokenData]=None)->Any:
    '''context 来指定用什么用户角色来添加数据'''
    '''比如用root用户执行函数 context 里边userrole为商家 即以商家角色添加数据'''
    '''getAuthorizedColumns去权限表里边查找商家能读取/写入的字段'''
    columns=['*']
    extra=[]
    allpermission = False
    if context:
        columns,extra=await getAuthorizedColumns(db,modelname,context.userrole,method='write')
    if '*' in columns:
        allpermission=True

    dic={}
    children=[]
    _lowerrelation=[i.lower() for i in columns if 'A'<=i[0]<='Z']
    for key,value in data.items():

        if isinstance(value,(dict,list)):
            if not allpermission and key.lower() not in _lowerrelation:
                raise PermissionException(f"not permission access {key}")
            children.append(key)
        else:
            if not allpermission and key not in columns:
                raise PermissionException(f"not permission access {key}")
            dic[key]=value
    model=findModelByName(modelname)
    if context:
        dic.update({i:getattr(context,i) for i in extra})
    db.add(model(**dic))
    await db.flush()
    for child in children:
        if isinstance(data[child],dict):
            data[child][modelname+"_id"]=model.id
            await fastAdd(db, child,data[child], context)
        else:
            for tmpdata in data[child]:
                await fastAdd(db,child,tmpdata, context)
async def fastDel(db: AsyncSession,modelname:str,id:int=0,context:Optional[settings.UserTokenData]=None)->Any:

    extra=[]
    if context:
        columns,extra=await getAuthorizedColumns(db,modelname,context.userrole,method='delete')
        if columns[0]!='Y':
            return False #no permission

    if service := getattr(Service, modelname + 'Service', None):
        await service.deleteByPk(db, id,{i:getattr(context,i) for i in extra})
        return {'status': 'success'}
    else:
        return False



