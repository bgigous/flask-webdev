Forms
=====

The templates you made go from server to user. Great for getting information _to_ us, but obviously you need to tell the server stuff, right? GET is server -> user, POST is user -> server. These things are called requests. POST requests give server access to user information, like login info and personal details and favorite flavor of ice cream.

Making form components with HTML is straightforward, but then there's validating. And then how the heck do you make sure the user input is valid? For example, "wood" isn't exactly a flavor of ice cream... and hang on, how do you connect all this to python???

For that you have flask-wtf! It makes making forms easy! (Don't let the name fool you)
