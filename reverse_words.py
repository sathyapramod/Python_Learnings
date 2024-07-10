"""
Reverse Words in a Given String in Python

Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks
Input : str = "my name is laxmi"
output : str= laxmi is name my
"""

string = " geeks quiz practice code"
reverse_word = string.split()[::-1]
print(" ".join(reverse_word))

