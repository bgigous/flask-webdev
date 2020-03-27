```python
from flask import Flask

app = Flask(__name__)
```

The first couple of lines simply imports the Flask class from the flask module, and then a variable `app` is created as an instance of a Flask object. To make such a Flask instance, the `Flask` class wants the name of the main module or package of the application. Generally, `__name__` passed in as an argument is the correct value, and Flask wants it so it can find all the templates and images you make for it to render! (Which will come later ;))

```python
@app.route('/')
def index():
    return "<h1>Hello Web World!</h1>"
```

This one is fun, because decorators are fun. The `app.route` decorator here, with `'/'` as its argument, translates to "whenever someone visits the root URL, call this `index()` function to return a response."
Put another way, the `index()` function is a *handler* for the root URL. If the application is deployed at *www.ragtime.com*, navigating to https://www.ragtime.com/ with nothing else would trigger the `index()` function to be called and run on the server.

The `app.route` decorator is a "shorthand" way of using the `app.add_url_rule()` method...