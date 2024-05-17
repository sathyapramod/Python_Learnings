"""
Interesting facts about strings in Python | Set 1
1. Strings are Immutable
2. Three ways to create strings
"""

a = 'Geeks'
print(a)

# a[2] = 'E'
# print(a) # TypeError: 'str' object does not support item assignment

# a string can be appended to a string.

a = a + 'for'
print(a)


string1 = "hello"
string2 = "hello"
print(id(string1))
print(id(string1))

# strings in three different
# ways and concatenate them.

# string with single quotes
a = 'Geeks'

# string with double quotes
b = "for"

# string with triple quotes
c = '''Geeks a portal  
for geeks'''

d = '''He said, "I'm fine."'''

print(a)
print(b)
print(c)
print(d)

# Concatenation of strings created
# using different quotes
print(a + b + c)