"""
Reverse words in a given String in Python
Given a string, the task is to reverse the order of the words in the given string.
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks
Input : str = "my name is laxmi"
output : str= laxmi is name my
"""

s = input()
sl = s.split()
sl = sl[::-1]
sj = " ".join(sl)
print(sj.capitalize())

"""
Each words first letter should be capital
"""

# s = "geeks quiz practice code"
# print(s.capitalize())
# l = s.split(" ")
# print(l)
# ll = []
# for i in l:
#     ll.append(i.capitalize())

# print(" ".join(ll))
