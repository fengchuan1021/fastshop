#!/bin/bash
if [ -z "$MODE" ] ; then
  MODE="PROD"
fi

if [ -z "$CMD" ] ; then
  CMD="APP"
fi
if [ "$CMD" = "APP" ] ; then
  if [ "$MODE" = "DEV" ] ; then
    uvicorn app:app --reload
  elif [ "$MODE" = "PROD" ] ; then
    CPUNUMBER=`grep -c ^processor /proc/cpuinfo`
    WORKERS=`expr $CPUNUMBER \* 2`
    gunicorn app:app --workers $WORKERS --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
  else
    uvicorn app:app --reload
  fi
elif [ "$CMD" = "CELERYWORKER" ] ; then
    celery -A celery_mainworker beat -S redbeat.RedBeatScheduler -l info >/dev/null &
    celery -A celery_mainworker worker --concurrency=4  --beat -S redbeat.RedBeatScheduler -l info
fi