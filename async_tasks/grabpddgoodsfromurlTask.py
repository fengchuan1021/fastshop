#type: ignore
import time


from sqlalchemy.dialects.mysql import Insert
import settings
import aiohttp

import asyncio
from celery_app import celery_app
from async_tasks.sync2async import sync2async
import Models
from component.snowFlakeId import snowFlack
from common.dbsession import getdbsession
@celery_app.task
@sync2async
async def pddgrabworker(keyword,pagenum,category=''):

    db=await getdbsession()

    for i in range(1,int(pagenum)+1):
        url = f'http://sj.66daili.cn/api/pdd/keyword?apikey=TsRpTaMWjE8X&keyword={keyword}&page={i}'
        n = 0
        while 1:
            if n>5:
                await db.close()
                break
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        data = await response.json()
                        print('data',data)
                        #arr=[]
                        if not data['data'] and data['msg']=='找不到更多的关键词信息了':
                            print('break::')
                            await db.close()
                            return None

                        for item in data['data']['items']:
                            dic={'id':snowFlack.getId(),'category':category}
                            for key in item:
                                if key=='tag_list':
                                    dic['tag_list']=','.join([row['text'] for row in item[key]])
                                else:
                                    if hasattr(Models.Product,key):
                                        dic[key]=item[key]
                            sql=Insert(Models.Product).values(**dic).on_duplicate_key_update(**dic)
                            await db.execute(sql)
                            await db.commit()
                            #arr.append(dic)
                        #await db.close()
                        #return arr
                        break
            except Exception as e:
                print(e)
                await asyncio.sleep(2)
                n+=1



def publishtask(keyword,pagenum=6,threadn=20,category=''):

    taskresults=[]

    url=f'http://sj.66daili.cn/api/pdd/keyword?apikey=TsRpTaMWjE8X&keyword='
    taskresults.append(pddgrabworker.delay(keyword,pagenum,category))
    return taskresults

#publishtask("手机")


@celery_app.task
@sync2async
async def webpddgrabworker(url):
    db=await getdbsession()
    arr=[]
    n=0
    while 1:
        if n>3:
            await db.close()
            return arr
        try:
            print('inwhei??')
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()

                    if not data['data'] and data['msg'] == '找不到更多的关键词信息了':
                        return arr
                    for item in data['data']['items']:
                        dic={'id':snowFlack.getId()}
                        for key in item:
                            if key=='tag_list':
                                dic['tag_list']=','.join([row['text'] for row in item[key]])
                            else:
                                if hasattr(Models.Product,key):
                                    dic[key]=item[key]
                        sql=Insert(Models.Product).values(**dic).on_duplicate_key_update(**dic)
                        await db.execute(sql)
                        await db.commit()
                        arr.append(dic)
                    await db.close()
                    return arr
        except Exception as e:
            print(e)
            await asyncio.sleep(2)
            n+=1



def webpublishtask(keyword,pagenum=6):

    taskresults=[]
    for i in range(1,pagenum+1):
        url=f'http://sj.66daili.cn/api/pdd/keyword?apikey=TsRpTaMWjE8X&keyword={keyword}&page={i}'
        taskresults.append(webpddgrabworker.delay(url))
    return taskresults