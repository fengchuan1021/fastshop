from sqlalchemy import select
from sqlalchemy.orm import joinedload, load_only
from typing import Tuple, List, Any
from sqlalchemy.sql.selectable import Select
import Models
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

def parseSQL(query:str,parentmodel:Any=None)->Any:
    modelname,columns,joinmodel=getmodelnamecloums(query)
    model = getattr(Models, modelname)
    if parentmodel==None:

        statment=select(model)
    else:
        statment=joinedload(getattr(parentmodel,modelname))#type: ignore

    if columns:
        statment=statment.options(load_only(*columns))
    for joint in joinmodel:
        joinstatment=parseSQL(joint,model)
        statment=statment.options(joinstatment)
    return statment