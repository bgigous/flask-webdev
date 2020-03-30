If you've been around the web development social bubble at all, you've probably heard about Twitter's open-source web browser framework called <a href="http://getbootstrap.com" target="_blank">Bootstrap</a>. The selling point of Bootstrap is simple: tons of slick-looking user interface components that are compatible with all modern browsers on both desktop and mobile. And of course it's free and super popular, so is anyone surprised there's a Flask extension called Flask-Bootstrap that gives you nice looking pages right out of the box?

If you *were* surprised, my apologies. For your information, Bootstrap operates on the client-side basically by slapping on some CSS and JavaScript to those otherwise old-school looking HTML pages. While Flask <a href="https://www.youtube.com/watch?v=zGxwbhkDjZM" target="_blank">ain't got no time for dat</a> client-side stuff, it still needs to do its part to give Bootstrap what it needs if it wants Bootstrap's help. Mainly, that just means referencing Bootstrap's CSS and JavaScript files. A pain to do with plain ol' Flask and Jinja, but with a few quick lines of code, Flask-Bootstrap does all that heavy-lifting.

![](../images/bootstrapper-300x229.jpg)

Oh yes, this guy is *ready* to make his webpages look snazzy using Flask-Bootstrap! He can install it easily if he has been following along this whole time:

```bash
pip install flask-bootstrap
```

