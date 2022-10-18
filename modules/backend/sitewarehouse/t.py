#type: ignore
import requests
p=requests.session()
ret=p.get('https://www.baidu.com/')
print(ret.text)