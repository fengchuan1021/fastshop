from typing import List

import settings
import os
import re
from devtools import generateModel
from pathlib import Path
import importlib
def before_appstart()->None:
    allmodelclasses=generateModel.generate_model()
    print(allmodelclasses)
    serviceTpl=open(os.path.join(settings.BASE_DIR, 'devtools','template', 'Service__init__.py.tpl'), 'r', encoding='utf8').read()
    #ModelsContent=open(os.path.join(settings.BASE_DIR, 'Models','allModels.py.fromdb'), 'r', encoding='utf8').read()
    #classnames=re.findall(r'class (.*?)\(Base\)',ModelsContent)
    arr={}
    for cls in allmodelclasses:
        arr[cls] = f'{cls}Service : CRUDBase[Models.{cls}]\n'
    def getclassnames(filetoread:Path)->List:
        allcontent=filetoread.open('rt',encoding='utf8').read()
        return re.findall(r'class (.*?)Service',allcontent)
    importoServiceini=[]
    for f in Path(settings.BASE_DIR).joinpath('Service').rglob('*.py'):
        if f.name.endswith('Service.py'):
            classnames=getclassnames(f)
            if not classnames:
                continue

            for classname in classnames:
                arr[classname]=f'{classname}Service : Service.{classname}Service\n'
            classService=[tmp+'Service' for tmp in classnames]
            importoServiceini.append(f"from .{str(f.relative_to(Path(settings.BASE_DIR).joinpath('Service'))).replace(os.path.sep,'.')[0:-3]} import {','.join(classService)}")

    with open(os.path.join(settings.BASE_DIR, 'ServiceManager.py'), 'r', encoding='utf8') as tmpf:
        oldcontent=tmpf.read()

    newcontent=resigtryTpl.replace('{annotations}','    '.join(arr.values()))
    if oldcontent!=newcontent:
        with open(os.path.join(settings.BASE_DIR, 'ServiceManager.py'), 'w', encoding='utf8') as tmpf:
            tmpf.write(newcontent)



    with open(os.path.join(settings.BASE_DIR, 'Service', '__init__.py'), 'r', encoding='utf8') as tmpf:
        oldcontent=tmpf.read()
    newcontent='\n'.join(sorted(importoServiceini))
    if oldcontent!=newcontent:
        with open(os.path.join(settings.BASE_DIR, 'Service', '__init__.py'), 'w', encoding='utf8') as tmpf:
            tmpf.write(newcontent)


if __name__=='__main__':
    before_appstart()
