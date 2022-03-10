### DEMO 1 ###
"""

Write a program that asks two questions using input()
then prints the values that were entered.
You can choose any questions that you want.

Example:
"""

# animal = input('Do you like dogs or cats more? ')
# pet_name = input('What would name your pet? ')
# print('You like {} and you would name your pet {}'.format(animal, pet_name))

"""
The input() always returns a string value!!! 
You can convert this string value to an integer with int():

Demonstrate this case with the following examples:
--------------------------------------------------

apples_string = '12'
total_apples = int(apples_string) + 5
print(total_apples) 

AND

purchased_apples = input('How many apples did you buy? ')
total_apples = int(purchased_apples) + 5
print(total_apples)

"""


### EXERCISE 1 ###
"""
You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.
Write a program calculate how many pizzas you need to feed you and your friends
"""
#
# friends = # Add input here
# pizzas = friends * 0.5
#
# print('You need {} pizzas for {} friends'.format(pizzas, friends))

"""
Example solution
"""
# friends = int(input('How many friends are at your house? '))
# pizzas = friends * 0.5
# print('You need {} pizzas for {} friends'.format(pizzas, friends))


### DEMO 2 ###
"""
Show simple examples on how to use datetime package
"""

# import datetime
# x = datetime.datetime.now()
# print(x)

########### formatting #############

# import datetime
# my_date = datetime.date(2020, 12, 31)
# print(my_date.strftime("%d/%b/%Y"))


### EXERCISE 2 ###
"""
Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) for £130. 
If a person pays within 14 days, then the amount will be reduced to £65.

Pseudo-code Example:

- Accept the PCN date as an input
- Calculate the deadline date, which is 14 days from the PCT issue date.
- Print the message informing the driver about the deadline date, so that they only need to pay £65.

Example solution below.
"""

# from datetime import datetime, timedelta
#
# pcn_date = input("Please enter the PCN issue date in the following format DDMMYYYY: ")
#
# date_obj = datetime.strptime(pcn_date, '%d%m%Y')
#
# # Calculating the 14 day deadline
#
# deadline = date_obj + timedelta(days=14)
#
# # Formatting the date
#
# formatted_deadline = deadline.date().strftime("%d %b %Y")
#
# print("\n If you pay PCN penalty by *{}*, the amount will be reduced to £65".format(formatted_deadline))



### EXERCISE 3 ###
"""
fetch current date and time to milliseconds and create a "timestamp" in the following format YYYYMMDD_HHMMSSMsMs

For example: if the current date and time is "30 October 2020, 10h 25 min 41 sec and 123456 milliseconds", out timestamp must be:

"20201030_22254112"

"""
# import datetime
#
# dt = datetime.datetime.now()
# print(dt) # check what we get back
#
# timestamp = "your solution is here"
#
# print("timestamp: " + timestamp)

"""
Example solution
"""

# import datetime
#
# dt = datetime.datetime.now()
# print(dt) # check what we get back
#
# timestamp = dt.strftime('%Y%m%d_%H%M%S%f')[:-4]
#
# print("timestamp: " + timestamp)


### DEMO 4 ###
"""
The pre-written range() function can be used to make a for loop repeat a certain number of times.

The range() function starts counting from 0

Examples below
"""
# for number in range(5):
#     print(number)


# for number in range(5):
#     print("executing a block of code within FOR LOOP - run No {}".format(number))
#     # relpace (number) with (number + 1)


# total = 0
# for number in range(3):  # remember --> 0, 1, 2
#
#     print("total value is: " + str(total))
#     print("this is run No " + str(number) + " inside the loop \n")
#     total = total + 10
#
# print("\nWe are outside the loop now")
# print("the final value is: " + str(total))


### EXERCISE 4 ####
"""
Write a very simple encoding program that accepts a word from a user and encodes it 
by wrapping each letter with some other letters (symbols).

Solution below - complete this together with the group
"""

# word = input("Enter the word you would like to encode: ")
#
# result = ''
#
# for char in word:
#     encoded = 'xyz{}abc'.format(char)
#     result = result + encoded
#
# print(result)


### DEMO 5 ###
"""
Due to social disctancing, only 10 people are allowed to be inside a shot at the same time. 
This program invites people in the queue to come in while we have some capacity.
"""

