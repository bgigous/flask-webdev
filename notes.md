Begin Notes
===========

Hello web world:
    Try making more routes
    Try putting some html in (headers, links...)
    what if we return a number

Forgot
======
`moment.include_moment()` in base.html until user profile
LinkedIn uses Flask

Homework Ideas
======
`moment.include_moment()` in base.html until user profile
LinkedIn uses Flask

Some Template Stuff
===================

I added a function with no route, that's probably something a student would do
and I tried rendering template without importing


in your jinja templates, you can try some filters! safe capitalize ...
should I introduce jinja macros?

You can use template inheritance ("extends") to define blocks that can be overridden by derived templates
or you can store common html in a separate file and "include" them to avoid repetition

I used {{variable}} in a {% %} block and it was syntactically wrong

Use `{{super()}}` in template `block` to inherit the base template's `block`

Miguel has:

```html
    {% block head %}
    <title>Plaza - {% block title %}{% endblock %} </title>
    {% endblock %}
```

But I don't know why because this:

```
    {% block head %}
        {% block title %}
            {% if shopper_name %}
                Shopper {{shopper_name}}
            {% endif %}
        {% endblock title%}
    {% endblock head %}
```

doesn't work. it will put Shopper whatever in the html doc

after extending base.html, I try putting content after blocks title and head (not in a block) and it doesn't show
putting it in a block does allow it to show

comments screw things up if before jinja (the `<!--` kind>)

the reason we don't have bootstrap is BECAUSE I LITERAlly HADA no inteERNET
Try some other bootstrap template blocks!

Pasting base.html template from microblog git repo

Navbar isn't showing up (nor is title inheriting) because: I was not inheriting from base.html but rather bootstrap/base.html

CSS Styling is missing for bootstrap in base template which has a navbar. ultimately because of `block head`...

Error Handling
==============

error.html inherits from base.html but it won't add margin to the content... Oh, it's not a page_content which is why

Forms
=====

The templates we made go from server to user. Great for getting information _to_ us, but obviously we need to tell the server stuff, right? GET is server -> user, POST is user -> server. These things are called requests. POST requests give server access to user information, like login info and personal details and favorite flavor of ice cream.

Making form components with HTML is straightforward, but then there's validating. And then how the heck do we make sure the user input is valid? For example, "wood" isn't exactly a flavor of ice cream... and hang on, how do we connect all this to python???

For that we have flask-wtf! It makes making forms easy! (Don't let the name fool you)

Secret Key
----------
But there's one quick thing we need to do first. If I want complete secrecy as to my own fav flavor of ice cream, to only confide it to the server, the framework has to make sure the data sent is *encrypted*. introducing the secret key (we'll add in configuration)
(use external links to encourage students to dive in further)

(be able to explain what the FlaskForm/Form class definitions mean/ the breakdown)

Templates
---------

Alright, now let's define the form "look" in a template
Remember the long spiel about security? There's a little more to do: hidden_tag() is needed for Flask-WTF to implement CSRF protection. Basically, you'll want to include it because it's important! Blah blah blah

You can even define ids in your form so that you can define CSS styles for them, within the template

To make our life easier, we're gonna use Flask-Bootstraps predefined CSS styles. That way, we don't have to cringe at a form that looks like it came from the Internet of the 90's, we can have a cool modern look right outta the box (`import "bootstrap/wtf.html" as wtf`, `wtf.quick_form(form)`, `form` is a variable, and we don't have to define the form fields individually)

GET and POST
------------

Wait a sec, what's with this "Method not allowed" message? Of course it's allowed! I just put the form in there! Oh, wait. It's talking about the [what GET/POST things are called] methods! Let's add those to our route decorator. view functions are only GET by default. More about POST... And upon POST, what happens with the `validate_on_submit` and validation...

Redirects and Message Flashing
----------

We never want to repeat a form submission if the user refreshes, so we'll prevent that with a `redirect`

As you can see with the redirect, hitting refresh after submitting the name doesn't trigger an alert. On top of that, the way we've done it, we can actually visit a different page, then come back and see our name is still there! (Verify this is true, and false otherwise)

Putting flashed messages in the base template ensures you don't have to repeat putting your flashed messages into other templates. And we use a loop because there might be more than one message to display at a time

Database Management
===================

What's a model? A model is basically [I need a way to describe this...]. The models are the objects that your webapp interacts with to get the data it needs and update data as needed. If say a user logs in , the webapp will need to load the information on the user so that the user sees nothing but what they expeect for the app.

If they register a new account, that means you'll add that information to the database. There are lots of other info that needs to be tracked with that user. The great thing about relational databases is that *relationships* can be formed between the data. Each user will have a *role* in the application, and that relationship between role and user can be defined with [].

