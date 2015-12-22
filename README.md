IntroCTF
-------
#### IntroCS2 Final Project by:
- James Wang
- Joel Ye

#### Setting up the environment:
1. Run `./setup.sh` to install required dependencies and packages.
2. Run `python setup.py` to initialize the database. Run `python wipe_db.py` to wipe the database clean, or just run `setup.py` again.

Optionally run `python populate.py` to populate the database with random data.

#### Deployment:
##### Flask
The simplest way to deploy the site is to run `python app.py`. However, this is not recommended for large-scale applications.
If you really wish to run it using this method, make sure to turn off debug mode, which can be found in `app.py`.

##### Gunicorn
[Gunicorn](http://gunicorn.org/) is a much more powerful alternative to running the app bare, and is
also very easy to setup. It takes two steps to deploy using this method.
1. `sudo pip install gunicorn`
2. `gunicorn --bind 0.0.0.0:8000 -w 4 "app:app"` where 4 can be any number of workers that you would like to have
