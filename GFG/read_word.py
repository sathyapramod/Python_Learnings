"""
Python program to read file word by word
"""

with open('abc.txt', 'r') as f:
    f = f.read()
    f1 = []
    for i in f.split():
        f1.append(i)
    print(f1)
    print(len(f1))

"""
Python program to read character by character from a file
"""
with open('abc.txt', 'r') as f:
    f = f.read()
    f1 = []
    for i in f.replace(' ', ''):
        f1.append(i)
    print(f1)

"""
Count number of lines in a text file in Python and ignore if it's empty
"""
with open('abc.txt', 'r') as f:
    f = f.readlines()
    print(len(f))

with open('abc.txt', 'r') as f:
    f = f.readlines()
    f1 = []
    for i in f:
        if i is '\n':
            pass
        else:
            f1.append(i)
    print(len(f1))


