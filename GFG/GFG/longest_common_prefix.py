"""
Given a set of strings, find the longest common prefix.
"""

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]

arr.sort()

prefix = ""

print(arr[0])
for i in range(len(arr[0])):
    print(arr[0][i])
    if all(x[i] == arr[0][i] for x in arr):
        prefix += arr[0][i]
    else:
        break
print(prefix)
