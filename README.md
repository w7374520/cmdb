# CMDB


This repository stores the Radiobuy cmdb website.


## Installation

To get setup with CMDB code you must have the follow installed:

> * Python 2.6+
> * MySQL
> * virtualenv 1.4.7+

## Setting up environment


Create a virtual environment where dependencies will live:

```
$ virtualenv --no-site-packages cmdb
$ source cmdb/bin/activate
(cmdb)$
```

Install cmdb project dependencies::

```
(cmdb)$ pip install -r requirements.txt
```


## Setting up the database

Now you can run:

```
(cmdb)$ python cmdb_project/manage.py migrate
(cmdb)$ python cmdb_project/manage.py createsuperuser
```

## Running a web server

In development you should run:

```
(cmdb)$ python manage.py runserver
```

## Deploy it

If you are deploying on ubuntu, you may install those build dependencies.

```
sudo aptitude install libmysqlclient-dev libxml2-dev libxslt1-dev
```

Install those python libs through virtual env.

```
sudo easy_install -U pip
sudo pip install virtualenv
sudo mkdir /usr/local/virtualenv
cd /usr/local/virtualenv
sudo virtualenv --distribute --no-site-packages cmdb
source /usr/local/virtualenv/cmdb/bin/activate
cd PROJECT_FOLDER

```

```
sudo su -
source /usr/local/virtualenv/cmdb/bin/activate
pip install -r requirements.txt
```
