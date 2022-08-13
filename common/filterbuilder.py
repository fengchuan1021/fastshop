
from typing import List,Dict,Literal, NewType,TypeAlias
from pymysql.converters import escape_string #

def filterbuilder(filter:list=[])->str:
    arr:List[str]=[]

    oprationtable={'eq':'=','gt':'>','lt':'<','gte':'>=','lte':'<=','ne':'!=','contains':'like'}
    for item in filter:
        if not item:
            continue
        print('item:',item)
        key,value=item.split('=',1)
        if not value.isnumeric():
            value = f"'{escape_string(value)}'"

        #user.name__eq 'fengchuan'
        column,opration=key.rsplit('__',1)
        column=column.replace('__','.')
        if opration=='contains':
            if not value.isnumeric():
                value=value[1:-1]
            value=rf"'%{value}%'"
        if opration in oprationtable:
            arr.append(f"{column} {oprationtable[opration]} {value}")
        elif opration=='mlike':
            _columns=column.split('|')
            _arr=[]
            if not value.isnumeric():
                value=value[1:-1]
            value=rf"'%{value}%'"
            for _column in _columns:
                _arr.append(f"{_column} like {value}")
            _value=f' ({" or ".join(_arr)}) '
            arr.append(_value)

    return ' and '.join(arr)
