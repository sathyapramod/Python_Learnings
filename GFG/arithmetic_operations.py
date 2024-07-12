"""
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
"""
a = int(input())
b = int(input())


def sum_sub_mul(a, b):
    print((a + b), (a - b), (a * b), sep="\n")


sum_sub_mul(a, b)
