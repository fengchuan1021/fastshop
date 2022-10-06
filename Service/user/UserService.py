import Service
from Service.base import CRUDBase
import Models
from typing import Union
from datetime import datetime, timedelta
from jose import JWTError, jwt
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy.sql import and_, or_
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import hashlib
import random



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from sqlalchemy import select



class UserService(CRUDBase[Models.User]):

    async def getUserByPhoneOrUsernameOrEmail(self,db: AsyncSession,usernameOrPhone:str)->Optional[Models.User]:
        query=select(self.model).filter(or_(Models.User.username==usernameOrPhone,Models.User.phone==usernameOrPhone,Models.User.email==usernameOrPhone))
        results = await db.execute(query)
        return results.scalar_one_or_none()

    #dont delete we need use this in futchure
    # def verify_password(self,plain_password:str, hashed_password : Optional[str])->bool:
    #
    #     return pwd_context.verify(plain_password, hashed_password,'bcrypt')
    # def get_password_hash(self,password):# type: ignore
    #     return pwd_context.hash(password)
    def verify_password(self,password:str, dbpassword:str)->bool:
        passwordhash, salthash = dbpassword.split(':')
        return passwordhash == hashlib.md5((salthash + password).encode()).hexdigest()

    def get_password_hash(self,password:str)->str:
        salthash = hashlib.md5(random.randint(10000, 99999).to_bytes(4, byteorder='big')).hexdigest()
        passwordhash = hashlib.md5((salthash + password).encode()).hexdigest()
        return passwordhash + ':' + salthash

    async def authenticate(self,dbSession: AsyncSession, username: str, password: str)->bool | Models.User:
        user = await self.getUserByPhoneOrUsernameOrEmail(dbSession,username)
        if not user:
            return False
        else:
            if not self.verify_password(password, user.password):#type: ignore
                return False
        return user
    async def create_refresh_token(self,data:Models.User, expires_delta: Union[timedelta, None] = None)->str:
        to_encode = settings.UserTokenData.from_orm(data).dict()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_SECONDS)
        to_encode.update({"exp": expire,'type':'refresh'})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    async def create_access_token(self,data:Models.User, expires_delta: Union[timedelta, None] = None)->str:
        to_encode = settings.UserTokenData.from_orm(data).dict()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        to_encode.update({"exp": expire,'type':'access'})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt



if __name__ == '__main__':
    import  asyncio
    from common.dbsession import getdbsession
    async def t():
        async with getdbsession() as db:
            await Service.userService.create(db,{"userrole":5,"username":"5556677","password":"ffffff"})

    asyncio.run(t())