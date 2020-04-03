It's finally time to start developing your first Flask app! Let's take a look at the code you wrote previously, but now you'll put it in a file.

### Initial Setup

Once you've got VSCode running, you can go to `File -> Open Folder`, then navigate to your `flask-webdev` repository and open it up! Let's also bring up VSCode's handy little terminal, which you can open from `View -> Terminal` or by pressing ``Ctrl + ` ``, or ``Cmd + ` `` for Mac. If the terminal's working directory isn't already your `flask-webdev` directory, change it. Also, make sure your virtual environment is activated.

[//]: # (Note to self: Be sure to change the filename later!)

---

Note: This is one more friendly reminder that you'll be developing in the `flask-webdev` directory from now on, unless otherwise specified. Assume that you'll have the steps above completed every time you come back for more Flask development.

---

Note: If you have multiple virtual environments you're juggling these days, make sure you have the correct one activated. You can issue the command `deactivate` in the CLI to close the session you currently have open in order to activate a new one.

---

Then in VSCode, make a new file called `hello.py`. Now let's get those fingers moving with some code!

### The Code

In your new `hello.py` file, just type these code blocks in order. Here goes!

#### Initialization

```python
from flask import Flask

app = Flask(__name__)
```

The first couple of lines simply imports the Flask class from the flask module, and then a variable `app` is created as an instance of a Flask object. To make such a Flask instance, the `Flask` class wants the name of the main module or package of the application. Generally, `__name__` passed in as an argument is the correct value, and Flask wants it so it can find all the templates and images you make for it to render! (Which will come later ;))

#### Routing

```python
@app.route('/')
def index():
    return "Hello Web World!"
```

This one is fun, because decorators are fun. The `app.route` decorator here, with `'/'` as its argument, translates to "whenever someone visits the root URL, call this `index()` function to return a response."

Put another way, the `index()` function is a *handler* for the root URL. If the application is deployed at *www.example.com*, navigating to https://www.example.com/ with nothing else would trigger the `index()` function to be called and run on the server. Routes will be covered a little more later.

[//]: # (or now? Also covering `add_url_rule` would be good)

-----

Note: If you're not super familiar with decorators, check out <a href="https://realpython.com/primer-on-python-decorators/" target="_blank">this Real Python article</a> on the subject.

-----

Okay, that wasn't too bad, right? Make sure you save the file and pat yourself on the back! Oh, what's that? We haven't even really done anything except write a 7-or-so line file, you say? Yes yes, we'll get to that next. (Web development requires patience, grasshopper!)

<iframe width="560" height="315" src="https://www.youtube.com/embed/gbNCBVzPYak?start=57" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>