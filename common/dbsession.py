from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
import settings
from fastapi import Request
from common.globalFunctions import get_token
import Broadcast
from sqlalchemy.util.concurrency import await_only
engine = create_async_engine(
    settings.DBURL,
    echo=settings.DEBUG,
)
from common.routingDBsession import AsyncSessionMaker
#async_session = AsyncSessionMaker()
#async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
async def _getdbsession(request,token)-> AsyncSession:
    session=AsyncSessionMaker()
    try:
        setattr(session, "_createdArr", [])
        setattr(session, "_updateArr", [])
        setattr(session, '_deletedArr', [])

        @event.listens_for(session.sync_session, 'before_flush')
        def before_flush(tmpsession, flush_context, instances) -> None:  # type: ignore
            await_only(Broadcast.fireBeforeCreated(session.new, session, token))

        @event.listens_for(session.sync_session, 'after_flush')
        def after_flush(tmpsession, flush_context) -> None:  # type: ignore
            if session.new:
                await_only(Broadcast.fireAfterCreated(session.new, session, token, background=False))
                session._createdArr += list(session.new)  # type: ignore
            if session.dirty:
                await_only(Broadcast.fireAfterUpdated(session.dirty, session, token, background=False))
                session._updateArr += list(session.dirty)  # type: ignore
            if session.deleted:
                await_only(Broadcast.fireAfterDeleted(session.deleted, session, token, background=False))
                session._deletedArr += list(session.deleted)  # type: ignore
        yield session
    finally:
        await session.commit()

        if session._updateArr:
            Broadcast.fireAfterUpdated(set(session._updateArr), session,token, background=True)  # type: ignore
        if session._createdArr:
            Broadcast.fireAfterCreated(session._createdArr, session,token, background=True)  # type: ignore
        if session._deletedArr:
            Broadcast.fireAfterDeleted(session._deletedArr, session,token, background=True)  # type: ignore
        if session._updateArr or session._createdArr or session._deletedArr:
            await session.commit()

        await session.close()
async def getdbsession(request=None,token=None)-> AsyncSession:
    generator=_getdbsession(request,token)
    return await generator.__anext__()


async def get_webdbsession(request:Request,token: settings.UserTokenData=Depends(get_token)) -> AsyncSession:
    session=await getdbsession(request,token)
    request.state.db_client=session
    return session


