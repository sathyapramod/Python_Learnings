"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example:
    arr = [1,3,5,7,9]
    The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24. The function prints 16 24
"""

arr = [1, 3, 5, 7, 9]

total_sum = sum(arr)
print(total_sum)

sums = []
for i in arr:
    sums.append(total_sum - i)

print(sums)
print(min(sums), max(sums))
