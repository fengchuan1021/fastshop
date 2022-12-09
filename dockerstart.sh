#!/bin/bash
if [ -z "$MODE" ] ; then
  MODE="MAIN"
fi

if [ -z "$CMD" ] ; then
  CMD="APP"
fi
CPUNUMBER=`grep -c ^processor /proc/cpuinfo`
if [ "$CMD" = "APP" ] ; then
  if [ "$MODE" = "DEV" ] ; then
    uvicorn app:app --reload --port 8000 --host=0.0.0.0
  elif [ "$MODE" = "MAIN" ] ; then
    mkdir -p /app/alembic/versions
    mkdir -p /app/img
    python manage.py upgrade
    #gunicorn app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
    gunicorn app:app --workers $CPUNUMBER --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
  else
    mkdir -p /app/alembic/versions
    mkdir -p /app/img
    python manage.py upgrade
    migratedb=1 python manage.py resetdb
    migratedb=0 uvicorn app:app --reload --port 8000 --host=0.0.0.0
  fi
elif [ "$CMD" = "CELERY" ] ; then
    #celery -A celery_mainworker beat -S redbeat.RedBeatScheduler -l info >/dev/null &
    celery -A celery_mainworker worker --concurrency=$CPUNUMBER  --beat -S redbeat.RedBeatScheduler -l info
fi