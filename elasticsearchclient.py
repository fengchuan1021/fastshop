
import asyncio

from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

import settings
if settings.ELASTICSEARCHURL:
    es = AsyncElasticsearch([settings.ELASTICSEARCHURL])
else:
    print("elasticsearch not enable")
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