SQLAlchemy vs Flask-SQLAlchemy
------------------------------------

Installation & Configuration
-----------------

Defining the Models And Their Relationships
-------------------------------

There are many relationship options you can use, and each has a different behavior/use case. (Try some in a lab)

create_all() can't be called again if the models need to be changed because the tables already have the old columns. To force a change in columns, you can call drop_all() and then create them all again with create_all(), but that removes any data you have!

But don't worry, there's a way to update your models without destroying all the information that exists! We'll discover this magical solution together later, but for now let's talk about how to get data in the tables in the first place.

Interacting With Our Models in the CLI
----------------------------------------------

To do that we're going to use the convenient `flask shell` command to interact with our database one command at a time (what?).

(Do you need a backref to a foreign key in the other table?)

for inserting users into our database with sample usernames, []. "Note that the role attribute can be used, even though it is not a real data‐
base column but a high-level representation of the one-to-many relationship."

The id attribute of the new objects haven't been set yet (paraphrased), and it's not explicit or doesn't have  to be because ids are set automatically. Check it out: `>>> print(manager_role.id)`

However, we haven't inserted these values into the database yet. We've only created the objects. That's why they haven't been assigned. Lets go ahead and put them in the table.

Before we do that, understand that values must be inserted in the [context or something] of a database session. This way you can line up a bunch of commands to execute, and when you're ready to actually insert them, you'll `commit` those commands. let's get the values ready

```
[add commands]
```

