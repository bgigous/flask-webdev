
Redirects and Message Flashing
----------

We never want to repeat a form submission if the user refreshes, so we'll prevent that with a `redirect`

As you can see with the redirect, hitting refresh after submitting the name doesn't trigger an alert. On top of that, the way we've done it, we can actually visit a different page, then come back and see our name is still there! (Verify this is true, and false otherwise)

Putting flashed messages in the base template ensures you don't have to repeat putting your flashed messages into other templates. And we use a loop because there might be more than one message to display at a time