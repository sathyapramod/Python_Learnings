"""
https://www.hackerrank.com/challenges/write-a-function/problem
"""

year = int(input())


def is_leap(year):
    leap = False
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        leap = False
    else:
        leap = True
    return leap


print(is_leap(year))
