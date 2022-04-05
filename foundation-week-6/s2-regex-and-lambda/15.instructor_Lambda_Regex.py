"""
LAMBDA FUNCTIONS

Examples & Practice

"""


#  Another Lambda Example


def triple1(num):
    return num * 3


triple2 = lambda num: num * 3

###############################################

#  Lambda Example with MAP
# """
# Compare using MAP function without a lambda expression and then with it.
#
# Remember, the map function expects two arguments: a function and a list.
# It takes the transformation function and applies it
# to ***every element in the list***,
# returning the list of modified elements as a map object.
# This is why we use list() again to convert
# the resulting map object back into a list again.
# """
# # WITHOUT LAMBDA

my_list = [2, 4, 6, 8]
print(my_list)


def add_five(number):
    return number + 5


new_list_A = list(map(add_five, my_list))
print(new_list_A)

# WITH LAMBDA

new_list_B = list(map(lambda x: x + 5, my_list))
print(new_list_B)

# In this case we did not need to define a separate function like 'add_five',
# we just used lambda in a single expression.

###############################################

#  Lambda Example with FILTER
"""
Compare using FILTER function without a lambda expression and then with it. 

Remember, with the filter function, the process is very similar. 
Filter takes a function and applies it to every element in a list.
It creates a new list with 
***only the elements that made the function to return True***.
"""
# WITHOUT LAMBDA

numbers = [1, 4, 5, 10, 20, 30]
print(numbers)


def greater_than_five(number):
    if number > 5:
        return True
    else:
        return False


new_numbers_A = list(filter(greater_than_five, numbers))
print(new_numbers_A)

# WITH LAMBDA

new_numbers_B = list(filter(lambda x: x > 5, numbers))
print(new_numbers_B)

# In this case we did not need to define a separate filter function
# like 'greater_than_five', we just used lambda in a single expression.

###############################################

#  Lambda Example with REDUCE
"""
Compare using REDUCE function without a lambda expression and then with it. 

Reduce is another brilliant Python function. 
It applies a ***rolling calculation to all items in a list***. 
You could use this to tally up a sum total, or multiply all numbers together.
"""

# WITHOUT LAMBDA

from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]
print(numbers)


def sum_up(a, b):
    return a + b


result_A = reduce(sum_up, numbers)
print(result_A)

# WITH LAMBDA

result_B = reduce(lambda a, b: a + b, numbers)
print(result_B)

###############################################

"""
Simply a useful example to know. 

Task:
Search through a list of dictionaries to find the only one 
dictionary that you need by value. 

Let's say we need to find some info on a specific CFG student. 
Out data structure is as follows: every student is represented as a dictionary
and all dictionaries are held in a list. 
We need to find one student by her name. 
"""

students = [
    {'name': "Jane", 'age': 43, 'specialisation': 'Software'},
    {'name': "Priya", 'age': 24, 'specialisation': 'Data'},
    {'name': "Diana", 'age': 18, 'specialisation': 'Data'}
]

# get info for a student called 'Priya' ( a search criteria can be anything:
# an ID, a name, name and surname together and many more)

result = list(filter(lambda student: student['name'] == 'Priya', students))

print(result)

################################################
"""
IMPORTANT NOTES:

These examples have shown just how easy lambda functions are.
Still, there are a few uses where lambda functions should not be used!

 - If you're doing anything more than a basic task, or want to call 
   other methods, use a normal function. 
   
 - Lambdas are great for one off, anonymous functions, 
   but they must only have one single expression. 
   
 - If your lambda starts growing in size and looking like a common expression, 
   then it is probably time to refactor in to a stand alone normal function.

"""

# NB go back to the PPT to start on REGEX.
# Come back to practical exercises later (as indicated in the PPT)

#################################################

"""
REGEX exercises and examples

"""

import re

# EXAMPLE 1 --- re.match

"""
matches the regex pattern starting from the beginning of the sentence 
and returns the matched substring. 
If something is found, then it returns a re.Match object; 
if not, it returns None
"""

my_str = "Nano Degree is fun"
regex = "Nano\s\w+\s"
'''
In the regex above: match 'Nano' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''


matched = re.match(regex, my_str)
print(matched)

# To get the position of the matched substring and the text,
# we can use .span() and .group() , respectively.

print(matched.span())
print(matched.group())

#####################################################

# EXAMPLE 2 --- re.search

"""
matches the regex pattern within the entire input sentence and returns 
the first occurrence of the matched substring. 
The difference between re.search and re.match is 
that the matched substring of re.search does not have to start 
from the beginning of the input string.
"""

my_str = "Software and Data Science 777 are fun"
regex = "Sci[\w\s]+\d+"
'''
In the regex above: match 'Sci' followed by a series of alphanumeric or space
char, followed by some digits
'''


matched = re.search(regex, my_str)
print(matched)

# To get the position of the matched substring and the text,
# we can use .span() and .group() , respectively.

print(matched.span())
print(matched.group())

#####################################################

# EXAMPLE 3 --- re.finditer

"""
matches all of the regex patterns in the input string and 
returns an iterator containing all the re.Match 
objects of the matched substrings.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
In the regex above: match 'data' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''

for matched in re.finditer(regex, my_str):
    print(matched)


#####################################################

# EXAMPLE 4 --- re.findall

"""
matches all of the regex patterns in the input string and returns a 
list containing all the matched substrings. The only difference between 
re.findall and re.finditer is that re.findall returns a list 
instead of an iterator and contains matched substrings 
instead of re.Match objects.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
In the regex above: match 'data' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''

for matched in re.findall(regex, my_str):
    print(matched)


#####################################################

# EXAMPLE 5 --- re.sub

"""
matches all of the regex patterns in the input string 
and substitutes them with the new_text provided.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
Substitute 'data science' and 'data analysis' with 'SQL queries'
'''
result = re.sub(regex, 'SQL queries ', my_str)
print(result)

#####################################################

# EXAMPLE 6 --- GROUPING

"""
Sometimes we might want to match a regex pattern but only capture a 
portion (or group) of it. Regex provides a simple way of doing this 
by using the parenthesis (). We can define the group we want to capture 
by surrounding it with () within the regex pattern.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s(\w+)\s"
'''
Match the word after 'data'
'''
for matched in re.findall(regex, my_str):
    print(matched)

#####################################################

# EXAMPLE 7 --- COMPILING

"""
SO FAR, we have mainly used module-level functions provided by re directly. 
Another way to perform regex pattern matching is to *compile* the pattern first
and then call the functions on the compiled object. 

In general, we can use the compiled approach if we are going to use 
the pattern MULTIPLE times; otherwise, it’s simpler to use the module-level
(non-compiled) functions.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s(\w+)\s"
pattern = re.compile(regex)
'''
Match the word after 'data'
'''
print("COMPILED EXAMPLE")
for matched in pattern.findall(my_str):
    print(matched)

#####################################################

# EXAMPLE 8 --- PRACTICAL EXAMPLE

"""
We have a list of mock trade ids that need to be processed, so that we
extract the date string from each id
"""

trade_ids = [
    "ghjd-gfjv-20220615-12345",
    "vbfd-dusi-20181103-11111",
    "pomm-xxsa-20041222-22222",
]
my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

# whole pattern and a group within the pattern
regex = "\w{4}-\w{4}-(\d{8})-\d+"
pattern = re.compile(regex)
'''
Match and extract a date in a trade id  
'''
# matches the whole pattern, but we want to return only the group(),
# hence group(1)
result = [pattern.search(_id).group(1) for _id in trade_ids]
print(result)
