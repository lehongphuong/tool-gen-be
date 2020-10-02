#!/bin/bash
# git clone project clone
sudo git clone https://github.com/lehongphuong/docker-aws-sample.git /myproject

# install latest version of docker the lazy way
sudo curl -sSL https://get.docker.com | sh

# make it so you don't need to sudo to run docker commands
sudo usermod -aG docker ubuntu

# install docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# on system restart
sudo curl -o /etc/systemd/system/docker-compose-app.service https://raw.githubusercontent.com/lehongphuong/docker-aws-sample/master/docker-compose-app.service
sudo systemctl enable docker-compose-app

# start up the application via docker-compose
cd /myproject
sudo docker-compose build
sudo docker-compose run web python /code/manage.py makemigrations
sudo docker-compose run web python /code/manage.py migrate
sudo docker-compose up -d