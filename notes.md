Notes
=====

Hello web world:
    Try making more routes
    Try putting some html in (headers, links...)
    what if we return a number

I added a function with no route, that's probably something a student would do
and I tried rendering template without importing


in your jinja templates, you can try some filters! safe capitalize ...
should I introduce jinja macros?

You can use template inheritance ("extends") to define blocks that can be overridden by derived templates
or you can store common html in a separate file and "include" them to avoid repetition

I used {{variable}} in a {% %} block and it was syntactically wrong

Use `{{super()}}` in template `block` to inherit the base template's `block`

Miguel has:
```
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

comments screw things up if before jinja (the <!-- kind>)

Try some other bootstrap template blocks!

Pasting base.html template from microblog git repo

Navbar isn't showing up (nor is title inheriting) because: I was not inheriting from base.html but rather bootstrap/base.html

CSS Styling is missing for bootstrap in base template which has a navbar. ultimately because of `block head`...

error.html inherits from base.html but it won't add margin to the content... Oh, it's not a page_content which is why

The templates we made go from server to user. Great for getting information _to_ us, but obviously we need to tell the server stuff, right? GET is server -> user, POST is user -> server. These things are called requests. POST requests give server access to user information, like login info and personal details and favorite flavor of ice cream.

Making form components with HTML is straightforward, but then there's validating. And then how the heck do we make sure the user input is valid? For example, "wood" isn't exactly a flavor of ice cream... and hang on, how do we connect all this to python???

For that we have flask-wtf! It makes making forms easy! (Don't let the name fool you)

But there's one quick thing we need to do first. If I want complete secrecy as to my own fav flavor of ice cream, to only confide it to the server, the framework has to make sure the data sent is *encrypted*. introducing the secret key (we'll add in configuration)
(use external links to encourage students to dive in further)

(be able to explain what the FlaskForm/Form class definitions mean/ the breakdown)

Alright, now let's define the form "look" in a template
Remember the long spiel about security? There's a little more to do: hidden_tag() is needed for Flask-WTF to implement CSRF protection. Basically, you'll want to include it because it's important! Blah blah blah

You can even define ids in your form so that you can define CSS styles for them, within the template

To make our life easier, we're gonna use Flask-Bootstraps predefined CSS styles. That way, we don't have to cringe at a form that looks like it came from the Internet of the 90's, we can have a cool modern look right outta the box (`import "bootstrap/wtf.html" as wtf`, `wtf.quick_form(form)`, `form` is a variable, and we don't have to define the form fields individually)

Wait a sec, what's with this "Method not allowed" message? Of course it's allowed! I just put the form in there! Oh, wait. It's talking about the [what GET/POST things are called] methods! Let's add those to our route decorator. view functions are only GET by default. More about POST... And upon POST, what happens with the `validate_on_submit` and validation...

We never want to repeat a form submission if the user refreshes, so we'll prevent that with a `redirect`

As you can see with the redirect, hitting refresh after submitting the name doesn't trigger an alert. On top of that, the way we've done it, we can actually visit a different page, then come back and see our name is still there! (Verify this is true, and false otherwise)

Putting flashed messages in the base template ensures you don't have to repeat putting your flashed messages into other templates. And we use a loop because there might be more than one message to display at a time












Rough Time Breakdown
=====================

Video production takes longer than expected


- Plaza development - 1 week
- 17 sections - 4 hours for descriptions
- 3.5 labs per section (30 m) - 30 hours
- 17 * 3 quizzes (30 m) - 25 hours
- 2.5 videos, 2 minutes per section (45 m) - 63 hours
- 1 week + 123 hours
Roughly 20 hours a week