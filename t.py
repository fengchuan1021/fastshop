#type: ignore
import asyncio

from sqlalchemy import select

from sqlalchemy.ext.serializer import loads, dumps

from Models.productModels.Product import Product
from common.dbsession import getdbsession
from sqlalchemy.orm.state import InstanceState
from sqlalchemy.orm import instrumentation
import Models
from common.globalFunctions import toJson
import datetime
async def test():
    async with getdbsession() as db:
        t=b'\x80\x05\x95\x1a\x02\x00\x00\x00\x00\x00\x00\x8c\x1cModels.productModels.Product\x94\x8c\x07Product\x94\x93\x94)\x81\x94}\x94(\x8c\x12_sa_instance_state\x94\x8c\x14sqlalchemy.orm.state\x94\x8c\rInstanceState\x94\x93\x94)\x81\x94}\x94(\x8c\x08instance\x94h\x03\x8c\x0fcommitted_state\x94}\x94\x8c\x03key\x94h\x02K\x02\x85\x94N\x87\x94\x8c\x0cload_options\x94\x8f\x94\x8c\x06class_\x94h\x02\x8c\x12expired_attributes\x94\x8f\x94\x8c\tload_path\x94]\x94h\x02N\x86\x94a\x8c\x07manager\x94\x8c\x1esqlalchemy.orm.instrumentation\x94\x8c\x11_SerializeManager\x94\x93\x94)\x81\x94}\x94h\x13h\x02sbub\x8c\x15productDescription_en\x94\x8c\x1aenglish productdescription\x94\x8c\x05price\x94N\x8c\ncreated_at\x94\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xe6\t\x0c\x0b(4\x00\x00\x00\x94\x85\x94R\x94\x8c\nupdated_at\x94h%C\n\x07\xe6\t\x0c\x0f\x0b"\x00\x00\x00\x94\x85\x94R\x94\x8c\x08brand_en\x94\x8c\renglish brand\x94\x8c\x0eproductName_en\x94\x8c\x13english productname\x94\x8c\x02id\x94K\x02ub.'
        m=loads(t, scoped_session=db)
        #m.brand_en = "hello brand1111111111111"

        b={'productDescription_en': 'english productdescription',
         'price': 33,
         'created_at': datetime.datetime(2022, 9, 12, 11, 40, 52),
         'updated_at': datetime.datetime(2022, 9, 12, 15, 11, 34),
         'brand_en': 'english brand',
         'productName_en': 'english productname',
         'id': 2}

        t=Models.Product(**b)
        t._sa_instance_state.committed_state = {}
        t._sa_instance_state.key=(Models.Product,(b['id'],),None)
        print(m._sa_instance_state.__getstate__())
        print(t._sa_instance_state.__getstate__())
        db.add(t)
        t.brand_en='12321312'

        await db.commit()

asyncio.run(test())