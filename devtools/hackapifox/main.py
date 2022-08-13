#type: ignore
import os
import redis   # 导入redis 模块

cache= redis.Redis(host='192.168.1.110', port=6379, decode_responses=True)
import requests
import settings

from sqlalchemy import create_engine, MetaData

def login():
    session = requests.session()
    headers = f'''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Host: api.apifox.cn
Origin: https://www.apifox.cn
Referer: https://www.apifox.cn/
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
X-Client-Mode: web
X-Client-Version: 2.1.29-alpha.1'''
    headerarr = headers.split('\n')
    for item in headerarr:
        key, value = item.split(': ', 1)
        # print(key,value)
        session.headers.update({key: value})

    url='https://api.apifox.cn/api/v1/login?locale=zh-CN'
    ret=requests.post(url,json={"account": os.getenv("apifoxusername"), "password": os.getenv('apifoxpassword')}).json()
    print('loginret:',ret)
    token=ret['data']['accessToken']
    cache.set('apifoxtoken',token)
    cache.set('apifoxuserid',ret['data']['userId'])

    session.headers.update({'Authorization': token})
    checkteam()
    url='https://api.apifox.cn/api/v1/user-projects?locale=zh-CN'
    ret=session.get(url).json()
    print("myproject",ret)
    createed_flag=0
    for item in ret['data']:
        print('item',item['name'],12312,os.getenv('apifoxprojectname',''))
        if item['name']==os.getenv('apifoxprojectname',''):
            cache.set('apifoxprojectid',item['id'])
            createed_flag=1
            break
    if not createed_flag:
        createproject()

    if not checkdbshemafolder():
        createdbshemafolder()

def checkteam():
    session=createsession()
    url='https://api.apifox.cn/api/v1/user-teams?locale=zh-CN'
    ret=session.get(url).json()
    print('myteam',ret)
    for team in ret['data']:
        if team['name']==os.getenv('apifoxteamname'):
            cache.set('apifoxteamid',team['id'])
            break
    else:
        createteam()
def createteam():
    session=createsession()
    url='https://api.apifox.cn/api/v1/teams?locale=zh-CN'
    ret=session.post(url,data={'name':os.getenv("apifoxteamname")}).json()
    print(session.headers)
    print("crateteam:",ret)
    print(f'name={os.getenv("apifoxteamname")}')
    cache.set('apifoxteamid',ret['data']['id'])

def createproject():
    session=createsession()
    name=os.getenv('apifoxprojectname')
    url='https://api.apifox.cn/api/v1/projects?locale=zh-CN'
    data={
        'name': name,
        'membersRoleList': [{"username": os.getenv("apifoxusername").split('@')[0], "userId": cache.get('apifoxuserid'), "roleType": 1}],
        'visibility': 'private',
        'teamId': cache.get("apifoxteamid"),
        'icon': 'https://cdn.apifox.cn/app/project-icon/builtin/9.jpg',
        'toApiHub': False,
        'isIncludeExample': False
    }
    ret=session.post(url,data=data).json()
    projectid=ret['data']['id']
    cache.set('apifoxprojectid', projectid)
def checkdbshemafolder():
    session=createsession()
    url='https://api.apifox.cn/api/v1/api-schema-folders?locale=zh-CN'
    ret=session.get(url).json()
    for item in ret['data']:
        if item['name']=='DBShema' and item['type']=='schema':
            return True
    return False

def createdbshemafolder():
    session=createsession()
    url='https://api.apifox.cn/api/v1/api-schema-folders?locale=zh-CN'
    print('cratedbshenam/?')
    ret=session.post(url,data={'name':'DBShema','parentId':0}).json()
    folderid=ret['data']['id']
    cache.set('apifoxshemafolderid',folderid)

def createsession():
    session=requests.session()
    headers=f'''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Authorization: {cache.get('apifoxtoken')}
Connection: keep-alive
Host: api.apifox.cn
Origin: https://www.apifox.cn
Referer: https://www.apifox.cn/
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
X-Client-Mode: web
X-Client-Version: 2.1.29-alpha.1
X-Device-Id: jS6w1Gfc-dnQQ-AE9J-m4S1-q1juQK260ojt'''
    headerarr=headers.split('\n')
    for item in headerarr:
        key,value=item.split(': ',1)
        #print(key,value)
        session.headers.update({key:value})
    if cache.get("apifoxprojectid"):
        session.headers.update({'X-Project-Id':str(cache.get("apifoxprojectid"))})
    return session
import json
if __name__ == "__main__":
    login()
def addDataModel(name:str,jsonSchema,folderId:int=cache.get('apifoxshemafolderid')):
    session=createsession()
    session.headers.update({'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'})
    ret=session.post(f'https://api.apifox.cn/api/v1/api-schemas?locale=zh-CN',data={'name':name,'folderId':folderId,'jsonSchema':json.dumps(jsonSchema)})
    print(ret.text)
def deleteDataModel(shemaid):
    session=createsession()
    ret=session.delete(f'https://api.apifox.cn/api/v1/api-schemas/{shemaid}?locale=zh-CN')
    print(ret.text)
def getDataModel():
    session=createsession()
    print("??/")

    ret=session.get(f'https://api.apifox.cn/api/v1/schemas-tree-list?locale=zh-CN').json()
    print(ret)
    return ret
import re
def gettableshema(name,info):
    dic={'type':"object"}
    properties={}
    requiredarr=[]
    for column in info.columns:
        item = {}
        if column.name in ['update_at','create_at']:
            continue
        columntype=str(column.type)
        if columntype=='DATETIME':
            item['type']='string'
            item['format']='date-time'
        elif columntype=='BIGINT' or columntype=='INTEGER':
            item['type']='integer'
        elif columntype.startswith('VARCHAR'):
            item['type']='string'
            item['maxLength']=re.findall(r'(\d+)',columntype)[0]
        elif columntype=='Float':
            item['type']='number'
        elif columntype=='ENUM':
            item['type']="string"
            item["enum"]=column.type.enums
        if not column.primary_key:
            requiredarr.append(column.name)
        properties[column.name]=item
    dic["properties"]=properties
    dic["required"]=requiredarr
    return dic

def generateall():
    engine = create_engine(settings.DBURL.replace('mysql+aiomysql','mysql+pymysql'))
    metadata = MetaData(bind=engine)
    metadata.reflect()
    for tablename in metadata.tables:
        schemadict=gettableshema(tablename,metadata.tables[tablename])
        addDataModel('DB'+tablename,schemadict)
def deleteall():
    url=f'https://api.apifox.cn/api/v1/api-schema-folders/{cache.get("apifoxshemafolderid")}?locale=zh-CN'
    session=createsession()
    ret=session.delete(url)
    # data=getDataModel()
    # for row in data['data']:
    #     if row['name']=='DBschema':
    #         for item in row['children']:
    #             deleteDataModel(item['schema']['id'])
    createdbshemafolder()