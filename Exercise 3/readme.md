### Project ###

We have a project where we need to define classes that have fields that we want validates before we can set their values. This might be because these objects will later be serialized into a database, and we need to ensure the data is valid before we write to the database.

## Part 1 ##

Write two data descriptors:
    - IntegerField -> only allows integral numbers, between a minimum and maximum value;
    - CharField -> only allows strings with a minimum and maximum length.

So we want to be able to use the descriptors like this:
    Class Person:
        name = CharField(1, 50)
        age = IntegerField(0, 200)

## Part 2 ##

You probably wrote in related classes to do Part 1. But you'll notice quite a bit of code duplication, with only the actual validation being different.

Refactor your code and create a BaseValidator class that will handle the common functionality. Then change your IntegerField and CharField descriptors to inherit from BaseValidator.

If you haven't coded your descriptors that way already, make sure you can also omit one or both of the minimum and maximum values where it makes sense. For example, we may want to specify a string that has no maximum limit. Or we want an integer field that has an upper bound, but no lower bound. Or maybe no bounds at all.