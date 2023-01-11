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
    * django-admin startproject <PROJECT_NAME> (in the case of this project, the project name was "Kenpachi")
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
    * Select "Mini - $5.00 USD" from the "plan name" drop-down menu and click "Submit Order Form."
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.
