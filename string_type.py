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

