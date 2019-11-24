# README - Movie_Blog Database Project | Milestone-3

## Issues

Setting up and configuring the Virtual environment has been very difficult. At times, I could create a venv(virtual environment) and work away no problem. However, when I returned to the code after closing out and re-activated the venv `source bin/venv/activate` it would open within the venv but dependencies where not all present and this appears to have been some sort of artefact from the venv that was opened? Sometimes it appeared to be a new venv or a sub one within the original.

After setting up an SQLite3 account and database to test my queries, I succeeded in this task. Then when I tried to convert code over to using a MYSQL database the import code would throw constant errors. `from flask-sqlalchemy import SQLAlchemy`. The importModule not Found error kept appearing with a pylint warning. Both of these modules where showing within the `pip list` of the venv! My researching of the issus suggested it was an issue with the Path to the venv for the interpreter?

1. Top paragraph seems to have corrected itself by following commands correctly `source venv/bin/activate` inside the root directory/folder. Now `pip list` is working and app is running. This has also for now corrected for the fact that the `from flask-alchemy import SQLAlchemy`!!

2. The issue then is certainly in the initial setup and configuration of the interpreter within the venv??

## VENV

Issue has resolved. No longer having problem accessing stored virtual environment. Still may be an issue when setting up a new configuration, we wait and see?

## Login Page

Adding basic login page for users to login through. Going into the directory that housing my app (root folder). `source venv/bin/activate` to engage venv. Add route (decorator) and build out function `login`. The route will need a list of methods added: `methods=["GET", "POST"]`. Then create function login and set `error=None` followed by a return render_template. Not handling post just an error. Needs to add conditional logic here `request.method`!

Created login.html template and added to templates folder. I then put a route together in app.py file. The login page was a simple bootstrap form with two fields. Username and Password. The route was set up with conditionals to test against these inputs, if false, user would get an error, if correct, user would be redirected to home page. Built and ran the app, checked dev tools and got 302 HTTP response for my POST request and then a 200 reponse when credentials were correct. All working well.

Included some jinja2 logic into page with an error message that was passed to the HTML through the routing fuction `return render_template("login.html", error=error)`.

This is only for one user and is not a protected route. YOu can access it without being logged in and as such defeats the purpose. Therefore, I shall not only modify this behaviour but also add in some form of notification to the user that will tell then when they are logged in themselves.

The tool to be used for the above will be Flask-Login for handling user login sessions. If the session user is logged in then page will redirect to home page `session["logged_in"] == True`. Then we must also add a logout functionality to the app and notify users when this case is true. This will require its own route: `@app.route("/logout")`. And when a guest is sent to this route we will simply pop the value of true back to `None` and the user will be logged out of the session by way of the session `logged_in` key being deleted.

This functionality would then require a secret key as sessions store the data, unlike cookies. We are just initially setting the secret key within app.py and as such is not random nor is it in another separate configuration file. These issues will addresed later.

Added in for loop with `get_flashed_message()` function to the HTML page for adding our various user messages and allow us to get greater control of them for styling purposes later. Also added this to the login page too. These have been built and tested well. There are now two messages responses showing on login page but that will be corrected for shortly.

