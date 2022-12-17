#type: ignore
import aiohttp
import orjson
from sqlalchemy import text

import Service
from common import cmdlineApp
from Models import Country
dic={
'1':{'name_en':'Europe','name_cn':'欧洲'},
'2':{'name_en':'North America','name_cn':'北美'},
'3':{'name_en':'South America','name_cn':'南美'},
'4':{'name_en':'Asia','name_cn':'亚洲'},
'5':{'name_en':'Oceania','name_cn':'大洋洲'},
'6':{'name_en':'Africa','name_cn':'非洲'},
'7':{'name_en':'Other','name_cn':'其他'},

     }

hotCountry=[
					{"countryCh":'美国',"countryEn":'UNITED STATES',"code":'US'},
					{"countryCh":'俄罗斯',"countryEn":'RUSSIA',"code":'RU'},
					{"countryCh":'法国',"countryEn":'FRANCE',"code":'FR'},
					{"countryCh":'英国',"countryEn":'UNITED KINGDOM',"code":'GB'},
					{"countryCh":'德国',"countryEn":'GERMANY',"code":'DE'},
					{"countryCh":'加拿大',"countryEn":'CANADA',"code":'CA'},
					{"countryCh":'西班牙',"countryEn":'SPAIN',"code":'ES'},
					{"countryCh":'巴西',"countryEn":'BRAZIL',"code":'BR'},
					{"countryCh":'意大利',"countryEn":'ITALY',"code":'IT'},
					{"countryCh":'澳大利亚',"countryEn":'AUSTRALIA',"code":'AU'},
					{"countryCh":'荷兰',"countryEn":'NETHERLANDS',"code":'NL'},
					{"countryCh":'瑞典',"countryEn":'SWEDEN',"code":'SE'},
					{"countryCh":'以色列',"countryEn":'ISRAEL',"code":'IL'},
					{"countryCh":'瑞士',"countryEn":'SWITZERLAND',"code":'CH'},
					{"countryCh":'乌克兰',"countryEn":'UKRAINE',"code":'UA'},
					{"countryCh":'波多黎各',"countryEn":'PUERTO RICO',"code":'PR'},
					{"countryCh":'比利时',"countryEn":'BELGIUM',"code":'BE'},
					{"countryCh":'捷克',"countryEn":'CZECH REPUBLIC',"code":'CZ'},
					{"countryCh":'挪威',"countryEn":'NORWAY',"code":'NO'},
					{"countryCh":'波兰',"countryEn":'POLAND',"code":'PL'},
					{"countryCh":'智利',"countryEn":'CHILE',"code":'CL'},
					{"countryCh":'丹麦',"countryEn":'DENMARK',"code":'DK'},
					{"countryCh":'芬兰',"countryEn":'FINLAND',"code":'FI'},
					{"countryCh":'土耳其',"countryEn":'TURKEY',"code":'TR'},
					{"countryCh":'墨西哥',"countryEn":'MEXICO',"code":'MX'},
					{"countryCh":'白俄罗斯',"countryEn":'BELARUS',"code":'BY'},
					{"countryCh":'日本',"countryEn":'JAPAN',"code":'JP'},
					{"countryCh":'菲律宾',"countryEn":'PHILIPPINES',"code":'PH'}
]
hots=[country['code'] for country in hotCountry]
async def addcountry(db):
    #await (await db.connection()).execute(text("truncate table country;")) 不要清空表 店小秘json中有重复数据
    with open('country.json','r',encoding='utf8') as f :
        json_data=orjson.loads(f.read())
        for i in range(1,8):
            items=json_data['map'][f'{i}']
            for item in items:
                country=Country()
                country.name_en=item["countryEn"]
                country.name_cn=item["countryCh"]
                country.country_code2=item["code"]
                country.continent=dic[f'{i}']['name_en']
                country.smt_code=item["smtCode"]
                if country.country_code2 in hots:
                    country.is_hot='Y'
                db.add(country)

        await db.commit()

#cmdlineApp(addcountry)()
errors=[]
@cmdlineApp
async def updatecountry(db):
	global errors
	async with aiohttp.ClientSession() as session:
		models=await Service.countryService.find(db)
		for model in models:
			async with session.get(f'https://restcountries.com/v3.1/alpha/{model.country_code2}') as resp:

				data=await resp.json()
				if len(data)==1:
					model.country_code3=data[0]['cca3']
					if "currencies" in data[0]:
						model.currency_code=list(data[0]["currencies"].keys())[0]
						print(data[0]["currencies"][model.currency_code])
						if 'symbol' in data[0]["currencies"][model.currency_code]:
							model.currency_symbol=data[0]["currencies"][model.currency_code]['symbol']
				else:
					print(model.country_code2)
					errors.append(model.currency_code)
	print(errors)
	print('end::')
	await db.commit()
updatecountry()