#type: ignore
from common.dbsession import getdbsession
from common.globalFunctions import async2sync
async def main():
    async with getdbsession() as db:
        db.add_all([])

async2sync(main)()