Imported `wraps` from functools to increase security, this allows for a login_required(f) to be added in app.py. This code was recognised and taken from advice in [Real Python.com]("http://realpython.com) video tutorials. Thank you Michael Herman.

### Jinja Templating

Set up templates folder. Goal is to move duplicate HTML code in a parent template to be reused - injected into a page. We call this parent base.html.

The extends tag `{% extends "base.html" %}` at the top of each template tells the templating engine that this - the current template is extending the code from the base template and then just adding / injecting new HTML into the area between where we place our `{% block content%} {% endblock %}` logic blocks. We can use any label here with "block" as long as we are consistent and use the same label / tag name in our receiving template.

Added the base.html and replaced all redundant HTML in other templates. Tested to make sure app still runs, error and flash messages still work when required and got healthy 302 and 200 Http requests. All is working well.

### Databases

I will create a git save point here as I am going to test setting up a database. This will be done by using plain SQL queries using a simple SQLite DB to test my set up. After which, if this is successful, then I will transfer over to setting up my database with SQLAlchemy and PostGRESQL.

Initially I will use SQLite database browser so as I can interact with my data and check it is storing correctly. I have also downloaded SQLite3 to my local machine for running this code and passing it to the database.

After importing SQLite3, I create a connection: `with sqlite3.connect("moviemagic.db") as connection:` and then set up a cursor connection with which to execute my statements. At first, I will simply create a moviemagic database with one table called 'movies'. I will give it a title, director, genre and description columns and then fill some generic data into those fields.

All tests worked well. I even added and updated another column from within the SQLite3 shell. You can activate this, if you already have it downloaded by going to your terminal and typing `python sql.py` and it will run the file and open a shell for you to work directly with the database.

**\* Enter sqlite3 database screenshot here for evidence \*\***

I then imported SQLite3 within my app.py file and added another configuration variable too. `app.database = "moviemagic.db"` and then we added in a function that would connect to our database - create a database object that we could interact with:
`def connect_db(): return sqlite3.connect(app.database)`

Insert image of screenshot of running the database app from within python shell successfully.

First attempt failed. Not entirely, the database was queried and we got a return but our formatting was defintely off. See image for result:
**_ place image in here - database error _**

The sqlite3 tests worked well. **_ show image of database data displayed on the index page _**. The line of code that casts our fetched data to a dictionary:

````[dict(title=row[0], director=row[1], genre=row[2], description=row[3])
              for row in cur.fetchall()]```

After which, I close the connection `g.db.close()` and pass the 'movies' variable data, our fecthed dictionary list, to the rendered template, to be injected into the HTML. Jinna2 logic was then used on the index page, in order to render the data in a basic but user friendly way. When the larger PostSQGRESQl database is wired up, this same layout will pretty much the underlying foundational code before I UX the nuts out of it with some super styling!! ****
````

`{% for movie in movies %}` templating logic used with templating variables `{{ movie.description }}`. The movies in the former logic statement is dictated by the curly braces with modulo symbols inside them. While the variables themselves are coded out using double curly braces with a dot notation logic flow.

### Data Structures

When defining a data structures, you must first explicitly state what kind of structure you want it to be. Only after which you can tell the engine what data to begin to place inside that structure. First you must know your grammar(data), following this, you decide what is the best, most effecient way to construct the data, therefore, you use your logic(data structure), what to put where, and with what label. Finally, you use rhetoric(query statements) to grab or upload the data you wish to work with and pass that to the routing function - deocrator / url to inject the data into your HTML for presentation layer styling.

The original code before refactoring was more human readable but not as concise.
`movies = [] for row in cur.fetchall(): movies.append(dict(title=[0], director=[1], genre=[2], description=[3]))`
Basically, define your list object, then use a `for` loop to iterate over the results from the cusor's fetchall method. Next, append a dictionary object onto the 'movies' variable by assigning a row label with its indexed position. And then close your connection as earlier stated.

### Testing

Flask comes with its own testing suite, right out of the box. This is an important feature, especially for more novice developers to test out their code early on and try get ahead of a lot of the bugs before they occur, because they will occur! This unit testing is also good practice for learning some more fundamentals of your code logic and allows for the developer to really think about his code and how they want it to read and perform. Questions, such as, what am I trying to achieve here and how do I want my end user to see or experience what I want to display to them. What access should be given to a user? How is my data being transferred, what messages or signs can I see and display to myself as a developer to assist me in understanding what way my data is being moved around and presented?

In general, you write tests to check the reponse for correctness. This is testing at its most fundamental level. I wish to do this - that is what happened, etc,. Its like an isolated app that we can send rsponses to without affecting the actual real app. We start by testing if we get a 200 reponse from the request when attempting to open our index page, does the url connect?

The first test for a 200 response was succesful **_ attach image of such here _** (200-reponse-data).
The beginning of each test function 'must' start with the word 'test' so that Flask knows that this is a test function. Irrespective of the fact that this code is being run from a file named; 'test.py', it is still neccesary to specify to the python engine that the function being run is a test function only.

The second test using the `test_login_page_loads` is self explanatory. It tests that when we get to the login page, the user is greeted by a text of "Please Login". This is denoted in the `selfassertTrue()` method by use of the "b" flag to indicate that what follows is text and that will be found in the `response.data` that is returned from the page HTML content. The spelling and upper or lowercase is important here as any deviation in these will result in a failed test, whereby, the error is in the spelling and not the test or the logic! Be careful.

The proceeding tests will dive deeper as we move down into the code base and its more detailed usage cases.
WE don't know with only a 200 response that the right template was rendered. We only know a successful url call was made - request returned, but to what page. Therefore, we needed to test the actual data on the page we want to know it was an accurate request status.

I will test for login behaviour with correct and incorrect credentials. This can be done by checking not only the responses sent back but also you to simultaneously test your error messaging is set up correctly too. Then we move our way down the line to test if the logout page behaves properly as expected...

The word "test" needs to be placed at the beginning of each test function, otherwise unittest will not pick it up as being part of the suite of tests. In addition to this, our test for the main login page must follow the redirects to check for a 302 reponse to make sure that users are brought back to the login page and told "You must login first.". We also need to write a test to ensure that our movies show up on the main page. I built tests to check for all 3 of the original Director's names that I used in my initial data. These tests were all successful too. This is not typically best practice. If the data that we tested for is removed from the database, then this test will fail future tests. In real world, we should be running tests to a designated test database. That way we can test writing to the test database to make sure it all works correctly. I will, if given enough time, return to this issue a later time and rewrite some of these tests to follow best practice!??

After the first 6 tests have all been run successfully, I notice that there is quite a bit of redundancy within the code. Therefore, I will attempt to clean up that code, in order to make it dryer (Don't Repeat Yourself) using some helper functions! Refactoring will be returned later in the development process.

### Deployment to Heroku

Gunicorn is a web server that works really with Flask and is good practice to install this in our app before deploying to Heroku. I will initially deploy my smaller, SQLite3 database run app to Heroku and then build out the app with the larger PostGreSQL database later. The purpose of installing gunicorn is that it allows you to test out your application locally. Instead of using just the regular development server. To do so just run command: `gunicorn -b 127.0.0.1:5000 app:app`. First, we are calling gunicorn, then we use the "-b" flag to "bind" the app to the local host, while optionally adding the port number. Then finally, we must specify the project and app name, both of which are the same in this case "app".

Add gunicorn-test image here to prove test of web server success **_ image here _** All data is displayed correctly and all is working as it should.

Next we need to set up a Procfile. This file is required by Heroku in order to know how to execute our application. We basically need to tell Heroku what kind of application it is and how it should be run. This is a pretty simple process. We run the terminal command `touch Procfile` to create the file. Always use a capitalized 'P' and there is no file extension. This is how Heroku will know to recognise and find the file. This file should be in your root directory. Each line contains a different command starting with the name of the command itself. This is then followed by a colon and proceeded by the actual commnad to be run, e.g. `web: gunicorn app:app`. We do not use the "-b" option flag to bind to a local address as this will all be done on the Heroku side.

Then we need to specify the dependencies with "pip". We do this using a requirements.txt file. In order to create this, we use the `pip freeze > requirements.txt` command and this will create the file with all of the current dependencies used to create your application at this stage. Remember, anything you add from here on out, new functionality that requires new modules to run, will have to be added to this file and pushed to Heroku, otherwise, it will not know how to build and run the application properly. Any dependencies that are added later on, can be added this file through running the same "pip freeze" command as above. The first time you run that command, it creates the file but every time you run it thereafter, it simply updates the file, if it has already been created.

Typing just the `pip freeze` command in the terminal will then print out to the console what dependencies you have install, so as to confirm they are all present. Once this check has been run, we want to store our application on the local git repo. This is a matter of running the `git init` command to install git. However, before we store of all this in our local repo, we need to add a .gitignore file that will take all those files that we do not wish to push out to our remote repo where important security information like our "environment variables" will be seen by other developers. After we have created this ".gitignore" file and stored our necessary files there. We will add our "venv" folder and any compiled python and database files so as not to add them to Heroku. Our currect database will also not be stored on Heroku as we will create the larger database for this later on Heroku itself.

We then run our `git add .` command to add all of our files, followed by `git commit -m "Initial commit"`,which is the common industry practice for our first commit. And finally, we do a `git push heroku` to push our code repo up to Heroku. Once this has been done, our app is now sitting on the Heroku platform and we can check its functionality by running `heroku open` command and we should be redirected to a web page with our application running correctly. This initial push will take longer than later pushes as Heroku has to create the application on its servers with all its dependencies.

After which we can add a dyno to our app. The command to spin up a Dyno is: `heroku ps:scale web=1`. Dyno's are specific to Heroku. It basically allows us to run processes. Our above command is telling to Heroku to run one web command, as it states in our Procfile and that it should use 1 Dyno for that process. Then we run `heroku ps` to see our currently running processes. **_ successful spin up of dyno added here _**. By running just the `heroku` command in your terminal, this will bring up the help menu with all your available commands there.

We can now also run our unittests from heroku. `heroku run python test.py -v` will run these tests for us on the platform. The "run" command will run whatever we specify after that keyword, in this case, we want python to run the file where the unittests are stored, "test.py". The "-v" option flag at the end is only necessary to see the test output for each test in the console, which makes for easier human readability of which of the tests failed, if any.

This initial test failed. The final test at this stage, the one testing for the some data from the movies data displayed on the index page. However, now the database is not being hosted on Heroku, we have added it to the .gitignore file remember, and as such, the data from our database is not being displayed on the index page any longer so this test failed as expected. We should now consider changing this test to reflect the current state of the application while running remotely on Heroku.

### Setting up SQLAlchemy Database

We must now set up our SQLAlchemy database locally and on Heroku. After which, we can re-establish the database connection to our new database and test against it. SQLAlchemy is a powerful abstraction layer and Object Relational Mapper (ORM). Most ORM's increase productivity because you don't have to switch languages. There is also the advantage of portability. SQLAlchemy is a high-level ORM. You can abstract the databsae engine making it easy to switch from SQlite to PostGreSQL, kind of! There is slight decrease in performance with using it but productivity gain makes up for this.

Flask SQLAlchemy comes with a number of preconfiguration right out of the box. We start by installing the engine using "pip", `pip install Flask-SQLAlchemy`. Make sure venv is running first so that its installed within that environment. Then we recreate our database schema using SQLAlchemy.

First we add a file to the root directory named, "models.py". Enter `touch models.py` into the console to create this file. Then we open up this file and attempt to translate the SQL commands over to Objects for the models.py file. We are migrating our schema and data over from SQLite at this stage. We begin by importing our database over from our app.py file, `from app import db` (this will be created shortly).

We then create a new "class", and we will name this "MoviesCollection". This class inherits from the database model so include this as an argument, `class MoviesCollection(db.Model):`. Then we define our table name and create the resources / columns with their respective labels. We are creating our database schema. The schema had already been decided when we created and tested our app earlier using SQLite, so we can copy that and adjust it here. We then initialize our database schema with the `__init__` function and finally we add a representational function just to tell the engine how to present our data within the Object.

The configuration of the database is handled with the code, `app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///collection.db"`. After which, we create the SQLAlchemy object with `db = SQLAlchemy(app)` this line of code and finally, we comment out our earlier connect.db function that was pointing us towards that SQLite3 database. The congfiguration should then be set up so we can use SQLAlchemy to manage our database.

The db_models.py file will contain our new creation code. We first import the database from our app and then our collection from the models.py file. There is one command to create all of our tables in the database from our models.py class created object, `db.create_all()`. The insert method is called using `db.session.add(MoviesCollection(...))` and adding in the data required for the appropriate fields.

Insert shell test showing the new database is not only up and running but we have inserted / added data to it from the shell **_ insert sqlalchemy shell test image here _**

We will now need to update our home function as it is no longer using SQLite3 to query our database. This will require deleting our try / except code for starters.

### Problems

We have to import the data collection from models.py but we must do so after creating the sqlalchemy object. However, the editor will just not allow me to do so? No matter what I try, the editor automatically moves the import to the top of the app.py file and this causes the issue!!

#### Database Issues

In order to attempt to solve the issue with importing the Class from 'models.py', I shall restructure my project now, creating multiple packages, rather than using modules. The hope is that this will resolve the import issue for the SQLAlchemy database 'Class' module.

When Python imports a module it runs the entire module, this is causing the issue. Its a circular loop. Python is looking for the db variable that it has yet to see and is all out of sync. If we run it directly from the terminal, Python call the app.py '**main**' but it hasn't seen the 'User' class is because it is below the Models import!!

To tell Python, 'something' is a package, we need to give it a `__init__` file. I will initially create a folder in the root directory with the same name as my database, "MovieCollection".

"app.py" will now be renamed to "run.py" as it has had all its code removed, with the exception of the main if statement to run the file. That is its only job now, to run the application, therefore it makes more sense to rename the file as "run.py".

## Pagination & Routes
Pagination is set up to show only current page - highlighted and then the first and last page as well as the previous and next pages. The rest of the links are highlighted by an elipses(...). This is in case there eventually is lots of pages and posts. The posts show the username of the person who posted them, author and this displays as a link. If clicked on, I want this link to pull up a page with only those posts created by that user.
