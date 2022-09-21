# Low coupling

Code bases that are tightly coupled can be hard to change and understand.
It is good to keep coupling to a minimum.

## Avoid Deep Inheritance

Having deep inheritance chains will be hard to follow and debug.

Testing for objects and classes with deep inheritance can also be tricky and messy.
There will either be a lot of mocking or it would be downright not possible.

## Seperate Creation and Use

Don't have objects creating other objects in it's creation or use.
Create all the objects seperately as they are needed and use them as needed.

## Abstractions

Can create Protocol objects that define the methods that are used.
This doesn't really change functionality, but can help highlight what methods are used,
and also ease testing as dummy objects can be easily made.

## Dependancy Injection

Similar to the previous thing, it is good to create the dependancies and then passing them in,
rather than having an object create or organise it's dependacies.

## Intermediate Data Structure

Sometimes it can be good to put things in an intermediate data structure, one that is widely and easily accepted.
This can make it easier to change things around and switch things in and out.

## Appendix

This video seemed pretty helpful <https://www.youtube.com/watch?v=qR4-PBLUZNw>
