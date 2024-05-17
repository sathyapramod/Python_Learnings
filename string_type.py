"""
Strings : A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around
your strings
"""

s = "This is a String"
s1 = 'This is also a String'

# String Methods : title, upper, lower

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello !", full_name.title() + "!")

"""
Exercise problems of String
1. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
2. Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
3. : Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
4.  Repeat Exercise 3, but this time store the famous person’s name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.
5. Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(),rstrip(), and strip().
"""

# 1
name = "Eric"
message = "Hello " + name + " would you like to learn some Python today?"
print(message)

# 2
name = "mythi sathyapramod"
print(name.title())
print(name.upper())
print(name.lower())

# 3 & 4
name = "Albert Einstein"
quota = '"A person who never made a mistake never tried anything new."'
message = name + " once said, " + quota
print(message)

"""
Geeks for Geeks Strings
https://www.geeksforgeeks.org/python-string/#what-is-a-string-in-python
"""

# Accessing characters in Python String
#  Positive Indexing
String1 = "GeeksForGeeks"
print("Initial String: ", String1)

print("First character of String is ", String1[0])

# Negative Indexing
print("Last character of String is ", String1[-1])

# String Slicing Python
print("Initial String: ", String1)

# Printing 3rd to 12th character
print("Slicing character from 3-12: ", String1[3:12])

# Printing 3rd and 2nd last character
print("Slicing character between 3rd and 2nd last character: ", String1[3:-2])

# Deleting/Updating from a String
"""
Updating a character
A character of a string can be updated in Python by first converting the string into a Python List and then updating the element in the list. As lists are mutable in nature, we can update the character and then convert the list back into the String.

Another method is using the string slicing method. Slice the string before the character you want to update, then add the new character and finally add the other part of the string again by string slicing.
"""

String1 = "Hello, I'm a String!"
print("Initial String: ", String1)

# Method 1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("Updated 2nd index: ", String2)

# Method 2

String3 = String1[0:2] + 'p' + String1[3:]
print(String3)

# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
