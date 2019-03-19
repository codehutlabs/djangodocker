# Django Docker

## Usefull commands

```
docker build . -t djangodocker
docker run -p 8008:80 -d djangodocker
docker exec -it CONTAINER_ID bash -c /var/www/djangodocker/docker-entrypoint.sh
docker exec -it CONTAINER_ID /bin/bash

#

docker login
docker tag djangodocker:latest codehutlabs/djangodocker:latest
docker push codehutlabs/djangodocker:latest

#

docker volume create data_volume

docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=djangodocker \
  -e MYSQL_USER=djangodocker \
  -e MYSQL_PASSWORD=djangodocker \
  -e MYSQL_DATABASE=djangodocker \
  -v data_volume:/var/lib/mysql \
  -p 3305:3306 -d mysql:5.7

docker run -it --link mysql:db --name phpmyadmin \
  -e MYSQL_ROOT_PASSWORD=djangodocker \
  -e MYSQL_USER=djangodocker \
  -e MYSQL_PASSWORD=djangodocker \
  -p 8888:80 -d phpmyadmin/phpmyadmin

docker run -it --link mysql:db --name djangodocker-runner -p 8008:80 -d djangodocker
docker run -it --link mysql:db --name djangodocker-runner -p 8008:80 -d codehutlabs/djangodocker
```

## AWS EC2 setup: Ubuntu 18.04

Using instructions based on https://docs.docker.com/install/linux/docker-ce/ubuntu/

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo docker run hello-world
```

Additionally installed:

```
sudo apt-get install nano apache2
```

And created a new vhost configuration in /etc/apache2/sites-available/dockercodehut.conf to setup proxy:

```
<VirtualHost *:80>
    ProxyPreserveHost On
    ProxyRequests Off
    ServerName docker.codehutlabs.io
    ServerAlias docker-django.codehutlabs.io
    ProxyPass / http://localhost:8008/
    ProxyPassReverse / http://localhost:8008/
</VirtualHost>
```
