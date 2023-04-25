# Introduction

This document will guide you on creating your first Django application and deploying it on the cloud using Raillway.

The steps are:
1. Install Python 3 on your machine
3. Install Python Dependencies
4. Create a Django Application
5. Create a Raillway account
6. Deploy your application

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
4. Push your changes

## 3.1. Create your requirements.txt file

Make sure you are on the base of your git repository folder and run the following command:

```bash
python3 freeze > ./requirements.txt
```

## 3.2. Create your .python-version file

Create a new file called `.python-version` on the base of your git repository folder.

Run the following command to check the version of the python 3 interpreter you are using:

```bash
python3 --version
```

Copy the version string (i.e.: `3.11.3`) and paste it the file you created above. Save it.

## 3.3. Create your Profile

Create a new file called `Profile` on the base of your git repository folder.

Paste the following line on it:

```bash
web: cd ./YourProjectName && python manage.py migrate && gunicorn YourProjectName.wsgi
```

**WARNING:** Replace `YourProjectName` above with the name you gave to your project when you created the Django application.

Save it.

## 3.4. Push your changes

Now you should have a lot of changes that you need to add, commit and push to git. Make sure you are on the folder of your clonned repository and run the following commands:

```bash
git add .
git add -f ./.python-version
git commit -m "Initial Project Setup"
git push
```

# 4. Create a Raillway account

# 5. Deploy your application

