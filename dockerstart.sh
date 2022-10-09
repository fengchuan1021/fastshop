#!/bin/bash
if [ -z "$MODE" ] ; then
  MODE="main"
fi

if [ -z "$CMD" ] ; then
  CMD="APP"
fi
CPUNUMBER=`grep -c ^processor /proc/cpuinfo`
if [ "$CMD" = "APP" ] ; then
  if [ "$MODE" = "dev" ] ; then
    uvicorn app:app --reload --port 8000 --host=0.0.0.0
  elif [ "$MODE" = "main" ] ; then
    #gunicorn app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
    gunicorn app:app --workers $CPUNUMBER --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
  else
    mkdir -p /app/alembic/versions
    python manage.py resetdb
    uvicorn app:app --reload --port 8000 --host=0.0.0.0
  fi
elif [ "$CMD" = "CELERY" ] ; then
    #celery -A celery_mainworker beat -S redbeat.RedBeatScheduler -l info >/dev/null &
    celery -A celery_mainworker worker --concurrency=$CPUNUMBER  --beat -S redbeat.RedBeatScheduler -l info
fi