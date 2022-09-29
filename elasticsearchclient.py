
import asyncio
from typing import Optional

import settings
from elasticsearch import AsyncElasticsearch
es:Optional[AsyncElasticsearch]
if settings.ELASTICSEARCHURL:

    from elasticsearch.helpers import async_bulk
    es = AsyncElasticsearch([settings.ELASTICSEARCHURL])
else:
    es=None

if __name__ == '__main__':
    import datetime


    async def main():#type: ignore
        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.datetime.now(),
        }
        resp = await es.index(index="test-index", document=doc)
        print(resp['result'])
    asyncio.run(main())
