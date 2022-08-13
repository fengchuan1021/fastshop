import datetime
import os, uuid

import time

import cv2
import numpy as np
import settings
from component.cache import cache
from pathlib import Path





async def upload(imgbyte: bytes,container_name:str='commonfile',astmpfile:bool=False):#type: ignore
    dir=Path(settings.BASE_DIR).joinpath('static',container_name,datetime.datetime.now().strftime("%Y-%m-%d"))
    dir.mkdir(parents=True,exist_ok=True)

    mainfilename =str(uuid.uuid4()) + ".jpg"
    filenames = [str(dir)+'/'+mainfilename]
    dir.joinpath(mainfilename).write_bytes(imgbyte)
        #f.write(imgbyte)
    if container_name in settings.AZCONTAINER_CONFIG:

        nparr = np.frombuffer(imgbyte, np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print('resize?')
        for w,h in settings.AZCONTAINER_CONFIG[container_name]['resize']:
            print('resize?111')
            tmpimg=cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
            tmpfilename=f'{mainfilename[0:-4]}_{w}x{h}.jpg'
            print('tmpfile',tmpfilename)
            try:
                with open(os.path.join(str(dir),tmpfilename),'wb') as f:
                    f.write(tmpimg.tobytes())
                filenames.append(str(dir)+'/'+tmpfilename)
            except Exception as e:
                print(e)
                pass

    if astmpfile:
        tomorrow = int(time.time()) + 3600*24
        mapdata={f:tomorrow for f in filenames}
        await cache.redis.zadd('localtmpfiles',mapdata)
    print(f'{filenames=}')
    return {'url':f'/{str(dir.relative_to(settings.BASE_DIR))}/{mainfilename}','status':'success'}
