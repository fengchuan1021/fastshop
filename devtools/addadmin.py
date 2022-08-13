import asyncio

import Models
from common.dbsession import getdbsession
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def adddefaultadmin():
    u = Models.User(username='fengchuan', password=pwd_context.hash('123456'), userrole=2)
    db=await getdbsession()
    db.add(u)
    await db.commit()


if __name__ == '__main__':
    asyncio.run(adddefaultadmin())