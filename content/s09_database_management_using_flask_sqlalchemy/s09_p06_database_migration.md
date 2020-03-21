
Database Migration with Flask-Migrate
-------------------------------------

Alright, so our problem earlier... So of course we need to add more columns to our database models so that we can build our app. But the problem is, so far, to do that we have to drop all tables and our data goes away. To fix that, we'll support "migration" which is a fancy way of saying, "Make scripts that can make the necessary changes to the database, and that can also _move_ the data to we already have as needed." Or something. It keeps track of how the database schema changes.

(Does sound kinda cool right? See the data in its natural habitat, doing its migrations as usual. I was inspired by that one NG guy's voice)

`pip install flask-migrate`

add Migrate and init it in our python code, like so []. After Migrate installs, it adds a `flask db init` command we can run in the CLI. Run it now, k?

You'll see that it creates a migrations directory, that's where all the migration scripts are.