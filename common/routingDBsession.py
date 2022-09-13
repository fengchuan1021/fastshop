from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import Update, Delete

import settings
import random
engines = {
    'master': create_async_engine(settings.DBURL),
    'slaver': create_async_engine(settings.SLAVEDBURL),
}


class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None, **kw):

        if self._flushing or isinstance(clause, (Update, Delete)):
            return engines['master'].sync_engine
        else:
            return engines[
                random.choice(['master', 'slaver'])
            ].sync_engine


# apply to AsyncSession using sync_session_class
AsyncSessionMaker = sessionmaker(
    class_=AsyncSession,
    sync_session_class=RoutingSession,
    expire_on_commit=False
)
