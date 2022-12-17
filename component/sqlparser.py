from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, load_only, contains_eager
from typing import Tuple, List, Any, Optional
from sqlalchemy.sql.selectable import Select
import Models
import settings
from common import findModelByName
from component.graphqlpermission import getAuthorizedColumns


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

async def parseSQL(query:str,db: AsyncSession=None,context:Optional[settings.UserTokenData]=None,parentmodel:Any=None,statment:Any=None)->Any:
    modelname,columns,joinmodel=getmodelnamecloums(query)
    extra=[]
    if context:
        permittedcolumns,extra=await getAuthorizedColumns(db,modelname,context.userrole,'read')
        if permittedcolumns[0]!='*':
            if not columns:
                columns=permittedcolumns
            else:
                for c in columns:
                    if c not in permittedcolumns:
                        raise PermissionError(f"{c} not allow permission for read")

    model = findModelByName(modelname)
    option=None
    if None==statment:
        if extra:
            statment=select(model).where(text(' and '.join( [f'{modelname}.{i}={getattr(context,i)}' for i in extra] )))
        else:
            statment = select(model)
    else:
        relivatetoparent=getattr(parentmodel,model.__name__)

        option=contains_eager(relivatetoparent)

        statment=statment.join(relivatetoparent)#type: ignore
    if columns:
        option=option.load_only(*columns) if option else load_only(*columns)

    childsoptions=[]
    for joint in joinmodel:

        statment,childsoption=await parseSQL(joint,db,context,model,statment)

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
    async def test():#type: ignore
        async with getdbsession() as db:
            print(await parseSQL("Store{appid,Market{market_url}}",db,context=UserTokenData(userrole=2,merchant_id=1)))
    test()