
import asyncio



import settings
if settings.ELASTICSEARCHURL:
    from elasticsearch import AsyncElasticsearch
    from elasticsearch.helpers import async_bulk
    es = AsyncElasticsearch([settings.ELASTICSEARCHURL])
else:
    print("elasticsearch not enable")
    class AsyncElasticsearch:#type: ignore
        def index(self,*args,**kwargs)->None:#type: ignore
            pass
    es=AsyncElasticsearch()

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
