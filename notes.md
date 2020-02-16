Notes
=====

Hello web world:
    Try making more routes
    Try putting some html in (headers, links...)
    what if we return a number

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

comments screw things up if before jinja (the <!-- kind>)

Try some other bootstrap template blocks!

Pasting base.html template from microblog git repo

Navbar isn't showing up (nor is title inheriting) because: I was not inheriting from base.html but rather bootstrap/base.html

CSS Styling is missing for bootstrap in base template which has a navbar. ultimately because of `block head`...

error.html inherits from base.html but it won't add margin to the content... Oh, it's not a page_content which is why

The templates we made go from server to user. Great for getting information _to_ us, but obviously we need to tell the server stuff, right? GET is server -> user, POST is user -> server. These things are called requests. POST requests give server access to user information, like login info and personal details and favorite flavor of ice cream.

Making form components with HTML is straightforward, but then there's validating. And then how the heck do we make sure the user input is valid? For example, "wood" isn't exactly a flavor of ice cream... and hang on, how do we connect all this to python???

For that we have flask-wtf! It makes making forms easy! (Don't let the name fool you)

But there's one quick thing we need to do first. If I want complete secrecy as to my own fav flavor of ice cream, to only confide it to the server, the framework has to make sure the data sent is *encrypted*. introducing the secret key (we'll add in configuration)
(use external links to encourage students to dive in further)

(be able to explain what the FlaskForm/Form class definitions mean/ the breakdown)

Alright, now let's define the form "look" in a template
Remember the long spiel about security? There's a little more to do: hidden_tag() is needed for Flask-WTF to implement CSRF protection. Basically, you'll want to include it because it's important! Blah blah blah

You can even define ids in your form so that you can define CSS styles for them, within the template

To make our life easier, we're gonna use Flask-Bootstraps predefined CSS styles. That way, we don't have to cringe at a form that looks like it came from the Internet of the 90's, we can have a cool modern look right outta the box (`import "bootstrap/wtf.html" as wtf`, `wtf.quick_form(form)`, `form` is a variable, and we don't have to define the form fields individually)

Wait a sec, what's with this "Method not allowed" message? Of course it's allowed! I just put the form in there! Oh, wait. It's talking about the [what GET/POST things are called] methods! Let's add those to our route decorator. view functions are only GET by default. More about POST... And upon POST, what happens with the `validate_on_submit` and validation...

We never want to repeat a form submission if the user refreshes, so we'll prevent that with a `redirect`

As you can see with the redirect, hitting refresh after submitting the name doesn't trigger an alert. On top of that, the way we've done it, we can actually visit a different page, then come back and see our name is still there! (Verify this is true, and false otherwise)

Putting flashed messages in the base template ensures you don't have to repeat putting your flashed messages into other templates. And we use a loop because there might be more than one message to display at a time


What's a model? A model is basically [I need a way to describe this...]. The models are the objects that your webapp interacts with to get the data it needs and update data as needed. If say a user logs in , the webapp will need to load the information on the user so that the user sees nothing but what they expeect for the app.

If they register a new account, that means you'll add that information to the database. There are lots of other info that needs to be tracked with that user. The great thing about relational databases is that *relationships* can be formed between the data. Each user will have a *role* in the application, and that relationship between role and user can be defined with [].

There are many relationship options you can use, and each has a different behavior/use case. (Try some in a lab)

create_all() can't be called again if the models need to be changed because the tables already have the old columns. To force a change in columns, you can call drop_all() and then create them all again with create_all(), but that removes any data you have!

But don't worry, there's a way to update your models without destroying all the information that exists! We'll discover this magical solution together later, but for now let's talk about how to get data in the tables in the first place.

To do that we're going to use the convenient `flask shell` command to interact with our database one command at a time (what?).

(Do you need a backref to a foreign key in the other table)

for inserting users into our database with sample usernames, []. "Note that the role attribute can be used, even though it is not a real data‐
base column but a high-level representation of the one-to-many relationship."

The id attribute of the new objects haven't been set yet (paraphrased), and it's not explicit or doesn't have  to be because ids are set automatically. Check it out: `>>> print(manager_role.id)`

However, we haven't inserted these values into the database yet. We've only created the objects. That's why they haven't been assigned. Lets go ahead and put them in the table.

Before we do that, understand that values must be inserted in the [context or something] of a database session. This way you can line up a bunch of commands to execute, and when you're ready to actually insert them, you'll `commit` those commands. let's get the values ready

```
[add commands
```

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



Pretty much everyone goes shopping. Except maybe not your Uncle Steve, who fends for himself out in the woods and hunts his own food.
Anyway that's why all users who sign up are "shoppers"




































































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