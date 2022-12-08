import aiohttp
import settings

from component.cache import cache
@cache(expire=24*3600)
async def CurrencyRate(from_currency:str,to_currency:str='GBP')->float:
    if from_currency==to_currency:
        return 1
    print(settings.FIXERTOKEN)
    async with aiohttp.ClientSession(headers={'apikey':settings.FIXERTOKEN}) as session:
        async with session.get(f'https://api.apilayer.com/fixer/latest?base={from_currency}&symbols={to_currency}') as resp:
            data=await resp.json()
            print(data)
            return data["rates"][to_currency]

