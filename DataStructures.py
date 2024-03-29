# -*- coding: utf-8 -*-
"""DataStructures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14jZSV-AkkbAnpGASlfQOdqJJ03pK4WYo
"""

# Basic operations on lists

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of a list
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slice of the list:", my_list[1:4])

# Modifying elements of a list
my_list[2] = 10
print("Modified list:", my_list)

# Appending to a list
my_list.append(6)
print("List after appending:", my_list)

# Removing from a list
my_list.remove(4)
print("List after removing:", my_list)

# Checking if an element is in the list
print("Is 3 in the list?", 3 in my_list)

# Length of the list
print("Length of the list:", len(my_list))

# Iterating over a list
print("Iterating over the list:")
for item in my_list:
    print(item)

# Sorting a list
my_list.sort()
print("Sorted list:", my_list)

# Reversing a list
my_list.reverse()
print("Reversed list:", my_list)

# Basic operations on strings

# Declaring a string
my_string = "Hello, world!"

# Accessing characters of a string
print("First character:", my_string[0])
print("Last character:", my_string[-1])
print("Slice of the string:", my_string[7:12])

# Concatenating strings
new_string = my_string + " Have a nice day!"
print("Concatenated string:", new_string)

# String length
print("Length of the string:", len(my_string))

# Checking if a substring is in the string
print("Is 'world' in the string?", 'world' in my_string)

# Counting occurrences of a character or substring
print("Number of 'l's in the string:", my_string.count('l'))

# Replacing substrings
new_string = my_string.replace('world', 'universe')
print("String after replacement:", new_string)

# Converting case
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())

# Splitting a string
split_string = my_string.split(',')
print("Split string:", split_string)

# Joining strings from a list
words = ["Hello", "world", "again"]
joined_string = ' '.join(words)
print("Joined string:", joined_string)

# Basic operations on tuples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice of the tuple:", my_tuple[1:4])

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Length of the tuple
print("Length of the tuple:", len(my_tuple))

# Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Checking if an element is in the tuple
print("Is 3 in the tuple?", 3 in my_tuple)

# Iterating over a tuple
print("Iterating over the tuple:")
for item in my_tuple:
    print(item)

# Nesting tuples
nested_tuple = (my_tuple, another_tuple)
print("Nested tuple:", nested_tuple)

# Tuple packing
packed_tuple = 1, 2, 3
print("Packed tuple:", packed_tuple)