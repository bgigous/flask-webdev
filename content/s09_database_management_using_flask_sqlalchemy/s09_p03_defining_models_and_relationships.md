Defining the Models And Their Relationships
-------------------------------

There are many relationship options you can use, and each has a different behavior/use case. (Try some in a lab)

create_all() can't be called again if the models need to be changed because the tables already have the old columns. To force a change in columns, you can call drop_all() and then create them all again with create_all(), but that removes any data you have!

But don't worry, there's a way to update your models without destroying all the information that exists! You'll discover this magical solution together later, but for now let's talk about how to get data in the tables in the first place.