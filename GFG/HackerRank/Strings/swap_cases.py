"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

s = "Sathya"
ns = ""
for i in s:
    if i.isupper():
        ns += i.lower()
    else:
        ns += i.upper()
print(ns)