store_capacity = 10  # people

while store_capacity > 0:
   print('Please come in. Spaces available: ' + str(store_capacity))
   store_capacity =  store_capacity - 1

print("\nPlease wait for someone to exit the store.")


### DEMO 6 ###
"""
Example INFINITE 'while loop' that runs forever until the memory is 'blown'
"""

# store_capacity = 10
#
# while store_capacity > 0:
#     print('Please come in. Spaces available: ' + str(store_capacity))
#     # store_capacity =  store_capacity - 1 ---> imagine that we forgot to add this logic!!!
#
# print("\nPlease wait for someone to exit the store.")


### DEMO & EXERCISE 7 ###
"""
Create functions, call functions and pass arguments.
Talk class through all examples. 
"""


# def hello():
#     print('Hello, class!')
#
#
# hello()

"""
Pass Arguments
 - You can send information to a function by passing values, known as arguments.
 - Arguments are declared after the function name in parentheses.
 - When you call a function with arguments, the values of those arguments are copied to their corresponding parameters inside the function.
"""

# # Pass single argument to a function
# def hello(name):
#     print('Hello,', name)
#
# hello('Maria')
#
# hello('Kim')

#########################################

# # Pass multiple arguments
#
# def some_function(name, job):
#     print(name, 'is a', job)
#
# some_function('Fiona', 'developer')



### DEMO & EXERCISE 8 ###

"""
Positional Arguments

Positional arguments values are copied to their corresponding parameters in order.
You must to pass arguments in the order in which they are defined.
"""

# # Correct arguments order
#
# def some_function(name, job):
#     print(name, 'is a', job)
#
# some_function('Fiona', 'developer')

# ---------------------------------------

# # Wrong arguments order
#
# def some_function(name, job):
#     print(name, 'is a', job)
#
# some_function('developer', 'Fiona')

"""
Keyword Arguments

you can pass arguments using the names of their corresponding parameters.
in this case, the order of the arguments no longer matters.
you can combine positional and keyword arguments in a single call.
if you do so, specify the positional arguments before keyword arguments.
"""

# def some_function(name, job):
#     print(name, 'is a', job)
#
# some_function(job='developer', name='Fiona')
#
# some_function(name='Fiona', job='developer')


"""
Default Arguments¶
You can specify default values for arguments when defining a function.
The default value is used IF the function is called without a corresponding argument.
"""
# def some_function(name, job='developer'):
#     print(name, 'is a', job)
#
# some_function('Fiona')
#
# some_function('Fiona', 'manager')

"""
Variable Length Arguments (*args and **kwargs)¶
Variable length arguments are useful when you want to create functions that take unlimited number of arguments.
Unlimited in the sense that you do not know beforehand how many arguments can be passed to your function by the user.

*args¶
When you prefix a parameter with an asterisk *, it collects all the unmatched positional arguments into a tuple
(we will learn about tuples later, think of it as a collection of items aka a box with numbers or words etc) .


**kwargs
The ** syntax is similar, but it only works for keyword arguments (aka corresponding pairs)
"""

# def print_arguments(*args):
#     print(args)
#
# print_arguments(1,2,3,4,5,6,7)

# ----------------------------------

# def print_arguments(**kwargs):
#     print(kwargs)
#
# print_arguments(name='Fiona', age=25, job='developer')



### DEMO & EXERCISE 9 ###
"""
Examples how to return values from a function.
"""
# Using return statement

# def sum(x, y):
#     return x + y
#
# # console
# result = sum(10, 15)
# result is: {}".format(result))

# -------------------------------

# Without return statement

# def sum(x, y):
#     print(x + y)
#
# result = sum(10, 15)
# print("result is: {}".format(result))


### EXERCISE 10 ###
"""
Complete the function to return the area of a circle
"""

# def circle_area():  # add the radius argument inside the brackets
#     area = 3.14 * (radius ** 2)
#     # return area here
#
#
# circle_1 =  circle_area(10)
#
# print(circle_1)


"""
Solution
"""
# def circle_area(radius):python_2_instructor.py
#     area = 3.14 * (radius ** 2)
#     return area
#
# area = circle_area(9)
#
# print(area)
