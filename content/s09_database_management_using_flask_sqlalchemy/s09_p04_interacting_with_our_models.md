
Interacting With Our Models in the CLI
----------------------------------------------

To do that you're going to use the convenient `flask shell` command to interact with our database one command at a time (what?).

(Do you need a backref to a foreign key in the other table?)

for inserting users into our database with sample usernames, []. "Note that the role attribute can be used, even though it is not a real data‐
base column but a high-level representation of the one-to-many relationship."

The id attribute of the new objects haven't been set yet (paraphrased), and it's not explicit or doesn't have  to be because ids are set automatically. Check it out: `>>> print(manager_role.id)`

However, you haven't inserted these values into the database yet. you've only created the objects. That's why they haven't been assigned. Lets go ahead and put them in the table.

Before you do that, understand that values must be inserted in the [context or something] of a database session. This way you can line up a bunch of commands to execute, and when you're ready to actually insert them, you'll `commit` those commands. let's get the values ready

```
[add commands]
```

(don't forget about lazy)

you could also have done `db.session.add([...])`, then commit()

(Probably good to explain the difference between the flask session and db session)

Try to commit only related changes in each commit, that way you won't run into as many errors (explain this)

Modifying rows is simple, just take the same object (manager_role say), change its name attribute, then just add it again and commit. To delete any data, like the owner role (not mentioned yet), just issue a session.delete(owner_role) and then commit. Notice the pattern here? (commit)

Now how do you see what data you have in the database? you can check each table with the convenient `query` object. To just see all of the data per table, you do a `query.all()`. (The query object is associated with each `Model`! not the db itself)


you can use `filter_by()` to find users with specific roles, say just shoppers. `Shopper.query.filter_by(role=shopper_role).all()`. Notice you have to use all() again, as just using filter_by gives us a `BaseQuery` object. weird huh? (why is that??)

Ooh, here's something fun. This is what basequery means, essentially a sql command. Watch:

```python
>>> str(filter_by())
'SELECT ...'
```

So if you were curious what FS is actually doing, this is a great  way to see. Alright let's get outta here `exit()`. I know you might miss those python objects, but don't worry, their legacy still exists in the database object!

So since you're exited, you really miss those python objects. It's real easy to get 'em back by `shopper_role = Role.query.filter_by(name='Shopper').first()`. Since you know there's only one shopper role, you don't need to use all(), instead you can use first(). Check out these other query filter functions: [list em, filter, filter_by, etc]

Then once you have a query object from one of those, there are different ways of getting the data that comes out. Check out theses other "executors" (not as deadly as it might seem): [all, first, get, etc]