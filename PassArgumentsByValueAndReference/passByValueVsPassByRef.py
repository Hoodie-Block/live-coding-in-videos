"""define two functions and check the pass by value and pass by reference

    functions:

        * func_for_value: a function which takes a integer as its argument
        * func_for_list: a function which takes a list as its argument
"""

import copy

## define functions
def func_for_value(value):
    value = value * 2
    print("value inside func_for_value", value)

def func_for_list_by_copy(lst):
    lst = copy.copy(lst)
    lst.append(42)
    print("list inside func_for_list_by_copy", lst)

def func_for_list(lst):
    lst.append(42)
    print("list inside func_for_list", lst)


## define some example values

num = 10
example_list = [1, 2, 3, 4]


## use the functions for the values

print("before using func_for_value", num)
func_for_value(num)
print("after using func_for_value\n", num)

print("before using func_for_list_by_copy", example_list)
func_for_list_by_copy(example_list)
print("after using func_for_list_by_copy\n", example_list)


print("before using func_for_list", example_list)
func_for_list(example_list)
print("after using func_for_list\n", example_list)