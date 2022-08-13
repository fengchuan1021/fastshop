#!/usr/bin/env python

import os
import subprocess
import sys
from pathlib import Path
try:
    import typer
except Exception as e:
    yn = input('speed pip install use china tsinghua university pip source y/n? [y]:')
    yn=yn.strip()
    if not yn or yn=='y' or yn=="Y":
        subprocess.check_call(['pip', "config", "set", "global.index-url", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    else:
        subprocess.check_call(['pip', "config", "unset", "global.index-url"])
    subprocess.check_call([sys.executable, "-m", "pip", "install","-r", 'requirements.txt'])
    if os.name!='nt':
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvloop"])
try:
    import typer
    app = typer.Typer()

except Exception as e:
    raise
import pymysql
import click
@app.command()
def inidb()->None:
    DB_HOST= click.prompt('Please input database host', default='127.0.0.1',type=str)
    DB_USER = click.prompt('Please input database user', default='root',type=str)
    DB_PASS = click.prompt('Please input database password', default='root',type=str)
    DB_PORT= click.prompt('Please input database port', default=3306,type=int)
    DATABASE =click.prompt('Please input database name', default="XT",type=str)
    AMQPURL=click.prompt('Please input rabbitmq url', default="amqp://admin:admin@127.0.0.1:5672/",type=str)
    REDISURL = click.prompt('Please input redis url', default="redis://127.0.0.1:6379",
                                     type=str)
    with open('DEVCONNECT.env','w',encoding='utf8') as conf:
        conf.write(f'''ASYNCDBURL="mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8mb4"
SYNCDBURL="mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8mb4"

BUILDBOT_CONFIG_URL="https://raw.fastgit.org/fengchuan1021/buildbot-docker-example-config/master/master.cfg"
AMQPURL="{AMQPURL}"
REDISURL="{REDISURL}"
nodeid="66"
''')
    db = pymysql.connect(host=DB_HOST,
                         user=DB_USER,
                         password=DB_PASS,
                         port=DB_PORT,autocommit=True
                         )

    try:
        with db.cursor() as cursor:
            cursor.execute(f'drop database IF EXISTS {DATABASE}')
            cursor.execute(f'create DATABASE {DATABASE}')
            from alembic import command
            import settings
            from alembic.config import Config
            versionpath=os.path.join('alembic','versions')
            if os.path.exists(versionpath):
                versionfiles=os.listdir(versionpath)
                for f in versionfiles:
                    if f =='__pycache__':
                        continue
                    os.remove(os.path.join(versionpath,f))
            else:
                os.mkdir(versionpath)
            configstr = str(Path(settings.BASE_DIR).joinpath('alembic.ini'))
            config = Config(configstr)
            command.revision(config=config, autogenerate=True)
            command.upgrade(config=config, revision='head')

    finally:
        db.close()


@app.command()
def migratedb()->None:
    from alembic import command
    import settings
    from alembic.config import Config
    configstr = str(Path(settings.BASE_DIR).joinpath('alembic.ini'))
    config = Config(configstr)
    command.revision(config=config, autogenerate=True)
    command.upgrade(config=config, revision='head')
    click.secho('Success: db migrate successfuly', fg='green')

@app.command()
def resetdb()->None:
    from alembic import command
    import settings

    from alembic.config import Config
    versionpath = os.path.join('alembic', 'versions')
    versionfiles = os.listdir(versionpath)
    for f in versionfiles:
        if f == '__pycache__':
            continue
        os.remove(os.path.join(versionpath, f))

    connection = pymysql.connect(host=os.getenv('DB_HOST'),
                                 user=os.getenv('DB_USER','root'),
                                 port=int(os.getenv('DB_PORT',3306)),
                                 password=os.getenv('DB_PASS','root'),
                                 database=os.getenv('DATABASE'),autocommit=True)
    cur=connection.cursor()
    cur.execute("delete from alembic_version")


    configstr = str(Path(settings.BASE_DIR).joinpath('alembic.ini'))
    config = Config(configstr)

    command.revision(config=config, autogenerate=True)
    command.upgrade(config=config, revision='head')
    click.secho('Success: db reset successfuly', fg='green')
@app.command()
def initall()->None:

    from devtools import patchlibrary
    print('begin patch library:')
    patchlibrary.patch()
    print('end patch library')

    if os.path.exists('.git'):
        print('begin setup git hook')
        subprocess.check_call(['git', "config", "--local", "core.hooksPath", ".githooks/"])
        print('end setup git hook')
    if os.getenv('DEBIAN_FRONTEND','')!='noninteractive':
        inidb()

    click.secho('Success: project has init successfully', fg='green')

from devtools.generatefromopenapi import mymain
@app.command()
def importopenapi(filepath:str)->None:
    content=open(filepath,'r',encoding='utf8').read()
    mymain(content)
if __name__ == "__main__":
    app()