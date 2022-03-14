### DEMO 1 ###
"""
Show students how to create a new file and then run this file.
Explain where the result is displayed (console) and then point how to re-run the file if necessary.
"""
print('Hello, World!')
print('I hope it is sunny this weekend')



### EXERCISE 1 ###

"""
Exercise 1.1: Now that you've run your first program, try the following:

- Change the message to anything you want
- Repeat the code on multiple lines to output several messages
- Find out what happens when you remove different parts of the code (e.g. brackets)
- Don't worry if something unexpected happens. Think about what you changed and why it might have caused it to happen.
"""

### DEMO & EXERCISE 2 ###
"""
Ask studetns to use Python console in PyCharm and practice the following operations together. 
Explain where required.

5 - 6
8 * 9
6 / 2
5 / 0
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4

What does each one do and what is its output?

Are there any outputs you didn't expect?

"""


### DEMO & EXERCISE 3 ###
"""
In your Python console type each of these

"Cat"
"Cat" + " videos"

"Cat" * 3
"Cat" + 3

"Cat".upper()
"Cat".lower()

"the lord of the rings".title()


What is the output for each one and why?
One of them causes an exception. Read the exception message. What do you think it means?

"""


### DEMO & EXERCISE 4 ###
"""
EXAMPLES OF STRINGS METHODS

You can copy-paste these examples into your console to save tim typing. 
Demonstrate what they do and only then complete an exercise together. 
"""

# 'Our example string object'.upper()
# 'Our example string object'.lower()
# 'Our example string object'.title()
# 'Our example string object'.count('o')
# 'our example string object'.capitalize()
# 'Our example string object'.endswith('ject')
# 'Our example string object'.endswith('mock')
# 'To make a nice cuppa you need: tea, milk, sugar and a cookie '.split(',')
# 'Our example string object'.replace('p', '#')

"""
DEMO - show in PyCharm console how to type a string, use dot and a 'tab' to bring up a list of methods for an object. 

# TASK TO COMPLETE TOGETHER: check built in methods available to use for strings

'string object' + . + click TAB
use help() function

"""

### EXERCISE 5 ###

"""
Errors and casting objects into different types

Run this:

print("Cat" + 3)

it would result in Error!
Putting a number in str() converts it to a string

print("Cat" + str(3))

"""

### DEMO 6 ###

"""
Show the example of this program to the class and walk each line step by step:
OBJECTIVE -- demonstrate that 
"""
# oranges = 12
# cost_per_orange = 0.5
#
# total_cost = oranges * cost_per_orange
#
# print(str(oranges) + " oranges")
# print("costs " + str(total_cost))

"""
The oranges variable is reused twice in the program
"""


### EXERCISE 7 ###
"""
In a new Python file called cat_food.py, create a program that calculates how many cans of cat food you need to feed 10 cats

Your will need:

A variable for the number of cats
A variable for the number of cans each cat eats in a day
A print() function to output the result
Extension: change the calculation to work out the amount needed for 7 days

Example solution below (share it with students after they have had a go)
"""
# cats = 10
# cans = 2
#
# total_cans = cats * cans
#
# output = str(cats) + " cats eat " + str(total_cans) + " cans"
# print(output)


### EXERCISE 7 ###
"""
Rewrite cat_food.py to use string formatting instead of joining strings with +.

An example of string formatting:
--------------------------------

user_name = 'Jenny_1995'
age = 23

output = '{} is {} years old'.format(user_name, age)
print(output)

"""

# Example solution

# cats = 10
# cans = 2
#
# total_cans = cats * cans
#
# output = "{} cats eat {} cans".format(cats, total_cans)
# print(output)


### DEMO 8 ###
"""
Show few examples on how to join strings together:

'-'.join(my_words)
' '.join(my_words)
''.join(my_words)

"""

### EXERCISE 8 ###
"""
Perform string formatting, so that your final sentence looks like this:
guests = ["Mary", "Pete", "Eoin"]

Result:
"We are going to cinema with my classmates: Mary, Pete, Eoin and me"

Example solution below:
(We can use string interpolation and join() function to build this sentence)
"""

# guests = ["Mary", "Pete", "Eoin"]
#
# "We are going to cinema with my classmates: {names} and me.".format(
#     names = ', '.join(guests))


### DEMO & EXERCISE 9 ###
"""
String Slicing ( do these examples with students explaining every case)

S = 'ABCDEFGHI'
print(S[2:7])

S = 'Hippopotamus'
print(S[-7:-2])

S = 'ABCDEFGHI'
print(S[2:-5])

S = 'ABCDEFGHI'
print(S[2:7:2])


Slice at Beginning & End

Omitting the start index starts the slice from the index. Meaning, S[:stop] is equivalent to S[0:stop]
Omitting the stop index extends the slice to the end of the string. Meaning, S[start:] is equivalent to S[start:len(S)]

# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3]) 


# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])


Reverse a String
You can reverse a string by omitting both start and stop indices and specifying a step as -1.

S = 'ABCDEFGHI'
print(S[::-1])

S = 'Code First Girls'
print(S[::-1])

"""

## DEMO 10 ###
"""
In built functions examples
Comment / uncomment each line in turn to see what each in-built function does
"""
# print('Code')
# type('Code')
# len('Code')
# ord('C')
# chr(ord('C'))
# help('Code')
# help(type('Code'))
