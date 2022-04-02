# storefront
Ecommerce backend using django and django rest framework


## Setup
#### The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Bappy4u/storefront.git
$ cd storefront
```

#### Create a virtual environment to install dependencies in and activate it:
if you have `pipenv`  installed in your machine
```sh
$ pipenv install
```
It will install a virtual environment for you and will install all the dependencies
* Select that environment as your python interpreter

Once you select and run virtual environment that you just installed :
* Change Database settings in the settings.py at storefront directory
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase', # This is where you put the name of the db file. 
                 # If one doesn't exist, it will be created at migration time.
    }
}
```

* To migrate all the settings command this in the terminal
```sh
(storefront)$ python manage.py migrate
```

* To check the admin pannel create a super user

```sh
(storefront)$ python manage.py createsuperuser
```

* Finally 

```sh
(storefront)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/


#### The most challenging part so far
* To register models to the admin panel
* I added extra functionality to the models in the admin panel ( e.g: Model count, Sort, Link, etc )
Check the file here https://github.com/Bappy4u/storefront/blob/main/store/admin.py

#### Although there is no front-end yet. But you can walkthrough:
* All the functionality in the admin panel by populating some data in the database
* Optimal query requests using django-orm in http://127.0.0.1:8000/playground/hello route using SQL section of django-debug-toolbar

#### What I've used in this project
* Python 3.8
* Django 3.2.5
* Django-orm
* MySql
* django-debug-toolbar
* django-rest-framework (not used yet)

#### Incomplete task
* rest-api for this eccommerce
* Front-end with React



