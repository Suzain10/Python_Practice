# -*- coding: utf-8 -*-
"""Strings_mod2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t08kxV9cVQN356qj518IWuVaZ0qqYRmo
"""

s = "Hello"
print(s[4])

s = "Hello"
print(s[:3])

s = "Hello"
print(s[:-1])

s = "Hello"
print(s[13])

s = "Hello"
print(s[1.5])

s = "Hello"
s[3]="p"

del s

print(s)

s1 ='Hello '
s2 ='Satish'
print(s1 + s2)
print(s1*3)

count = 0
for letter in "elephantly":
  if letter == 'y':
    count +=1
print(count)

s = "Slovakia"
print('lo' in 'Slovakia')
s.lower()

str = 'My name is Suzain '
str1 = str.split()
print(str1)

str1 ='-'.join(['My', 'name', 'is', 'Suzain'] )
print(str1)

str1 = 'My-name-is-Suzain-'
str2=str1.split('-')
print(str2)

str1 = '-'.join(['My', 'name', 'is', 'Suzain', ''])
print(str1)

str1 = 'Good Morning'
str2=str1.find('Mo')
print(str2)

str1 = 'Good Morning'
str2=str1.replace('Mo','Mooor')
print(str2)

mystr = input("Enter the string:")
revstr = reversed(mystr)
if list(mystr) == list(mystr):
  print("Palindrome")
else:
  print("Not Palindrome")

myStr = "python program to sort words in alphabetic order"
words = myStr.split()

words.sort()
for word in words:
  print(word)

