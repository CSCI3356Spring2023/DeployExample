# Introduction

This document will guide you on creating your first Django application and deploying it on the cloud using Raillway.

The steps are:
1. Install Python 3 on your machine
2. Install Python Dependencies
3. Create a Django Application
4. Create a Raillway account
5. Deploy your application

# 1. Install Python 3 on your machine

There are many web sites that explain how to install python on a variety of platforms (Windows, MacOS, etc.). You google it yourself or try [this one](https://realpython.com/installing-python/).

# 2. Install Python Dependencies

Our application is going to be based on the Django Web Framework. The Raillway cloud service uses gunicorn web server as its WSGI (Web Server Gateway Interface). Run the following command to install these dependencies on your machine so we can run our application locally in the same Raillway does:

```bash
pip3 install gunicorn django
```

# 3. Create a Django Application on GitHub

Pick a name for your project. In the instructions below, I will use the name `YourProjectName`. Replace it with the name you have chose where appropriate.

Create a new GitHub repository for your project called `YourProjectName`. Clone your new Git repository on your machine and change to this folder.


Create your first Django application by running the following command:

```bash
django-admin startproject YourProjectName 
```

**WARNING:** Make sure you replace `YourProjectName` above with a name of your chosing.


Now you must do three things in order to run your application on the Raillway service:
1. Create your requirements.txt file
2. Create a file called .python-version to indicate the version of python you are using
3. Create a Procfile to tell Raillway how to start your application
4. Change your setting.py files
5. Manage statics
6. Push your changes

## 3.1. Create your requirements.txt file

Make sure you are on the base of your git repository folder and run the following command (if you are using a Mac/Linux machine):

```bash
python3 freeze > ./requirements.txt
```
If you are using a Windows machine you have to use pip or pip3 (if you have multiple Python versions):

```bash
pip freeze > ./requirements.txt
```

Be careful, if you didn't create your project as a separate environment in your machine, this may generate a file that has all modules/libraries that you have installed in your computer. And this may bring issues.

## 3.2. Create your .python-version file

Create a new file called `.python-version` on the base of your git repository folder (no file extension).

Run the following command to check the version of the python 3 interpreter you are using:

```bash
python3 --version
```

Copy the version string (i.e.: `3.11.3`) and paste it the file you created above. Save it.

## 3.3. Create your Procfile

Create a new file called `Procfile` on the base of your git repository folder (no file extension).

Paste the following line on it:

```bash
web: cd ./YourProjectName && python manage.py migrate && gunicorn YourProjectName.wsgi
```

**WARNING:** Replace `YourProjectName` above with the name you gave to your project when you created the Django application.

Save it.

## 3.4 Change your setting.py files

Next, we need to make some adjustments to our settings.py file
Look for the line that has

```bash
ALLOWED_HOST = [ ]
```

and change it to:

```bash
ALLOWED_HOST = ['*']
```
also add the lines below:

```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
```

Look for the line that has:
```bash
DEBUG = True
```

and change it to:

```bash
DEBUG = False
```

Look for the line that has:

```bash
MIDDLEWARE = [
    ...
]
```
and add the following line above all other middleware lines apart from Django's SecurityMiddleware. It should look like:

```bash
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
```


## 3.5. Manage statics

Make sure you are on the base of your git repository folder and run the following command to collect our static files into one folder:

```bash
python manage.py collectstatic
```

## 3.6. Push your changes

Now you should have a lot of changes that you need to add, commit and push to git. Make sure you are on the folder of your clonned repository and run the following commands:

```bash
git add .
git add -f ./.python-version
git commit -m "Initial Project Setup"
git push
```

# 4. Create a Raillway account

Follow the steps on the link below to create your Railway account:
https://docs.railway.app/reference/accounts

# 5. Deploy your application

Connect your Railway account with your GitHub project repo:

![image](https://user-images.githubusercontent.com/289918/234321635-0ab4fc75-3363-4a97-a7c5-39a84b4a7885.png)


Select your project repo:

![image](https://user-images.githubusercontent.com/289918/234321762-a55aea27-37c0-4cfe-b651-6365d34ae0c8.png)

You will see this, it means that Railway is running everything you said it needs to have to be able to run your project:

![image](https://user-images.githubusercontent.com/289918/234321844-897452df-5e2c-474a-8712-520e35788a5e.png)


When you click on the left "widget" that has your project name, you can see how things are working.

![image](https://user-images.githubusercontent.com/289918/234321928-ab9961e5-46f8-4473-b10a-c33b7802454b.png)


Click on the settings tab (screen below), in the middlle of screen there is an option that says domain. Click on generate domain.

![image](https://user-images.githubusercontent.com/289918/234321992-dc66cd92-a88a-46da-86d5-0db094555b1c.png)

When you click on generate domain, a web address will appear: 

![image](https://user-images.githubusercontent.com/289918/234322073-bb8dee18-1ae6-41ee-bbf0-cab8880dfb07.png)

This web address is your project deployed address.

Look at the web address that Railway gave you, let's say that mine it was: `https://your-base-domain`,

Go back to the settings file on your project and add the following lines, with the web address that Railway gave to you:

```bash

CSRF_TRUSTED_ORIGINS = [
    'https://your-base-domain'
]
```

You are done deploying your project.

If you have issues with your deployment, go back to to deployment and click on the buttom that says view logs. This will show you the same logs you can see in your machine and you will have to google the message to try to sort it out the issues you have.

![image](https://user-images.githubusercontent.com/289918/234322160-e81aa13b-6f15-4786-a160-a389517b80d9.png)

