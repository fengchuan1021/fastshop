import importlib
from pathlib import Path
import os
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
import settings
from fastapi import Request
from common.globalFunctions import get_token
import Broadcast
from sqlalchemy.util.concurrency import await_only
from elasticsearchclient import es
from common.routingDBsession import AsyncSessionMaker,engines

for f in Path(settings.BASE_DIR).joinpath('listeners').rglob('*.py'):
    if f.name.endswith('Listener.py'):
        importlib.import_module(str(f.relative_to(settings.BASE_DIR)).replace(os.sep,'.')[0:-3])

class getdbsession:
    def __init__(self,request:Request=None,token: settings.UserTokenData=None):
        self.request = request
        self.token=token
        self.session = AsyncSessionMaker()
        setattr(self.session, "_createdArr", [])
        setattr(self.session, "_updateArr", [])
        setattr(self.session, '_deletedArr', [])

        @event.listens_for(self.session.sync_session, 'before_flush')
        def before_flush(tmpsession, flush_context, instances) -> None:  # type: ignore
            await_only(Broadcast.fireBeforeCreated(self.session.new, self.session, self.token))

        @event.listens_for(self.session.sync_session, 'after_flush')
        def after_flush(tmpsession, flush_context) -> None:  # type: ignore
            if self.session.new:
                await_only(Broadcast.fireAfterCreated(self.session.new, self.session, self.token, background=False))
                self.session._createdArr += list(self.session.new)  # type: ignore
            if self.session.dirty:
                await_only(Broadcast.fireAfterUpdated(self.session.dirty, self.session, self.token, background=False))
                self.session._updateArr += list(self.session.dirty)  # type: ignore
            if self.session.deleted:
                await_only(Broadcast.fireAfterDeleted(self.session.deleted, self.session, self.token, background=False))
                self.session._deletedArr += list(self.session.deleted)  # type: ignore

    def __await__(self):#type: ignore
        if settings.MODE!='dev':
            raise Exception("this method is only usable in dev environment for testing porpose. in product mode it will not trigger broadcast")
        self.__init__()
        return self.__aenter__().__await__()
    async def __aenter__(self)->AsyncSession:
        return self.session

    async def __aexit__(self,*args):#type: ignore

        await self.session.commit()
        if self.session._updateArr:
            await Broadcast.fireAfterUpdated(set(self.session._updateArr), self.session,self.token, background=True)  # type: ignore
        if self.session._createdArr:
            await Broadcast.fireAfterCreated(self.session._createdArr, self.session,self.token, background=True)  # type: ignore
        if self.session._deletedArr:
            await Broadcast.fireAfterDeleted(self.session._deletedArr, self.session,self.token, background=True)  # type: ignore
        if self.session._updateArr or self.session._createdArr or self.session._deletedArr:
            await self.session.commit()
        await self.session.close()
        if not self.request:
            await es.close()
            [await engine.dispose() for engine in engines.values()]



async def get_webdbsession(request:Request,token: settings.UserTokenData=Depends(get_token)) -> AsyncSession:#type: ignore
    db_client=getdbsession(request,token)
    request.state.db_client = db_client
    return db_client.session




