"""
Author: SUNNY BHAVEEN CHANDRA

For more information - 
- [1] Python notes-
    https://c17hawke.github.io/Python/

- [2] Python YouTube Playlist- 
    https://youtube.com/playlist?list=PLrdaCCBhU_hnxIzB7EJlY-pfYOMGRycAK

"""

# Variables in Python

x = 5
print("Twice of a num", x * 2)


lecture = "Introduction to python"
print("This is a lecture of:", lecture)

# f-string way to write above statement - Most frequently used
lecture = "Introduction to python"
print(f"This is a lecture of: {lecture}") # do not forget f in the beginning

name = "Sunny"
print(f"My name is: {name}")

age = 52
print(f"My age is: {age}")

print(f"My name is {name} and My age is {age} years")

# write a table of a no. upto 10
x = 5
print(f"showing table of: {x}")
print(f"{x} x 1 = {x * 1}")
print(f"{x} x 2 = {x * 2}")
print(f"{x} x 3 = {x * 3}")
print(f"{x} x 4 = {x * 4}")
print(f"{x} x 5 = {x * 5}")
print(f"{x} x 6 = {x * 6}")
print(f"{x} x 7 = {x * 7}")
print(f"{x} x 8 = {x * 8}")
print(f"{x} x 9 = {x * 9}")
print(f"{x} x 10 = {x * 10}")

"""
RULE
1. Variable names can contain letters, 
numbers, and underscores only (A-Z, a-z, 0-9, and _ ), 
but cannot start with a number.
"""
# Correct variable names as per the above rule
my_variable = 10
my_variable_1 = 20
MyVariable_1 = 20
_variable = 200

# # against the rule above
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
same as Python keywords or inbuilt functions.

>   NOTE: Think of keywords as a 
vocabulary of Python language.
"""

# against the above rule
print = 12
print(print)

# to print the keywords present in python
import keyword
print(keyword.kwlist)

# to print the builtins present in python
import builtins
print(dir(builtins))


"""
CONVENTIONS
"""
# following is an example of declaring a hidden variable
_variable = 200

# Generally names of variables should start with small letters
variable = 200
x_val = 100

# Name of constants or the values that you do not wish to change in the program
# are constants
PI = 3.14
radius = 3
area_of_circle = PI * radius * radius
area_of_circle = PI * radius ** 2
print(f"Area of circle with radius: {radius} is {area_of_circle} unit-square")

"""
FEATURES
1. There is no need to declare a 
variable before assigning a value to it.
"""
# other languages
# int x = 2


x = 2
y = "sample text"


# advance - TYPE hinting
x: int = 2
y: str = "example text"

"""
2. You can assign values to multiple 
variables in one line.
"""
# x = 235
# y = 135
# z = 12
x, y, z = 235, 135, "text" # allowed 
print(x,y,z)


# More real-world examples -

length = 10
width = 20

area_of_rectangle = length * width
perimeter = 2 * (length + width)

print(f"for rectangle with length: {length} and width: {width}")
print(f"Area of rectangle: {area_of_rectangle} unit-square")
print(f"Perimeter of rectangle: {perimeter} units")

cost_of_shirt = 600
units_to_purchase = 3

amount_payable = cost_of_shirt * units_to_purchase
print(f"Cost of 1 shirt: {cost_of_shirt}")
print(f"Units to purchase: {units_to_purchase}")
print(f"Amount payable (in INR): {amount_payable}")

