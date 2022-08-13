from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
import settings
from fastapi import Request
from common.globalFunctions import get_token
import BroadcastManager
from sqlalchemy.util.concurrency import await_only
engine = create_async_engine(
    settings.DBURL,
    echo=settings.DEBUG,
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
async def getdbsession()-> AsyncSession:
    session=async_session()
    return session

async def get_webdbsession(request:Request,token: settings.UserTokenData=Depends(get_token)) -> AsyncSession:
    session=await getdbsession()
    setattr(session,"_createdArr",[])
    setattr(session, "_updateArr", [])
    setattr(session,'_deletedArr',[])
    @event.listens_for(session.sync_session, 'before_flush')
    def before_flush(tmpsession, flush_context,instances)->None:#type: ignore
        await_only(BroadcastManager.fireBeforeCreated(session.new,session,token))

    @event.listens_for(session.sync_session, 'after_flush')
    def after_flush(tmpsession, flush_context)->None:#type: ignore
        if session.new:
            await_only(BroadcastManager.fireAfterCreated(session.new,session,token,background=False))
            session._createdArr += list(session.new)#type: ignore
        if session.dirty:
            await_only(BroadcastManager.fireAfterUpdated(session.dirty,session,token,background=False))
            session._updateArr += list(session.dirty)#type: ignore
        if session.deleted:
            await_only(BroadcastManager.fireAfterDeleted(session.deleted,session,token,background=False))
            session._deletedArr+=list(session.deleted)#type: ignore


    request.state.db_client=session
    return session


