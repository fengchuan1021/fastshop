
from typing import List, Dict, Literal, NewType, TypeAlias, Optional, Tuple
from pymysql.converters import escape_string #
from pydantic import BaseModel
def filterbuilder(filters:Dict | BaseModel,sep:str=' and ')->Tuple[str,Dict]:
    if not filters:
        return '',{}
    if type(filters)==dict:
        pass
    else:
        filters=filters.dict(exclude_unset=True,exclude_none=True) #type: ignore

    arr:List[str]=[]
    params={}
    oprationtable={'eq':'=','gt':'>','lt':'<','gte':'>=','lte':'<=','ne':'!=','contains':'like','in':'in'}
    for keyoprator,value in filters.items():
        if value==None:
            continue
        tmp=keyoprator.rsplit('__',1)
        if len(tmp)==2:
            key,opration=tmp
        else:
            key=tmp[0]
            opration='eq'

        column=key.replace('__','.')

        if opration in oprationtable:
            if opration=='in':
                arr.append(f"{column} {oprationtable[opration]} (:{key})")
                params[key]=','.join([str(v) for v in value])
            elif opration=='contains':
                arr.append(f"{column} {oprationtable[opration]} :{key}")
                params[key] = f"%{value}%"
            else:
                arr.append(f"{column} {oprationtable[opration]} :{key}")
                params[key]=value

    return sep.join(arr),params
