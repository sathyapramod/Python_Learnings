"""
Python program to check whether the string is Symmetrical or Palindrome

Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""
import re

input_string = "amaama"
reverser_string = input_string[::-1]
print(reverser_string)

if input_string == reverser_string:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if re.match(r"^(\w+)", input_string) and input_string == reverser_string:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")
