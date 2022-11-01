import settings
import os
import importlib
from pathlib import Path
from .__init__ import Market
class ThirdMarketService():
    pass
    def __init__(self)->None:
        self.markets={}
        files=os.listdir('market')
        for f in files:
            if f.endswith('Market.py'):
                print(Path(__file__).parent.joinpath('market',f[0:-3]).relative_to(settings.BASE_DIR).__str__().replace('\\','.'))
                clsfile=importlib.import_module(Path(__file__).parent.joinpath('market',f[0:-3]).relative_to(settings.BASE_DIR).__str__().replace('\\','.'))
                cls=getattr(clsfile,f[0:-3])
                self.markets[f[0:-9].lower()]=cls
    async def getMarket(self,marketname:str)->Market:
        if marketname in self.markets:
            return self.markets[marketname]
        else:
            raise Exception(f"{marketname} not implement found")


if __name__=='__main__':
    import asyncio
    from common.dbsession import getdbsession
    async def test()->None:
        async with getdbsession() as db:
            t = ThirdMarketService()
            tiktok=await t.getMarket('tiktok')
            r=await tiktok.getProductList()


