#!/bin/bash

whoami
pwd

docker ps -a
docker build -t djangodocker .
docker run --name djangodocker -p 8008:80 -d djangodocker
docker exec djangodocker bash -c /var/www/djangodocker/docker-entrypoint.sh
docker exec djangodocker pytest
docker stop djangodocker
docker rm djangodocker
