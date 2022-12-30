#!/usr/bin/env python
import os
from pathlib import Path
import site
def patch()->None:
    print('beginpatch')
    files=site.getsitepackages()
    targetdir=''
    for f in files:
        if f.endswith('site-packages'):
            targetdir=f
        else:
            continue
        patchdir=str(Path(__file__).parent.joinpath('patchs'))
        files=os.listdir(patchdir)
        print('beginpatch')
        for filename in files:
            try:
                with open(os.path.join(patchdir,filename),'r',encoding='utf8') as tmpf:
                    filepath=tmpf.readline().strip()

                    content=tmpf.read()
                    realpath=filepath.replace('venv/Lib/site-packages',targetdir)
                    if os.path.exists(realpath):
                        with open(realpath,'w',encoding='utf8') as tf:
                            tf.write(content)
            except Exception as e:
                print(e)
if __name__ == '__main__':
    patch()