# EXAMPLEs FOR VIDEO GUIDE 2

# # hash for integer unchanged
# print('Hash for 100 is:', hash(100))
# # hash for decimal
# print('Hash for 100.55 is:', hash(100.55))
# # hash for string
# print('Hash for CFG is:', hash('CFG'))
# # hash for tuple
# word = ('g', 'i', 'r', 'l', 's')
# print('The hash is:', hash(word))


# class CFGStudent:
#
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name
#
#     def __hash__(self):
#         print('The hash is:')
#         return hash((self.age, self.name))
#
#
# person = CFGStudent(30, 'Nina')
# print(hash(person))

###################################################################

# GENERAL DICTIONARY EXERCISES

"""
Python program to find the sum of all items in a dictionary.

Input : {'a': 100, 'b':200, 'c':300}
Output : 600
"""

# # option 1
# # def return_sum(my_dict):
# #     sum = 0
# #     for i in my_dict:
# #         sum = sum + my_dict[i]
# #     return sum
# #
# #
# # # option 2
# # def return_sum(my_dict):
# #     sum = 0
# #     for i in my_dict.values():
# #         sum = sum + i
# #     return sum
# #
# #
# # dict = {'a': 100, 'b': 200, 'c': 300}
# # print("Sum :", return_sum(dict))

#####################################################################

"""
Ways to sort list of dictionaries by values in Python.

1. We are going to use itemgettor operator
"""

# from operator import itemgetter
#
# my_list = [
#     {"name": "Zainab", "age": 20},
#     {"name": "Natasha", "age": 20},
#     {"name": "Sahitya", "age": 19}]
#
# print("The list printed sorting by age: ")
# print(sorted(my_list, key=itemgetter('age')))
#
# print("\r")
#
# # using sorted and itemgetter to print list sorted by both age and name
#
# print("The list printed sorting by age and name: ")
# print(sorted(my_list, key=itemgetter('age', 'name')))
#
# print("\r")
#
# # using sorted and itemgetter to print list sorted by age in descending order
# print("The list printed sorting by age in descending order: ")
# print(sorted(my_list, key=itemgetter('age'), reverse=True))


"""
Python – Replace words from Dictionary

Input : 
test_str = ‘CodeFirstGirls best for girls’, repl_dict = {“girls” : “all keen learners”}

Output : 
CodeFirstGirls best for CodeFirstGirls.

Explanation: 
“girls” word is replaced by lookup value.
"""


test_str = "CodeFirstGirls best for girls"

print("The original string is : " + str(test_str))

lookup_dict = {"best": "good and better", "girls": "all keen learners"}


temp = test_str.split()
res = []
for wrd in temp:

    res.append(lookup_dict.get(wrd, wrd))

res = ' '.join(res)

print("Replaced Strings : " + str(res))
