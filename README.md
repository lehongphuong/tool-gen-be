# Django CRM Project - Contact Management Project 

I am trying to create a Tutorial on How yo Create CRM or Contact Management System in Django. Basically this tutorial is creating while explaining video tutorial. This is the series of Django CRM Tutorial.

### Setup
1. Create a folder and put all the files inside it.
2. Create a virtual environtment - `virtualenv env`
3. Activate VirtualENV - ubuntu : `source env/bin/activate` || windows : `. .\env\Scripts\activate`
4. Run requirements.txt - `pip install -r requirements.txt`
5. Run the Application - `python manage.py runserver`
6. Migrate



### Setup with docker
1. Build Image and Container: `sudo docker-compose build`
2. Migration database: `sudo docker-compose run web python /code/manage.py makemigrations`
2. Migration database: `sudo docker-compose run web python /code/manage.py migrate`
3. Create supseruser: `sudo docker-compose run web python /code/manage.py createsuperuser`
4. Run application with attach log: `sudo docker-compose up`
5. Run application with no attach: `sudo docker-compose up -d`
6. Run application with no attach and build: `sudo docker-compose up -d --build`


### sample
curl -o lightsail-compose.sh https://raw.githubusercontent.com/mikegcoleman/todo/master/lightsail-compose.sh 
## Câu lệnh này sẽ dùng để deploy trên cloud
sudo curl -o ./lightsail.sh https://raw.githubusercontent.com/lehongphuong/docker-aws-sample/master/lightsail-compose.sh

sudo chmod +x lightsail.sh

sudo ./lightsail.sh 



## chạy lệnh này để cài docker
sudo apt-get update; sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y; curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -; sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"; sudo apt-get update -y; sudo apt-get install docker-ce -y; docker --version;

## cai docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose;
sudo chmod +x /usr/local/bin/docker-compose


# It runs from the directory of a docker instance and for the docker-compose that is running
docker-composer stop
# Run from the directory of a docker instance and start the docker-compose
docker-composer start
# Stop all containers
docker stop $ (docker ps -a -q)
# Remove all containers
docker rm $ (docker ps -a -q)
# Delete all images
docker rmi $ (docker images -q)
