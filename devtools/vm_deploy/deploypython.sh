sudo docker build . -t xtpythonimg --build-arg MODE=STAGE
sudo  docker ps | grep xtpython && sudo docker stop xtpython
sudo docker run -d --rm --name xtpython xtpythonimg