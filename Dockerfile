FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install -y apt-utils vim nano curl apache2 apache2-utils
RUN apt install -y python3 python3-dev python3-pip libapache2-mod-wsgi-py3
RUN apt install -y mysql-client default-libmysqlclient-dev

RUN ln /usr/bin/python3 /usr/bin/python
RUN ln /usr/bin/pip3 /usr/bin/pip

RUN mkdir /var/www/djangodocker
RUN mkdir /var/www/djangodocker_static
RUN mkdir /var/www/log

ENV WEBAPP_DIR=/var/www/djangodocker
WORKDIR $WEBAPP_DIR

COPY . $WEBAPP_DIR/
COPY  $WEBAPP_DIR/app/docker_settings.py $WEBAPP_DIR//app/local_settings.py

RUN chmod +x docker-compose-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
