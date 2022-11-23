from typing import Any, Dict, Optional

from sqlalchemy import text, func
from sqlalchemy.ext.asyncio import AsyncSession

import settings
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
           filter:Dict={},
           pagenum:int=0,
           pagesize:int=0,
           orderby:str='',
           returntotal:bool=False,
           token:Optional[settings.UserTokenData]=None,
           permissioncheck:bool=False,
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
