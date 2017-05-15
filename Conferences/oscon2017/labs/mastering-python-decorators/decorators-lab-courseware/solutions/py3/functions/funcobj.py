'''_

We'll use this helper function:

>>> def reverse_string(s):
...     return s[::-1]

>>> reverse_string("Hello, world")
'dlrow ,olleH'


mk_adder is a function that takes a number argument, and returns a
function object.  That function object takes one argument itself, and
returns the sum.

>>> add2 = mk_adder(2)
>>> type(add2)
<class 'function'>

>>> add2(7)
9

>>> add7 = mk_adder(7)
>>> add7(3)
10

You can use it directly, without storing in a variable:

>>> mk_adder(4)(2)
6

apply1 calls a function for you. It takes a two arguments. The first
is a function object; apply1 will call that function, passing it the
second argument.  (In other words: the second argument to apply1 is
the first argument to the function apply1 calls).

>>> apply1(add2, 4)
6

apply1 actually works with any callable - meaning, anything that can
be called like a function. int is a type, but you can call int("42")
like a function, since Python has no "new" keyword.

>>> apply1(int, "42")
42

>>> apply1(reverse_string, "Hello, world")
'dlrow ,olleH'

>>> verbose_reverse_string = announce1(reverse_string)
>>> type(verbose_reverse_string)
<class 'function'>

>>> verbose_reverse_string("Python")
Calling with arg: Python
'nohtyP'

>>> verbose_reverse_string("Monty")
Calling with arg: Monty
'ytnoM'

Remember, you can convert any object to a string with str().

>>> verbose_sum = announce1(sum)
>>> verbose_sum([5, 10, 20])
Calling with arg: [5, 10, 20]
35

>>> verbose_sum([-2, 1, 1])
Calling with arg: [-2, 1, 1]
0


Here's some house data:

>>> bobs_house = {
...     "address": "1423 99th Ave",
...     "square_feet": 1705,
...     "price_usd": 340210,
... }
>>>
>>> johns_house = {
...     "address": "24257 Pueblo Dr",
...     "square_feet": 2305,
...     "price_usd": 170210,
... }

Let's make helper to look up different fields:

>>> get_price = keylookup("price_usd")
>>> type(get_price)
<class 'function'>
>>> get_price(bobs_house)
340210
>>> get_price(johns_house)
170210

>>> get_address = keylookup("address")
>>> get_address(bobs_house)
'1423 99th Ave'
>>> get_address(johns_house)
'24257 Pueblo Dr'

Notice we don't have to store keylookup()'s return value in a
variable.  It works just fine directly, without giving it a "name":

>>> keylookup("square_feet")(bobs_house)
1705
>>> keylookup("square_feet")(johns_house)
2305


Finally, let's write a function called apply(), which  generalizes apply1:

>>> def f(x, y):
...    return x * y

>>> def g(a, b, c):
...     return (a + b)/c

>>> apply(f, 2, 3)
6

>>> apply(g, 4, 8, 6)
2.0

And let's not forget about keyword arguments:

>>> apply(f, y=4, x=9)
36

>>> apply(g, 4, 8, c=4)
3.0

def apply(func, *args, **kwargs):
    return func(*args, **kwargs)

'''

# Write your code here:

def mk_adder(increment):
    def add(arg):
        return arg + increment
    return add

def apply1(func, arg):
    return func(arg)
    
def announce1(func):
    def newfunc(arg):
        print("Calling with arg: " + str(arg))
        return func(arg)
    return newfunc

def keylookup(key):
    def lookup(dictionary):
        return dictionary[key]
    return lookup

def apply(func, *args, **kwargs):
    return func(*args, **kwargs)

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