(don't forget about lazy)

we could also have done `db.session.add([...])`, then commit()

(Probably good to explain the difference between the flask session and db session)

Try to commit only related changes in each commit, that way you won't run into as many errors (explain this)

Modifying rows is simple, just take the same object (manager_role say), change its name attribute, then just add it again and commit. To delete any data, like the owner role (not mentioned yet), just issue a session.delete(owner_role) and then commit. Notice the pattern here? (commit)

Now how do we see what data we have in the database? We can check each table with the convenient `query` object. To just see all of the data per table, we do a `query.all()`. (The query object is associated with each `Model`! not the db itself)


We can use `filter_by()` to find users with specific roles, say just shoppers. `Shopper.query.filter_by(role=shopper_role).all()`. Notice we have to use all() again, as just using filter_by gives us a `BaseQuery` object. weird huh? (why is that??)

Ooh, here's something fun. This is what basequery means, essentially a sql command. Watch:

```python
>>> str(filter_by())
'SELECT ...'
```

So if you were curious what FS is actually doing, this is a great  way to see. Alright let's get outta here `exit()`. I know you might miss those python objects, but don't worry, their legacy still exists in the database object!

So since we're exited, we really miss those python objects. It's real easy to get 'em back by `shopper_role = Role.query.filter_by(name='Shopper').first()`. Since we know there's only one shopper role, we don't need to use all(), instead we can use first(). Check out these other query filter functions: [list em, filter, filter_by, etc]

Then once you have a query object from one of those, there are different ways of getting the data that comes out. Check out theses other "executors" (not as deadly as it might seem): [all, first, get, etc]

Trying Out Our Models in a View Function
----------------------------------------

Database Migration with Flask-Migrate
-------------------------------------

Alright, so our problem earlier... So of course we need to add more columns to our database models so that we can build our app. But the problem is, so far, to do that we have to drop all tables and our data goes away. To fix that, we'll support "migration" which is a fancy way of saying, "Make scripts that can make the necessary changes to the database, and that can also _move_ the data to we already have as needed." Or something. It keeps track of how the database schema changes.

(Does sound kinda cool right? See the data in its natural habitat, doing its migrations as usual. I was inspired by that one NG guy's voice)

`pip install flask-migrate`

add Migrate and init it in our python code, like so []. After Migrate installs, it adds a `flask db init` command we can run in the CLI. Run it now, k?

You'll see that it creates a migrations directory, that's where all the migration scripts are.

When And How to Perform Migrations
---------------------------------------------

in Alembic a migration is represented as a migration script. Al has two functions called `upgrade()` and `downgrade()`, and they apply the database changes that are part of the migration and removes them, respectively. (am I grammaring right?)

The procedures that one must follow in order for a successful migration:

1. make changes to the model classes
2. create an automatic migration script with `flask db migrate`
3. review the script, adjust it so that it acc reflects changes made to models
4. add the script to source code (!)
5. then run `flask db upgrade` to apply the migration

    "For a first migration, this is effectively equivalent to calling db.create_all(), but in
successive migrations the flask db upgrade command applies updates to the tables
without affecting their contents."

Make sure *ALL* changes to your models are reflected in your migration scripts! Otherwise any `upgrade()` commands won't reflect what changes you ultimately made (and the result might look strange).


Pretty much everyone goes shopping. Except maybe not your Uncle Steve, who fends for himself out in the woods and hunts his own food. Anyway that's why all users who sign up are "Fans"

I ADDED FLASK_APP=ragtime.py TO BASHRC SCRIPT FOR CONVENIENCE

*[Skipping email for later]*

Scaling Up
=========

Work through config, then __init__.py in app, then main/__init__.py blueprint, then __init__.py again to include main blueprint, then errors in main blueprint, then views in main bp, then the ragtime.py to create_app()

Project Structure
---------

Basic Configuration
------------
now we introduce the config class. Or should we say classes. Flask allows us to load a configuration as a class, which means we can create a class and define CONSTANTS within it to pass our settings to the app. We can even put multiple configuration classes inside a file and use a dictionary to "name" each one. In our case These names are actually values we define in our factory, which you'll see later (that last sentence might not be quite right)

We'll define more configurations later.

Application Factory
------
we make a folder app and putting most of the files in there because this is the way of the app factory. It uses the factory pattern aka the `create_app` function. we're making a flask app inside a package. with this factory, we can put in any configuration we want and get out a flask app that uses that configuration. the only drawback is that we can't change the configuration dynamically anymore. Our package is called `app`. This encasulates everything in a folder, and we can load the config from outside.

Blueprints
---------

for error handlers in a blueprint, we must use `app_errorhandler` decorator for app-wide error handling

Creating the Main Blueprint
-----------------------------

the `url_for()` must change to either "main.index" or ".index"

Made main/__init__.py because that's where the Blueprint is born. imports views and errors from there. We'll use this module to register our blueprint later

views and errors.py go in a folder `main`, as well as our form class. These views, error handlers, and forms are all part of the blueprint. Theoretically, our blueprint is in a dormant state until we register with our flask app. It's a bit like a keyboard or mouse, where the devices are dormant until we plug them into the computer. So once we register our bp, our views come to life! Error handlers actually need the `app_` to make them work app wide. We import our form in the views module. Note the `main` folder is also a python package, but it's within a package

More Configurations
-------------------------

production development testing

Laying the Foundation for Future Work
-------------------------------------

User Authentication
==========================

Will not use login_required decorator in this section, doesn't make sense to restrict users to plain pages (we don't have fan page yet, let's say)

##### how flask-login works
1. user clicks "Log in" to navigate login page and is presented (by the handler for the URL) with the form
2. User enters info. Upon Submit, same handler is invoked again, but now as a POST instead of GET
    a. Handler validates the creds, then invokes `login_user()` to log user in
    b. login_user() func writes ID of user to USER SESSION (not a const) as a string
    c. view func returns with redirect to homepage
3. browser receives the redirect and requests home page
    a. view func for home is invoked, triggers main Jinja2 template
    b. during rendering of template, a reference to current_user appears for the first time
    c. current_user context variable then invokes `_get_user_()` to find who current user is
    d. `_get_user()` function checks if there's a userID stored in user session. If there's none, returns instance of AnonymousUser. If there is an ID, the `user_loader` decorated function
    e. user_loader handler reads the user from the database and returns it
    f. template receives the newly assigned value of current_user

I'm thinking "Fan" will be confusing at first so I might want to use User for everything else...


##### for testing
Made a tests/ folder for pytest tests. Only had to use `python -m pytest tests/` and then fix the import/module errors to get it to work

NOTE cannot really use `pytest` as the above works well

Fixtures go in conftest.py. Their scope can be defined using `@pytest.fixture(scope='function')` or "module/session/class"

##### more notes on user auth

Password security is no joke because if a breach occurs on your app, you could expose your users' passwords to the attackers. Lots of users use the same password for multiple sites, so that's trouble. So how can you protect your users easily, but effectively?
=======
Need to explain why the development vs production setup is the way it is

brief intro on testing? at this point?

Password hashing is a common solution to this problem. a hashing function takes a plaintext password as input, applies some randomness to it (the salt), then applies several one-way crypto transformations to it. What comes out is a new sequence of characters that look nothing like the original. We use werkzeugs functions for hashing


Email verification
===========

Flask-Mail uses SMTP for email sending/delivery. There's different configuration keys you can use including `localhost` listed here: [list]

Sending mail from the shell: import Message, then compose message, a body, and html body then you can send within app_context()

let's make a new file email.py in the top app directory to define a function to send the email

Let's have the app email us when a new user signs up. (explain why current_app goes in `home()` view func) (also warning could get annoying so don't pick a good email)

actually no that won't go in the home form, but the register form me things. I think we're gonna remove the form on home() because it's not useful anymore

To enable SMTP connections in GMail, you'll wanna go to your Google Security Settings. as of this writing it's at: https://myaccount.google.com/security . Then, turn ON "less secure app access." Don't worry too much about the "less secure" part as Google just wants you to use OAuth2 or something. (This is fine though, right? Probably want to offer some alternatives to python's `smtplib`)

You'll also need to enable two factor authentication, then create an app password. Kinda confusing but once you get that, you'll be all set to send emails from your SECONDARY account

send_email() in email.py, along with importing `mail` from app and current_app.

Verification
-------------

Some applications like to verify that their users have valid information. The most common requirements apps ask of users is to verify their email. We'll have our app do the same so we can show you how it's done. For each new user, we'll mark the account as unconfirmed until a link in the email is clicked.

A confirmation link might be as simple as www.website.com/auth/confirm/id where id is the users id in the database. Once the link is clicked in email, the view function that handles that URL will know what the userid is and can then mark that user as confirmed. But that's not a secure implementation because anyone can just take the link in the email and change the id to anything. That's not secure, but we can make it secure very easily. Confirmation tokens can help us do that, and we'll use itsdangerous package.

A confirmation token will replace the id with something a lot more cryptic and undecypherable to a person but that only our app can generate and understand. We [didn't yet] discuss earlier that user sessions are actually protected by signed cookies. These cookies contain a signature generated by itsdangerous.

Let's demonstrate the package's ability to generate one of these

```
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer(app.config['SECRET_KEY'], expires_in=3600)
>>> token = s.dumps({ 'icecream': 'wood' })
>>> token
b'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4MzcwOTc4NiwiZXhwIjoxNTgzNzEzMzg2fQ.eyJpY2VjcmVhbSI6Indvb2QifQ.ffG5SQcwTXFON0RA0VUk_HgiS2VCmyf0niH2VHdGjbra7p83hVtr0fmTCpmhLbqI1q7Vtq3KGXiqZnci28jE8Q'
>>> data = s.loads(token)
>>> data
{'icecream': 'wood'}
```

`dumps` generates a crypto signature for the data given. Data is serialized and the signature as a neat little token string. `expires_in` is in seconds

`loads()` method takes token, outputs original data if the exp time and signature are both valid

Let's add a confirmed column to our User model. `generate_confirmation_token()` takes an expiration in seconds and returns the generated token. `confirm()` verifies the token, if valid it will set the `confirmed` attribute to True

SQLAlchemy OperationalError from config not creating testing database (not filled in) (MAYBE NOT). Adding Environ gets to config for database names

learned that conftest doesn't work right inside classes

We use `_external` in the url_for function to indicate that we want fully qualified url, meaning the https:// or http://, hostname and port

when we make before_app_request: if the user's logged in and is not in the auth blueprint, the app will catch this in the if statement we made, then will show the "unconfirmed" page. They have to have an unconfirmed account ofc

We can send email asynchronously so we don't have to wait for the server to send the email. Basically what happens is we start a new thread to process sending the email so our app can focus on doing web things, like responding to the client. Cool huh?

    Miguels async email example didn't work. THIS saved my butt. We get the app object itself https://www.reddit.com/r/flask/comments/5jrrsu/af_appapp_context_in_thread_throws_working/


User Roles
==========

intro
-----

Sometimes an app with users might have only one "role" for every user (use the site the same exact way! Kinda boring right?). Some apps might have just two roles, perhaps a regular ol' user who can do a select few things in a webapp, and an administrator who can manage content and resources created by users or the admins themselves (`is_admin` in user model). But often there are *roles* with *permissions* that are in between regular user and admin such as moderators, who might have powers similar to admin but more limited. The virtual sky is the limit, as long as it can be coded.

~~Even some other times, permissions depend on *what page* a user visits. That will be true in our web app! And we'll see how to handle that [if that's even worth going into detail here]~~

Not sure where this goes
-----
(Me going on a tangent)

Now as we continue to build our app out, we may need to migrate occasionally

```bash
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Target database is not up to date.
```

Oh my. Probably because I changed the name of my models, or as it says my database not "up to date." If this happens to you, you may have to delete your migrations folder and try again with `flask db init`. I also deleted my database or dropped all tables or something, so obviously we'd only migrate if we're *running* the website in production from epoch 0

I will keep my old on in source control but will do `db init`

Also, I forgot `lazy='dynamic'` and I don't know how to explain. And I think in general I'll have to keep the same users as before like john because it'll get confusing which ones we have or not

Now that we've updated User Profile, migration

**homework idea add field to reconfirm a different email but where you have to put password in first**


Rough Time Breakdown
=====================

Video production takes longer than expected


- Plaza development - 1 week
- 17 sections - 4 hours for descriptions
- 3.5 labs per section (30 m) - 30 hours
- 17 * 3 quizzes (30 m) - 25 hours
- 2.5 videos, 2 minutes per section (45 m) - 63 hours
- 1 week + 123 hours
Roughly 20 hours a week