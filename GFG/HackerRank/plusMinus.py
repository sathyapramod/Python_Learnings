"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
"""

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = []
    negative = []
    zero = []

    for i in arr:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)

    print("{:.6f}".format(len(positive)/len(arr)))
    print("{:.6f}".format(len(negative)/len(arr)))
    print("{:.6f}".format(len(zero)/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
