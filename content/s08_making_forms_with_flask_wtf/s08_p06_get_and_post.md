GET and POST
------------

Wait a sec, what's with this "Method not allowed" message? Of course it's allowed! I just put the form in there! Oh, wait. It's talking about the [what GET/POST things are called] methods! Let's add those to our route decorator. view functions are only GET by default. More about POST... And upon POST, what happens with the `validate_on_submit` and validation...