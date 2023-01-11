# Deployment

## Initial Deployment
Below are the steps I took to deploy the site to Heroku and any console commands required

1. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
1. Install Django with version 3.2:
    * ```pip3 install 'django<4'```
1. Install gunicorn:
    * ```pip3 install gunicorn```
1. Install supporting libraries:
    * ```pip3 install boto3```
    * ```pip3 install django-storages```
    * ```pip3 install psycopg2-binary```
    * ```pip3 install django-phone-field```
    * ```pip3 install django-crispy-forms```
    * ```pip3 install crispy-bootstrap5```
    * ```pip3 install django-countries```
    * ```pip3 install pillow```
    * ```pip3 install django-allauth```
    * ```pip3 install mailchimp```
    * ```pip3 install mailchimp-marketing```
    * ```pip3 install stripe```
    * ```pip3 install pysqlite3-binary```

1. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
1. Create an empty folder for your project in your chosen location.
1. Create a project in the above folder:
    * ```django-admin startproject <PROJECT_NAME> .``` (in the case of this project, the project name was "Kenpachi")
1. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` (in the case of this project, the app name was "cart", "store", "home", "checkout", "marketing")
1. Add a new app to the list of installed apps in setting.py
1. Migrate changes: 
    * ```python manage.py migrate```
1. Test server works locally: 
    * ```python3 manage.py runserver```  (You should see the default Django success page)
    
## Create Heroku App:
The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * Will form part of the URL
1. Select the nearest location:
    * For me, this was Europe.
1. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears. 
    * Select "Mini - $5.00 USD" from the "plan name" drop-down menu and click "Submit Order Form." (credit card and subscription required)
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

### Setting up setting.py File:
1. At the top of your settings.py file, add the following snippet immediately after the other imports:
``` 
import os
import dj_database_url
from django.contrib.messages import constants as messages
if os.path.isfile('env.py'):
    import env
    
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
```
1. Delete the value from the setting.py DATABASES section and replace it with the following snippet to link up the Heroku Postgres server:  
   
    ```
    if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```
    
1. Set up AWS S3 in settings.py file and tell Django to use it:
   
   ```
   STATIC_URL = '/static/'
   if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
   else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   
   if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'kenpachi-estore'
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
   ```
  
1. Add allowed hosts to settings.py:
    ```
    ALLOWED_HOSTS = [
    'kenpachi-estore.herokuapp.com',
    'localhost',
    '.localhost',
    '127.0.0.1',
    '[::1]'
    ]
    ``` 

1. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn PROJECT_NAME.wsgi ```

1. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```
    
1. **Run server locally** with ``` python3 manage.py runserver ```


To setup a **virtual env** on **MacOS/Windows**:
1. Create a new folder on your machine
2. Rename it as you wish
3. For MacOS run in the terminal ```brew install git``` / Windows visit [Git](https://git-scm.com/download/windows)
4. Fro MacOS right click on the folder and select "New Terminal at Folder" / Windows right click into the folder and "GitBash here"
5. Creating a virtual environment: run command MacOS ```python3 -m venv env``` / Windows ```py -m venv env```
6. Activating a virtual environment: run command MacOS ```source env/bin/activate``` / Windows ```.\env\Scripts\activate```
7. You can confirm you’re in the virtual environment by checking the location of your Python interpreter: MacOS ```where python``` / Windows ```where python```
8. It should be in the env directory: MacOS ```.../env/bin/python``` / Windows ```...\env\Scripts\python.exe```
As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.
9. Leaving the virtual environment: ```deactivate```

Now that you’re in your virtual environment you can install packages.

1. Install Django with version 3.2:
    * ```pip3 install 'django<4'```
1. Install gunicorn:
    * ```pip3 install gunicorn```
1. Install supporting libraries:
    * ```pip3 install boto3```
    * ```pip3 install django-storages```
    * ```pip3 install psycopg2-binary```
    * ```pip3 install django-phone-field```
    * ```pip3 install django-crispy-forms```
    * ```pip3 install crispy-bootstrap5```
    * ```pip3 install django-countries```
    * ```pip3 install pillow```
    * ```pip3 install django-allauth```
    * ```pip3 install mailchimp```
    * ```pip3 install mailchimp-marketing```
    * ```pip3 install stripe```
    * ```pip3 install pysqlite3-binary```
1. Run ```pip freeze```
1. Create a project:
    * ```django-admin startproject <PROJECT_NAME> .``` (in the case of this project, the project name was "Kenpachi")
1. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` (in the case of this project, the app name was "cart", "store", "home", "checkout", "marketing")
1. Add a new app to the list of installed apps in setting.py
1. Migrate changes: 
    * ```python manage.py migrate```
1. Test server works locally: 
    * ```python3 manage.py runserver```
1. Check port 127.0.0.1:8000: (You should see the default Django success page)
2. Follow the steps from above to create the Heroku App and setting un the Settings.py file.

Documentation used can be found [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

[Back to Readme](README.md)
