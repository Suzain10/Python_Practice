# -*- coding: utf-8 -*-
"""Tuple.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsAOSroWLf6eJLdIFqJxKVcKRuu86uA9
"""

tup = (1,3,2,7,5,"Theo",True)
print(type(tup))

print(tup)

tup1 = (1)
type(tup1)
tup1 = (1,)
type(tup1)

print(tup[2:5])

if "Theo" in tup:
  print("Yes")

print(tup[2:7:2])
print(tup[2::2])  #Both are same

print(tup[::2]) #Prints alternative values

print(tup[2::2])

countries =("Russia","Greece","Poland","Auckland")
print(type(countries))

temp_1 =list(countries)
print(temp_1)

print(type(temp_1))

temp_1.append("Brazil")

print(temp_1)

temp_1.sort()
print(temp_1)



temp_1.reverse()
print(temp_1)

temp_1.pop(2)
print(temp_1)

temp_1[3]="Germany"
print(temp_1)

countries = tuple(temp_1)
print(countries)

tupl1 = (1,6,4,2,4,4,7,9,8,6)
print(tupl1)

print(tupl1.index(4,1,7))

print(tupl1.count(6))

print(tupl1.index(6))

