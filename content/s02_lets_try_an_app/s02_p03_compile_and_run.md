[//]: # (Steps a student would take to build a Flask app in repl.it)

Now, let's get to building your first Flask app. We'll be using an online coding tool called Repl.it, where you can write and run your own code from within the browser. If you've never used it before, you type your code in one window, click the run button, then watch it work! You can also pop out your pre-made website address; that address is where you'll be able to see your own Flask app.

Type the following into Repl.It, then try running it and see if you get a "hello" back! Or you can go <a href="https://repl.it/@gigabot/nanoblog" target="_blank">here</a> and try to run it.

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello Web World!"

app.run(host='0.0.0.0', port=8080)
```

[Repl.it coder thing]

Did it work? If so, then _HOLY FLASK_ you just make your first Flask website! If you haven't already, you could even try making the page say something else. ;)

But I'm sure you're anxious to get to the *real stuff*. No problem, but we'll have to do just a bit of setup first, but then after that, you'll be all set to start the real training, so let's move on!