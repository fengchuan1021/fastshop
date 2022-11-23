from sqlalchemy import select
from sqlalchemy.orm import joinedload, load_only, contains_eager
from typing import Tuple, List, Any
from sqlalchemy.sql.selectable import Select
import Models
def getmodelnamecloums(query:str)->Tuple[str,List[str],List[str]]:
    p1 = query.find('{')
    modelname = query[0].upper()+query[1:p1]
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

def parseSQL(query:str,parentmodel:Any=None,statment:Any=None)->Any:
    modelname,columns,joinmodel=getmodelnamecloums(query)
    model = getattr(Models, modelname)
    option=None
    if None==statment:
        statment=select(model)
    else:
        relivatetoparent=getattr(parentmodel,modelname)
        option=contains_eager(relivatetoparent)
        statment=statment.join(relivatetoparent)#type: ignore
    if columns:
        option=option.load_only(*columns) if option else load_only(*columns)
    childsoptions=[]
    for joint in joinmodel:
        statment,childsoption=parseSQL(joint,model,statment)
        if childsoption:
            childsoptions.append(childsoption)
    if childsoptions and option:
        option=option.options(*childsoptions)#type: ignore
    if not parentmodel:
        return statment if not option else statment.options(option)
    return statment,option