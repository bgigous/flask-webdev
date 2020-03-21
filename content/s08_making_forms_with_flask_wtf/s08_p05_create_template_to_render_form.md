Templates
---------

Alright, now let's define the form "look" in a template
Remember the long spiel about security? There's a little more to do: hidden_tag() is needed for Flask-WTF to implement CSRF protection. Basically, you'll want to include it because it's important! Blah blah blah

You can even define ids in your form so that you can define CSS styles for them, within the template

To make our life easier, we're gonna use Flask-Bootstraps predefined CSS styles. That way, we don't have to cringe at a form that looks like it came from the Internet of the 90's, we can have a cool modern look right outta the box (`import "bootstrap/wtf.html" as wtf`, `wtf.quick_form(form)`, `form` is a variable, and we don't have to define the form fields individually)