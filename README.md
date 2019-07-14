#collaborators
rafiq.macronoob@gmail.com
ilhdaf.macronoob@gmail.com
firdauz.macronoob@gmail.com

# e-invite
guestbook and einvite
virtualenv: pyeinvite
requirements: django, mysql, xlrd
reference: 
https://cloud.google.com/python/django/appengine #google tutorial
gcloud auth application-default login
gcloud services enable sqladmin
instance id: mvites-instance
pw: mvites12345
connectionName: mvites-project:asia-southeast1:mvites-instance
cloud_sql_proxy.exe -instances="mvites-project:asia-southeast1:mvites-instance"=tcp:3306
Python manage.py createsuperuser --username=admin --email=it.macronoob@gmail.com pw:mvites12345

Settings.py:

ALLOWED_HOSTS = ['*']
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/mvites-project:asia-southeast1:mvites-instance',
            'USER': 'root',
            'PASSWORD': 'mvites12345',
            'NAME': 'mvitesdb',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'mvitesdb',
            'USER': 'root',
            'PASSWORD': 'mvites12345',
        }
    }

    
app.yaml:
# [START django_app]
runtime: python37

handlers:
# This configures Google App Engine to serve the files in the app's static
# directory.
- url: /static
  static_dir: static/

# This handler routes all requests not caught above to your main app. It is
# required when static routes are defined, but can be omitted (along with
# the entire handlers section) when there are no static files defined.
- url: /.*
  script: auto
# [END django_app]
© 2019 GitHub, Inc.

main.py:

from mysite.wsgi import application #mustchange mysite to projectname

# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of your Django app,
# application from mysite/wsgi.py and renames it app so it is discoverable by
# App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi
app = application

