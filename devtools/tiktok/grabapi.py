#type: ignore
import asyncio
from collections import defaultdict
dic=defaultdict(dict)
from ichrome import AsyncChromeDaemon
async def main():
    async with AsyncChromeDaemon(headless=0, disable_image=False,extra_config="--no-sandbox --single-process") as cd:
        async with cd.connect_tab(index=0, auto_close=True) as tab:
            global dic
            await tab.goto('https://developers.tiktok-shops.com/documents/document/237461',timeout=5)
            total=tab.inject_js('''var dic={};document.querySelectorAll("#root > div > div.style-module__body--EljLn > div > div > div.style-module__scroll-intersection--_kRoo > div.style-module__scroll-intersection-left--2yo6u > div > div > div > div > a > span > span").forEach(i=>dic[i.innerHTML]={});
            let keys=Object.keys(dic);
            for(let i=0;i<keys.length;i++){
                document.querySelectorAll(`#root > div > div.style-module__body--EljLn > div > div > div.style-module__scroll-intersection--_kRoo > div.style-module__scroll-intersection-left--2yo6u > div > div > div > div:nth-child(${i+1}) > div > span > span`).forEach(j=>dic[keys[i]][j.innerHTML]='')
            }
            ''')
            await tab.click('#main > div > div._1DncS32V > div > div > div > div._3oOM3OKF > div')


if __name__ == "__main__":
    asyncio.run(main())