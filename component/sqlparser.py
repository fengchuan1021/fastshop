from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, load_only, contains_eager
from typing import Tuple, List, Any, Optional

import Models
import settings
from common import findModelByName
from component.graphqlpermission import getAuthorizedColumns

#from sqlalchemy.orm import aliased
def getmodelnamecloums(query:str)->Tuple[str,List[str],List[str]]:
    p1 = query.find('{')
    modelname = query[0:p1]
    body = query[p1 + 1:-1]
    columns = []
    joinmodel=[]
    if body == '':
        return modelname, [],[]
    else:
        tmpstr = ''
        count = 0
        flag=0
        for i in body:
            if i == ',' and count == 0:
                if flag==0:
                    columns.append(tmpstr)
                else:
                    joinmodel.append(tmpstr)
                    flag=0
                tmpstr = ''
            elif i == '{':
                tmpstr += '{'
                count += 1
                flag=1
            elif i == '}':
                tmpstr += '}'
                count -= 1
            else:
                tmpstr += i
        if tmpstr:
            if i=='}':
                joinmodel.append(tmpstr)
            else:
                columns.append(tmpstr)
        return modelname,columns,joinmodel

async def parseSQL(query:str,db: AsyncSession=None,context:Optional[settings.UserTokenData]=None,parentmodel:Any=None,statment:Any=None)->Any:#,modelarr=None
    #if modelarr==None:
    #   modelarr=[]
    modelname,columns,joinmodel=getmodelnamecloums(query)
    if parentmodel:
        realmodelname = parentmodel.__annotations__.get(modelname)
    else:
        realmodelname=modelname
    extra=[]
    if context:
        permittedcolumns,extra=await getAuthorizedColumns(db,realmodelname,context.userrole,'read')
        if permittedcolumns[0]!='*':
            if not columns:
                columns=permittedcolumns
            else:
                for c in columns:
                    if c not in permittedcolumns:
                        raise PermissionError(f"{c} not allow permission for read")


    option=None
    if None==statment:
        model = findModelByName(modelname)
        #modelarr.append(model.__name__)
        if extra:
            statment=select(model).where(text(' and '.join( [f'{modelname}.{i}={getattr(context,i)}' for i in extra] )))
        else:
            statment = select(model)
    else:
        relivatetoparent=getattr(parentmodel,modelname)

        option = contains_eager(relivatetoparent)
        #if realmodelname in modelarr:
        #    statment = statment.join(relivatetoparent.of_type(aliased(getattr(Models,realmodelname))))  # type: ignore
        #else:
            #modelarr.append(realmodelname)
        statment=statment.join(relivatetoparent)#type: ignore
    if columns:
        option=option.load_only(*columns) if option else load_only(*columns)

    childsoptions=[]
    for joint in joinmodel:

        statment,childsoption=await parseSQL(joint,db,context,model,statment)#modelarr

        if childsoption:
            childsoptions.append(childsoption)
    if childsoptions:
        if option:
            option=option.options(*childsoptions)#type: ignore
        else:
            statment=statment.options(*childsoptions)
    if not parentmodel:
        return statment if not option else statment.options(option)
    return statment,option

if __name__=='__main__':

    from component.dbsession import getdbsession
    from common import cmdlineApp
    from settings import UserTokenData


    @cmdlineApp
    async def test(db):#type: ignore
        s=select(Models.Category).join(Models.Category)
        print(s)

    test()