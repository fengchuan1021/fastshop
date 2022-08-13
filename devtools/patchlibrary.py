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

    patchdir=str(Path(__file__).parent.joinpath('patchs'))
    files=os.listdir(patchdir)
    print('beginpatch')
    for filename in files:
        content=None
        try:
            with open(os.path.join(patchdir,filename),'r',encoding='utf8') as tmpf:
                filepath=tmpf.readline().strip()

                content=tmpf.read()
                realpath=filepath.replace('venv/Lib/site-packages',targetdir)
                print(f'patchfile:     {realpath}')
                with open(realpath,'w',encoding='utf8') as tf:
                    tf.write(content)
        except Exception as e:
            print(e)