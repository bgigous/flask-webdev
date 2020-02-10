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