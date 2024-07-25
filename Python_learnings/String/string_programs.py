"""
Write a program to accept some string from the keyboard and display its characters by
index wise(both positive and negative index)
"""

s = input("Enter the string\n")
i = 0
for x in s:
    print("Positive index {}, Negative index {} and Char {} ".format(i, i - len(s), x))
    i = i+1
