Nightclubs in Madrid - Django Project

## Introduction
This project is a Django web application that showcases nightclubs in Madrid. As you join the webapp, it will feature numerous clubs in Madrid with their corresponding information(location, music type). You can search for a club and find its info, or if you want you can search for a music type and find all the clubs featuring that music and their info. If you wish to return to the home page there is also a home button. 

## Prerequisites
To run this project, you will need the following installed on your system:
1. Python: Version 3.8 or higher.
2. Django: Version 3.2 or higher.
3. MySQL: Make sure MySQL server is installed and running.
4. MongoDB: Ensure MongoDB is installed and the service is running.
5. Pip: Python package installer.
6. Web scraping dependencies: Libraries like requests, BeautifulSoup or any other library used in webScraping.py.

## Setup Instructions
### Step 1: Clone the Repository
```bash
git clone [your-repository-link]
cd [repository-name]
```

Step 2: Install Required Python Packages

```bash
pip install django mysqlclient pymongo requests beautifulsoup4 django-extensions djangorestframework python-dotenv django-cors-headers celery django-redis pytest pytest-django factory_boy django-allauth Jinja2 django-migration-linter django-compressor django-storages Babel

```

Step 3: Set Up the Databases
• MySQL:
  • Create a new MySQL database for the project.
  • Update the settings.py file in the Django project with the MySQL database credentials.
• MongoDB:
  • Ensure MongoDB is running.
  • Update the settings.py file with the appropriate MongoDB connection details.(username, password, database name...)

Step 4: Run Web Scraping Script
Before running the server, it is essential to populate the database with initial data from the web scraping script. We could have made it possible so that it webscrapes every time we run the server, but it is useless and means we need connection to the internet. Once is enough.
```bash
python webapp/webScraping.py
```
Make sure this script runs successfully and the data is populated in the database.

Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Step 6: Start the Django Development Server
```bash
python manage.py runserver
```

Step 7: Access the Application
• Open your web browser and go to http://127.0.0.1:8000/ to view the application.
