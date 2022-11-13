sudo docker build . -t xtpythonimg
sudo  docker ps | grep xtpython && sudo docker stop xtpython
sodo docker run -d --rm --name xtpython xtpythonimg