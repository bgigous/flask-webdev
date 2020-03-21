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