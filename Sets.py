# -*- coding: utf-8 -*-
"""Sets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FwOqZKyop-Y__ZwE4uYdU941vSKLkqEi
"""

s = {1,4,3,2,3,3,2,4}
print(s)

s = {"Carla", 19,False,19} #Unordered
print(s)

s =set()
print(s)
print(type(s))

s = {"Carla", 19,False,19}
for value in s:
  print(value,end="/")

s1 = {1,4,9,7}
s2 = {7,9,8}
print(s1.union(s2))

print(s1.isdisjoint(s2))

a = {1,2,3}
b ={1,2}
print(a.issuperset(b))

a = {1,2,3}
b ={1,2}
print(b.issubset(a))

a = {1,2,3}
a.add(8)
print(a)

a = {1,2,3,4,"Tokyo"}
a.remove("Tokyo")
#a.discard("Tokyo")
b = a.pop()
print(a)
print(b)

a = {1,2,3}
del a
print(a)

a = {1,2,3}
a.clear()
print(a)

a = {1,2,3,"john"}
if "john" in a:
  print("Yes")
print(a)

s3 = s1.symmetric_difference(s2)
print(s3)

s3.difference
print(s3)

print(s1,s2)

s1.update(s2)

print(s1)

print(s2.intersection(s1))

s1.intersection_update(s2)
print(s1)