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
    resigtryTpl=open(os.path.join(settings.BASE_DIR, 'devtools','template', 'RegistryManager.py.tpl'), 'r', encoding='utf8').read()
    #ModelsContent=open(os.path.join(settings.BASE_DIR, 'Models','allModels.py.fromdb'), 'r', encoding='utf8').read()
    #classnames=re.findall(r'class (.*?)\(Base\)',ModelsContent)
    arr={}
    for cls in allmodelclasses:
        arr[cls] = f'{cls}Registry : CRUDBase[Models.{cls}]\n'
    def getclassnames(filetoread:Path)->List:
        allcontent=filetoread.open('rt',encoding='utf8').read()
        return re.findall(r's (.*?)Registry\(CRUDBase',allcontent)
    importoregistryini=[]
    for f in Path(settings.BASE_DIR).joinpath('Registries').rglob('*.py'):
        if f.name.endswith('Registry.py'):
            classnames=getclassnames(f)
            if not classnames:
                continue

            for classname in classnames:
                arr[classname]=f'{classname}Registry : Registries.{classname}Registry\n'
            classregistries=[tmp+'Registry' for tmp in classnames]
            importoregistryini.append(f"from .{str(f.relative_to(Path(settings.BASE_DIR).joinpath('Registries'))).replace(os.path.sep,'.')[0:-3]} import {','.join(classregistries)}")
    # for classname in classnames:
    #     if os.path.exists(os.path.join(settings.BASE_DIR, 'Registries', f'{classname}Registry.py')):
    #         arr.append(f'{classname}Registry : Registries.{classname}Registry\n')
    #     else:
    #         arr.append(f'{classname}Registry : CRUDBase[Models.{classname}]\n')
    with open(os.path.join(settings.BASE_DIR, 'RegistryManager.py'), 'r', encoding='utf8') as tmpf:
        oldcontent=tmpf.read()

    newcontent=resigtryTpl.replace('{annotations}','    '.join(arr.values()))
    if oldcontent!=newcontent:
        with open(os.path.join(settings.BASE_DIR, 'RegistryManager.py'), 'w', encoding='utf8') as tmpf:
            tmpf.write(newcontent)


    # files=os.listdir(os.path.join(settings.BASE_DIR, 'Registries'))
    # arr=[]
    # for f2 in files:
    #     if f2.endswith('Registry.py'):
    #         name=f2.replace('.py','')
    #         arr.append(f"from .{name} import {name}")
    with open(os.path.join(settings.BASE_DIR, 'Registries', '__init__.py'), 'r', encoding='utf8') as tmpf:
        oldcontent=tmpf.read()
    newcontent='\n'.join(sorted(importoregistryini))
    if oldcontent!=newcontent:
        with open(os.path.join(settings.BASE_DIR, 'Registries', '__init__.py'), 'w', encoding='utf8') as tmpf:
            tmpf.write(newcontent)


if __name__=='__main__':
    before_appstart()
