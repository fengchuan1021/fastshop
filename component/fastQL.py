from typing import Any, Dict, Optional

from sqlalchemy import text, func
from sqlalchemy.ext.asyncio import AsyncSession

from common import filterbuilder
from component.sqlparser import parseSQL

class DotMap:
    def __init__(self,data:Any,total:Optional[int]=None)->None:
        '''data: result
        total: total len of result
        '''
        self.data=data
        self.total=total

async def fastQL(db: AsyncSession,
           query:str,
           id:int=0,
           pagenum:int=0,
           pagesize:int=0,
           orderby:str='',
           returntotal:bool=False,
           filter:Dict={},
            )->Any:
    if query[-1] != '}':
        query = query + '{}'
    if id:
        _filter[f'{modelname.lower()}_id']=id#type: ignore

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
    if id:
        return DotMap(data[0] if data else None,None)
    return DotMap(data,total)