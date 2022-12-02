sudo docker build . -t xtpythonimg --build-arg MODE=STAGE --build-arg USE_TUNA=1
sudo  docker ps | grep xtpython && sudo docker stop xtpython
sudo docker run -d --rm -p8000:8000 -e MODE="STAGE" -e CMD="APP" --name xtpython xtpythonimg

sudo  docker ps | grep xtpythoncelery && sudo docker stop xtpythoncelery
sudo docker run -d --rm  -e MODE="STAGE" -e CMD="CELERY" --name xtpythoncelery xtpythonimg
