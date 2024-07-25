"""
How to Remove number From a String in Python
Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
"""

string1 = 'Geeks987For457Geeks'
# new_string = string[:5] + string[8:11] + string[14:]
# print(new_string)

# new_string = string.replace('123', '')
# print(new_string)

s1 = " "
# for i in string1:
#     if 49 <= ord(i) <= 57:
#         continue
#     else:
#         s1 = s1 + i
# print(s1)

for i in string1:
    if i.isdigit():
        continue
    else:
        s1 = s1+i
print(s1)
