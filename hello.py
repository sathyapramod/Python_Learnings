"""
Write a program to print hello world! In the console
"""

print("Hello World!")

"""
Creating variable and assigning values
<variable name> = <value>
"""

# Integer
a = 2
print(a)
print(type(a))

# Floating point
pi = 3.14
print(pi)
print(type(pi))

# String
b = 'A'
print(b)
print(type(b))

name = 'Sathya Pramod'
print(name)

# Boolean
q = True
print(q)
print(type(q))

# Empty or null
x = None
print(x)
print(type(x))

# File handling

# with open('abc.txt', 'w') as f:
#     f.write('abc\n')
#     f.write('xyz\n')
#     f.write('qwerty\n')
#     print("Is closed:", f.closed)
#     print("Successful")

f = open('abc.txt', 'r')
print(f.tell())
print(f.read(10))
print(f.tell())
