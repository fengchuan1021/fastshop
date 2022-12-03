docker build . -t xtpythonimg --build-arg MODE=STAGE --build-arg USE_TUNA=1
docker ps | grep xtpython && docker stop xtpython
docker run -d --rm -p8000:8000 -e MODE="STAGE" -e CMD="APP" --name xtpython xtpythonimg

docker ps | grep xtpythoncelery && docker stop xtpythoncelery
docker run -d --rm  -e MODE="STAGE" -e CMD="CELERY" --name xtpythoncelery xtpythonimg
