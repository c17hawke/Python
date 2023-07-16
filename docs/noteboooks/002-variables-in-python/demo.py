# Variables in python

x = 5
print("Twice of a num", x * 2)


lecture = "Introduction to python"
print("This is a lecture of:", lecture)


# write a table of a no. upto 10
x = 5
print("showing table of", x)
print(x, "* 1 =", x * 1)
print(x, "* 2 =", x * 2)
print(x, "* 3 =", x * 3)
print(x, "* 4 =", x * 4)
print(x, "* 5 =", x * 5)
print(x, "* 6 =", x * 6)
print(x, "* 7 =", x * 7)
print(x, "* 8 =", x * 8)
print(x, "* 9 =", x * 9)
print(x, "* 10 = ", x * 10)

"""
RULE
1. Variable names can contain letters, 
numbers, and underscores only (A-z, 0-9, and _ ), 
but cannot start with a number.
"""
# Correct variable names as per above rule
my_variable = 10
my_variable_1 = 20
MyVariable_1 = 20
_variable = 200


# against the rule above
# 1_variable = 100
# my_variable_@ = 20

"""
RULE
2. Variable names are case-sensitive.
"""
my_variable = 10
my_Variable = 20
print(my_variable)
print(my_Variable)

"""
RULE
3. Variable names cannot be the 
same as Python keywords or inbuilt function.

>   NOTE: Think of keywords as a 
vocabulary of python language.
"""

# against the above rule
# print = 12
# y  = 2
# print(print)

# to print the keywords present in python
# import keyword
# print(keyword.kwlist)


"""
Feature
4. There is no need to declare a 
variable before assigning a value to it.
"""
x = 2
y = "sample text"

"""

5. You can assign values to multiple 
variables in one line.
"""
x, y, z = 2, "sample text", 100

print(x , y, z)

# More real world examples -

cost_of_shirt_per_unit = 600
units_to_purchase = 3

amount_payable = cost_of_shirt_per_unit * units_to_purchase
print("Amount payable (in INR):", amount_payable)