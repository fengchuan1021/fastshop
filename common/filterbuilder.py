
from typing import List, Dict, Literal, NewType, TypeAlias, Optional, Tuple

from pydantic import BaseModel
def filterbuilder(filters:Optional[Dict | BaseModel],sep:str=' and ')->Tuple[str,Dict]:
    if not filters:
        return '',{}
    if type(filters)==dict:
        pass
    else:
        filters=filters.dict(exclude_unset=True,exclude_none=True) #type: ignore

    arr:List[str]=[]
    params={}
    n=0
    oprationtable={'eq':'=','gt':'>','lt':'<','gte':'>=','lte':'<=','ne':'!=','contains':'like','in':'in'}
    for keyoprator,value in filters.items():
        n+=1
        bindparamname=f'params{n}'
        if value==None:
            continue
        tmp=keyoprator.rsplit('__',1)
        if len(tmp)==2:
            column,opration=tmp
        else:
            column=tmp[0]
            opration='eq'

        #column=key.replace('__','.')

        if opration in oprationtable:
            if opration=='in':
                if not value:
                    continue
                arr.append(f"{column} {oprationtable[opration]} ({','.join([':params%d' % (n+i) for i in range(len(value))])})")
                for i,v in enumerate(value):
                    params[f'params{n+i}']=v# if isinstance(v,int) else f"'{v}'"

                n+=i
            elif opration=='contains':
                arr.append(f"{column} {oprationtable[opration]} :{bindparamname}")
                params[bindparamname] = f"%{value}%"
            else:
                arr.append(f"{column} {oprationtable[opration]} :{bindparamname}")
                params[bindparamname]=value

    return sep.join(arr),params
