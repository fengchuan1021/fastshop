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
    uvicorn app:app --reload
  elif [ "$MODE" = "main" ] ; then

    gunicorn app:app --workers $CPUNUMBER --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
  else
    uvicorn app:app --reload
  fi
elif [ "$CMD" = "CELERY" ] ; then
    celery -A celery_mainworker beat -S redbeat.RedBeatScheduler -l info >/dev/null &
    celery -A celery_mainworker worker --concurrency=$CPUNUMBER  --beat -S redbeat.RedBeatScheduler -l info
fi