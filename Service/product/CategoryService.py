#type: ignore

from pydantic import BaseModel

import Service
from Service.base import CRUDBase
import Models
from typing import Dict
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select


class Tree(BaseModel):
    category_name: str
    category_id: int
    parent_name: str
    parent_id: int
    category_image: str

class CategoryService(CRUDBase[Models.Category]):

    async def getCategoryTree(self,db:AsyncSession)->Dict:
        root={'category_id':0,'category_name':'webroot','category_image':'','children':[]}
        arr=[root]
        async def getchildren(nodedict):
            print('nodedist:',nodedict)
            cols=[Models.Category.category_id,Models.Category.category_name,Models.Category.category_image,Models.Category.parent_id,Models.Category.parent_name]
            statment=select(*cols).filter(Models.Category.parent_id==nodedict['category_id']).order_by(Models.Category.category_order.asc())
            results=(await  db.execute(statment)).all()
            #print('result:',results.sc)
            if results:
                nodedict['children']=[child._asdict() for child in results]
                for child in nodedict['children']:
                    print('child:',child)
                    await getchildren(child)

        await getchildren(root)
        return arr


if __name__ == "__main__":
    from common.globalFunctions import cmdlineApp
    from component.dbsession import getdbsession
    @cmdlineApp
    async def testgetCategoryTree():
        async with getdbsession() as db:
            await Service.categoryService.findByPk(db,'80194405654332482')
            #tmp=await Service.categoryService.getCategoryTree(db)
            #print('tmp::',tmp)
    testgetCategoryTree()


