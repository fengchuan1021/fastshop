from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
import settings
from fastapi import Request
from common.globalFunctions import get_token
import Broadcast
from sqlalchemy.util.concurrency import await_only

from common.routingDBsession import AsyncSessionMaker

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
            await_only(Broadcast.fireBeforeCreated(self.session.new, self.session, token))

        @event.listens_for(self.session.sync_session, 'after_flush')
        def after_flush(tmpsession, flush_context) -> None:  # type: ignore
            if self.session.new:
                await_only(Broadcast.fireAfterCreated(self.session.new, self.session, token, background=False))
                self.session._createdArr += list(self.session.new)  # type: ignore
            if self.session.dirty:
                await_only(Broadcast.fireAfterUpdated(self.session.dirty, self.session, token, background=False))
                self.session._updateArr += list(self.session.dirty)  # type: ignore
            if self.session.deleted:
                await_only(Broadcast.fireAfterDeleted(self.session.deleted, self.session, token, background=False))
                self.session._deletedArr += list(self.session.deleted)  # type: ignore

    def __await__(self):
        if settings.MODE!='dev':
            raise Exception("this method is only usable in dev environment")
        self.__init__()
        return self.__aenter__().__await__()
    async def __aenter__(self):
        return self.session

    async def __aexit__(self,*args):
        await self.session.commit()
        if self.session._updateArr:
            Broadcast.fireAfterUpdated(set(self.session._updateArr), self.session,token, background=True)  # type: ignore
        if self.session._createdArr:
            Broadcast.fireAfterCreated(self.session._createdArr, self.session,token, background=True)  # type: ignore
        if self.session._deletedArr:
            Broadcast.fireAfterDeleted(self.session._deletedArr, self.session,token, background=True)  # type: ignore
        if self.session._updateArr or self.session._createdArr or self.session._deletedArr:
            await self.session.commit()
        await self.session.close()


async def get_webdbsession(request:Request,token: settings.UserTokenData=Depends(get_token)) -> AsyncSession:
    with getdbsession(request,token) as session:
        request.state.db_client = session
        yield session



