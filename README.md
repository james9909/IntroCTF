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

##### Apache with mod_wsgi
An alternative method of deploying the site is to use Apache and mod_wsgi. Flask has [documentation](http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/)
explains this method well.
