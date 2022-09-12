
from typing import List,Dict,Literal, NewType,TypeAlias
from pymysql.converters import escape_string #

def filterbuilder(filters:Dict={},sep=' and ')->str:
    arr:List[str]=[]

    oprationtable={'eq':'=','gt':'>','lt':'<','gte':'>=','lte':'<=','ne':'!=','contains':'like','in':'in'}
    for keyoprator,value in filters.items():
        if not value:
            continue

        key,opration=keyoprator.split('__',1)

        if isinstance(value,list):
            newvalue=[nv if  (nv:=str(v)).isnumeric() else f"'{escape_string(v)}'" for v in value]
        elif not value.isnumeric():
            newvalue = f"'{escape_string(value)}'"
        else:
            newvalue=str(value)
        column=key.replace('__','.')
        if opration=='contains':
            if not newvalue.isnumeric():
                newvalue=newvalue[1:-1]
            newvalue=rf"'%{newvalue}%'"
        if opration in oprationtable:
            if opration=='in':
                arr.append(f"{column} {oprationtable[opration]} ({','.join(newvalue)})")
            else:
                arr.append(f"{column} {oprationtable[opration]} {newvalue}")

    return sep.join(arr)
