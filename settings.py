import orjson
import pydantic
def orjson_dumps(v, *, default)->str:#type: ignore
    return orjson.dumps(v, default=default).decode()
pydantic.config.BaseConfig.json_loads=orjson.loads
pydantic.config.BaseConfig.json_dumps=orjson_dumps
from pathlib import Path
from pydantic import BaseModel
from typing import Union, Optional, Literal

from dotenv import load_dotenv
import os
BASE_DIR = Path(__file__).parent.__str__()
DEBUG=False
MODE=os.getenv("MODE","dev")

if MODE=='dev':
    DEBUG = True
    load_dotenv(os.path.join(BASE_DIR, 'environment/DEV.env'))
    load_dotenv(os.path.join(BASE_DIR, 'environment/DEVCONNECT.env'))
elif MODE=='stage':
    load_dotenv(os.path.join(BASE_DIR, 'environment/STAGE.env'))
else:
    load_dotenv(os.path.join(BASE_DIR, 'environment/PROD.env'))
from UserRole import UserRole
NODEID=int(os.getenv("NODEID", 0))
REDISURL:str=os.getenv('REDISURL','')
SLAVEREDISURL:str=os.getenv('SLAVEREDISURL','')
CELERY_BROKER_URL=os.getenv('AMQPURL','')
CELERY_RESULT_BACKEND=os.getenv('REDISURL','')
CELERY_RESULT_EXPIRED=3600


ELASTICSEARCHURL=os.getenv('ELASTICSEARCHURL','')

DBURL=os.getenv("ASYNCDBURL",'')
SLAVEDBURL=os.getenv("SLAVEDBURL",DBURL)
SYNC_DBURL=os.getenv("SYNCDBURL",'')

AZ_BLOB_CONNSTR=os.getenv('az_blob_connstr','')

ENABLE_CACHE=True
CACHE_PREFIX='xtcache'
DEFAULT_CACHE_EXPIRE=3600*12

SECRET_KEY = "11a60e557ae59d6a4674bb5aeddcbc963bed0a4d44694f62c3be578d4155471d"
ACCESS_TOKEN_EXPIRE_MINUTES = 3600*24*30
ALGORITHM = "HS256"
AZCONTAINER_NAMES=Literal['productimage','categoryimg','deitalimage','commonfile']
AZCONTAINER_CONFIG={
'productimage':{
    'resize':[(100,100),(50,50)]

}
}
class UserTokenData(BaseModel):
    id:int
    phone:str=''
    userrole:int=0
    username=''
    nickname:Optional[str]=''
    is_guest=False
    @property
    def is_admin(self)->int:
        if not self.userrole:
            self.userrole=0
        return self.userrole & UserRole.admin.value
    class Config:
        orm_mode = True
