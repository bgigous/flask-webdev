Forgot
======
Epiphany: istances of database models get ids if they are new AFTER they get committed

`moment.include_moment()` in base.html until user profile

LinkedIn uses Flask

Homework Ideas
======
`moment.include_moment()` in base.html until user profile
LinkedIn uses Flask
**homework idea add field to reconfirm a different email but where you have to put password in first**

Problems and Maybe Solutions
===================

I added a function with no route, that's probably something a student would do
and I tried rendering template without importing

in your jinja templates, you can try some filters! safe capitalize ...
should I introduce jinja macros?

You can use template inheritance ("extends") to define blocks that can be overridden by derived templates
or you can store common html in a separate file and "include" them to avoid repetition

I used {{variable}} in a {% %} block and it was syntactically wrong

Use `{{super()}}` in template `block` to inherit the base template's `block`

Miguel has:

```html
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

comments screw things up if before jinja (the `<!--` kind>)

the reason we don't have bootstrap is BECAUSE I LITERAlly HADA no inteERNET
Try some other bootstrap template blocks!

Pasting base.html template from microblog git repo

Navbar isn't showing up (nor is title inheriting) because: I was not inheriting from base.html but rather bootstrap/base.html

CSS Styling is missing for bootstrap in base template which has a navbar. ultimately because of `block head`...

Generated all slugs correctly and it loaded everything back again! yay