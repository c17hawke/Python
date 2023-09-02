"""
Author: SUNNY BHAVEEN CHANDRA

For more information - 
- [1] Python notes-
    https://c17hawke.github.io/Python/

- [2] Python YouTube Playlist- 
    https://youtube.com/playlist?list=PLrdaCCBhU_hnxIzB7EJlY-pfYOMGRycAK
"""

# User input in Python
# Data-type conversion | implicit conversions
# Data-type casting | explicit conversions

# User input in Python

name = "Sunny"
lecture = input("Name of the lecture?: ")

print(f"Hello, everyone! My name is: {name}")
print(f"Welcome to the lecture of: {lecture}")

age = input("Age: ?")
N = 5 # int
print(f"BEFORE: type of age variable: {type(age)}")
age = int(age)
print(f"AFTER: type of age variable: {type(age)}")

print(f"type of N variable: {type(N)}")

print(f"Age of the user after {N} years will be: {age + N}")


# Data-type conversion | implicit conversions

# int + float = float
x = 24 # int
y = 37.4 # float
z = x + y 
print(" x  +  y  =  z ")
print(f"{x} + {y} = {z}")
print(f"type of x: {type(x)}")
print(f"type of y: {type(y)}")
print(f"type of z: {type(z)}")

# int * float = float
x = 24
y = 37.4
z = x * y
print(" x  *  y  =  z ")
print(f"{x} * {y} = {z}")
print(f"type of x: {type(x)}")
print(f"type of y: {type(y)}")
print(f"type of z: {type(z)}")

# int / int = float
x = 24
y = 37
z = x / y
print(" x  /  y  =  z ")
print(f"{x} / {y} = {z}")
print(f"type of x: {type(x)}")
print(f"type of y: {type(y)}")
print(f"type of z: {type(z)}")


# Data-type casting | explicit conversions

# str + float
x = float("24.4")
y = 37.4
z = x + y
print(" x  +  y  =  z ")
print(f"{x} + {y} = {z}")
print(f"type of x: {type(x)}")
print(f"type of y: {type(y)}")
print(f"type of z: {type(z)}")


x = int(float("24.4")) # direct conversion leads to error
y = 37.4
z = x + y
print(" x  +  y  =  z ")
print(f"{x} + {y} = {z}")
print(f"type of x: {type(x)}")
print(f"type of y: {type(y)}")
print(f"type of z: {type(z)}")