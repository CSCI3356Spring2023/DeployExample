# Deploy_Example

Heroku provides a [good tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) about how to deploy python applications in their cloud. 

This document presents a summary of the steps.

## Make sure you have an account at Heroku

Go to https://www.heroku.com and signup if you don't have an account yet.

## Installing Heroku CLI

On your mac:

```bash
brew install heroku/brew/heroku
```


## Clonning the GitHub repository for this App

Clone this repository:

```bash
git clone https://github.com/CSCI3356-Spring2021/Deploy_Example
cd ./Deploy_Example
```

**WARNING:** From now on, all commands bellow must be run from inside `Deploy_Example`.

## Creating an application

Now, change to the `Deploy_Example` folder and create a new app on your heroku by running the following command on your terminal:

```bash
heroku apps:create
```

This action must be done from inside the app source folder so that Heroku can link your source repository to your app.

Make sure you have the following files at the root of your app source folder:
* `runtime.txt` - Tells Heroku  the version of Python that you need
* `Procfile` -  Tells Heroku how to start your web app.
* `requirements.txt` - Tells Heroku what libraries must be installed 

## Push your main branch to the heroku origin

The previous command created a new origin in your local clone of the repository called `heroku`. Everything you push to that new origin is automatically deployed in the heroku cloud for you.

Let's now push the source and get the application deployed:

```bash
git push heroku main
```

After this command, you will see a lot of output like this:

```bash
Enumerating objects: 490, done.
Counting objects: 100% (490/490), done.
Delta compression using up to 12 threads
Compressing objects: 100% (217/217), done.
Writing objects: 100% (490/490), 86.40 KiB | 86.40 MiB/s, done.
Total 490 (delta 242), reused 490 (delta 242), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Determining which buildpack to use for this app
remote: -----> Python app detected
remote: -----> Installing python-3.9.4

...

remote: -----> Launching...
remote:        Released v5
remote:        https://lit-cliffs-36797.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/lit-cliffs-36797.git

```

Wait until heroku gives you the URL for your deployed application like the example above.

## Scale the App to 1 Web Server

Make sure you have at least one web server serving your app by running the following command:

```bash
heroku ps:scale web=1
```

## Visit your App

You can now open your app with the URL you got before. If you did not save the URL, use the following command:

```bash
heroku open
```

## Remove your application from your Heroku account

```bash
heroku apps:destroy
```

