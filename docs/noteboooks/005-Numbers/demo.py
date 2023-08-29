# Numbers
# - integers
#   - large integers
# - floating point numbers
#   - large float values
#   - scientific notation
# - complex numbers
# - inbuilt functions/methods for numbers
#   - abs, divmod, pow, and round


# - integers
#   - large integers
x = 10000000
y = 10_000_000 # 10,000,000
z = 10,000,000 # avoid this
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")

# - floating point numbers
#   - large float values
x = 10000000.75
y = 10_000_000.75 # 10,000,000.75
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")

# - floating point numbers
#   - scientific notation x >> 1 and x >= 0 (positive)
x = 12_000.00 
y = 1.2 * 10 ** 4
z = 1.2e4
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")

x = 12_000 
y = int(1.2 * 10 ** 4)
z = int(1.2e4)
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")

#   - scientific notation x << 1 and x >= 0 (positive)
x = 0.00012
y = 1.2 * 10 ** -4
z = 1.2e-4
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")

x = 0.00012
y = 1.2 * 10 ** -4
z = 1.2E-4
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")

# - complex numbers
x = 3 + 4j
y = -2 - 3j
z = 1j # equivalent to 0 + 1j, aka perfect complex numbers
a = 0j
b = 1+0j # complex number with real part only
print(f"Value: x={x} | type: {type(x)}")
print(f"Value: y={y} | type: {type(y)}")
print(f"Value: z={z} | type: {type(z)}")
print(f"Value: a={a} | type: {type(a)}")
print(f"Value: b={b} | type: {type(b)}")

# - inbuilt functions/methods for numbers
#   - abs

x = -5
result = abs(x)
print(f"BEFORE: {x}, AFTER: {result}")

x = 5
result = abs(x)
print(f"BEFORE: {x}, AFTER: {result}")

# - divmod 
x = 10
y = 3

quotient, reminder = divmod(x, y)
print(f"{x}/{y}, quotient: {quotient}, reminder: {reminder}")

x = 10
y = 5

quotient, reminder = divmod(x, y)
print(f"{x}/{y}, quotient: {quotient}, reminder: {reminder}")


x = 10
y = 2

quotient, reminder = divmod(x, y)
print(f"{x}/{y}, quotient: {quotient}, reminder: {reminder}")


x = 11
y = 2

quotient, reminder = divmod(x, y)
print(f"{x}/{y}, quotient: {quotient}, reminder: {reminder}")


# - pow
x = 2
y = 3
z = pow(x, y)
print(f"{x} to the power of {y} = {z}")

# - round
# without specifying upto 
# what decimal point you want to round off

x = 3.14159
result = round(x) 
print(f"BEFORE: {x}, AFTER: {result}")

x = 3.9
result = round(x) 
print(f"BEFORE: {x}, AFTER: {result}")

x = 3.4
result = round(x) 
print(f"BEFORE: {x}, AFTER: {result}")

x = 3.5
result = round(x) 
print(f"BEFORE: {x}, AFTER: {result}")

# round upto one decimal places
x = 3.45
result = round(x, 1) 
print(f"BEFORE: {x}, AFTER: {result}")


# round upto one decimal places
x = 3.43
result = round(x, 1) 
print(f"BEFORE: {x}, AFTER: {result}")

# round upto two decimal places
x = 3.44567
result = round(x, 2) 
print(f"BEFORE: {x}, AFTER: {result}")

# round upto three decimal places
x = 3.44567
result = round(x, 3) 
print(f"BEFORE: {x}, AFTER: {result}")

# avoid using it not a proper round up
x = 3.6
result = int(x) # another way but wrong way to round up
print(f"using 'int' BEFORE: {x}, AFTER: {result}")
result = round(x) # another way but wrong way to round up
print(f"using 'round' BEFORE: {x}, AFTER: {result}")