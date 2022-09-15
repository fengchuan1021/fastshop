### install and iniproject

clone code repository:

```
git clone https://github.com/fengchuan1021/tmapi.git
```

initproject after clone.(such as input db password,db name ,etc).

```
python manage.py initall
```



### start up server

```
python app.py
```

or

```
python -m uvicorn app:app --reload
```





### generate cotroller and shema from openapi.json:



```shell
python manage.py importopenapi 1.json
```







### some docker command to setup mysql,redis,rabbmitmq quickly.





docker run --add-host=host.docker.internal:host-gateway --restart=always --log-opt max-size=10m --log-opt max-file=5 -d --name myredis -p 6379:6379 redis

docker run --add-host=host.docker.internal:host-gateway --restart=always --log-opt max-size=10m --log-opt max-file=5 -d --name mymysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=XT  -v /home/fengchuan/mysqldata:/var/lib/mysql mysql:8 --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4

docker run --add-host=host.docker.internal:host-gateway --restart=always --log-opt max-size=10m --log-opt max-file=5 -d --hostname my-rabbit --name myrabbit -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p5672:5672 -p15672:15672 rabbitmq:3-management

###other command.
alembic revision --autogenerate -m "add root_cause table"
alembic upgrade head
mysql+pymsql://root:root@host.docker.internal/buildbot


### if you have Distributed tasks,start celery worker(linux only)

```
celery -A celery_mainworker beat -S redbeat.RedBeatScheduler -l info
celery -A celery_mainworker worker -l info --concurrency=4
```