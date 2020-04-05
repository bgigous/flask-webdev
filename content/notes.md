Forgot
======
Epiphany: istances of database models get ids if they are new AFTER they get committed

`moment.include_moment()` in base.html until user profile

LinkedIn uses Flask

tammy87
kathleendavis@farrell.com


Homework Ideas
======
`moment.include_moment()` in base.html until user profile
LinkedIn uses Flask
**homework idea add field to reconfirm a different email but where you have to put password in first**

Problems and Maybe Solutions
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

Generated all slugs correctly and it loaded everything back again! yay

Followers and Following
============================

### return to Relationships

Relationships: Databases links between records
    one to many is most common, one record linked with list of related records
    "many" side elements have foreign key that points to linked "one" element
We currently have two of these: role -> users, user -> compositions

Many to one is simply the reverse. One to one is where an element on one side is constrained to only link to one other on the opposite side

Followers is a many to many relationship and isn't quite as straightforward. Think of a university database, where you have students and classes. One to many doesn't work: with one student, you could add a foreign key to the classes that links to the student, but that doesn't make sense because other students take the same class. It's impractical to add all of their IDs to the classes

The solution is a third *association* table. To query a many to many takes two steps.

[example of students and classes]

class registrations are defined as a `db.Table` and not a full blown model since sql manages tables internally

In SQLAlchemy, working with many to many couldn't be easier, it's just like a list:

```
s = Student
c = Class
s.classes.add(c)
db.session.add(s)
```

you can list the classes that s is registered for, and list of students for class c

```
s.classes.all()
c.students.all()
```

Say you're student s and you want to drop that hard class c. `s.classes.remove(c)`

(Could use song likes as an analogue)

In fact, in sqlalchemy, a many to many can be made with two many to ones

### self-referential

But we only have users following other users, how do we make some follow others? Simple, there's still an association table, and instead of putting one key from one model and another from another model, we use two keys from Users. One for following and one for followers.

`[]`

Since you may want to store other information about the link between two entities. Say when someone followed the other so you can list them in chrono order. You won't be able to use a `db.Table` because it can't store that info. Instead it'll have to be upgraded to a Model

When we define a model, we make the model, then when making followed and followers in User, we want no ambiguity. We explicitly specify what relationship to use with `foreign_keys`. We use `joined` for lazy backref; if we ask for who a user is following with `user.following.all()' we'll get 100 Follow instances, with each one containing back references `follower` and `following` to the respective users. If lazy wasn't set here, it would default to `select` and that would require an individual query for each one, which means 200 queries total instead of 100.

Then there's lazy on the User side, `dynamic` makes it so that relationship attributes return query objects instead of returning the items directly. This way, you can add additional filters to the query before it's executed

If one user deletes their account, we don't want the relationship between their account and the users that they follow or that follow them, so the adding `cascade` of `delete-orphan` would delete that association. [why is 'add, ' in there, too?]

Since we're working with two one-to-many relationships, there's a bit more information to keep track of than a standard "What kind of composition is this?" We have to know who wants to (un)follow who, and if a user is following someone currently or not.

### Profile Page

You'll want to display buttons for follow/unfollow, and display how many you follow or who follow you. If you view a user page, you'll also be able to see if a user follows you.

