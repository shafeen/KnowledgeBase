'''_

Let's learn a useful way to use function objects: Python's KEY
FUNCTIONS.  Whenever you use max(), min() or sorted(), it will compare
elements according to the type. For a list of ints and floats,
elements are just compared by their numeric value:

>>> nums = [3, 10, 9, 21]
>>> sorted(nums)
[3, 9, 10, 21]

For a list of strings, the elements are compared lexicographically -
like alphabetically, in other words, but generalized to full ASCII and
Unicode:

>>> nums_as_strings = ["3", "10", "9", "21"]
>>> sorted(nums_as_strings)
['10', '21', '3', '9']

When sorting strings, "10" comes before "21", for the same reason "ba"
comes before "cb". That's the opposite of numerical order; what's if
that numerical order is what you actually want?  You could create a
new list of converted values, but that's wasteful and gives you
elements of a different type, which you might just have to convert
back. Instead, you can pass in a parameter for the *key function*:

>>> sorted(nums_as_strings, key=int)
['3', '9', '10', '21']

A *key function* is a function of one argument - which will be fed an
element in the list - and returns a value you want sorted() to use for
comparison. In effect, sorted() is letting you modify its algorithm,
by passing in this key function.

Notice what you're passing in for "key=". You write "key=int", not
"key=int()". You're passing in the name of the function object, NOT
calling it in any way. sorted() is what's calling it.

(And of course, int is actually a type - this works with any
callable, not just formal functions.)

It turns out max() and min() support this too:

>>> max(nums_as_strings, key=int)
'21'
>>> min(nums_as_strings, key=int)
'3'

Some other examples, using abs() (for absolute value):
>>> integers = [-10, -3, 4, 1]
>>> sorted(integers)
[-10, -3, 1, 4]
>>> sorted(integers, key=abs)
[1, -3, 4, -10]
>>> min(integers, key=abs)
1
>>> max(integers, key=abs)
-10

Note that you *must* pass in the "key=" - it doesn't work as a
non-keyword argument:

>>> sorted(integers, abs)
Traceback (most recent call last):
...
TypeError: abs() takes exactly one argument (2 given)

If there's no built-in function, you might need to write your own to
pass in:

>>> nobles = [{'symbol': 'Kr', 'name': 'Kr', 'atomic_number': 36},
...           {'symbol': 'He', 'name': 'He', 'atomic_number': 2},
...           {'symbol': 'Ne', 'name': 'Ne', 'atomic_number': 10},
...           {'symbol': 'Xe', 'name': 'Xe', 'atomic_number': 54},
...           {'symbol': 'Ar', 'name': 'Ar', 'atomic_number': 18}]

>>> def get_atomic_number(atom):
...     return atom["atomic_number"]

>>> max(nobles, key=get_atomic_number)['symbol']
'Xe'
>>> min(nobles, key=get_atomic_number)['symbol']
'He'


Okay, let's practice working with key functions. Write the following
functions, use either min(), max() or sorted()  for each -
whichever fits best - along with an appropriate key function.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions 

Modify your code to use lambda expressions instead of separately defined key functions.

'''

# Write your code here:

# most_spaces using a custom key function
# You can define num_spaces inside of most_spaces, or outside (globally) - either is fine.
def most_spaces(items):
    def num_spaces(s):
        return s.count(" ")
    return max(items, key=num_spaces)

# most_spaces using a lambda (for extra credit)
def most_spaces(items):
    return max(items, key=lambda s: s.count(" "))

# these count_* functions are helpers for fewest_vowels and most_consonants
def count_chars(s, subset):
    count = 0
    for c in s.lower():
        if c in subset:
            count += 1
    return count
def count_vowels(s):
    return count_chars(s, 'aeiou')
def count_consonants(s):
    return count_chars(s, 'bcdfghjklmnpqrstvwxyz')

def fewest_vowels(items):
    return min(items, key=count_vowels)

def most_consonants(items):
    return max(items, key=count_consonants)

# sorted_by_word_count using a custom key function
def sorted_by_word_count(items):
    def num_words(s):
        return len(s.split())
    return sorted(items, key=num_words)

# sorted_by_word_count using lambda (for exatra credit)
def sorted_by_word_count(items):
    return sorted(items, key=lambda s: len(s.split()))


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
