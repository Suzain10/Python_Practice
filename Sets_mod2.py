# -*- coding: utf-8 -*-
"""Sets_Mod2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u0Xd5kqxccJYLaG2PhYoK-fCsVhvt93A
"""

s = set()
print(type(s))

s = {1,2,3,5,42,1,6,1,1,6,9,7,8}
print(s)

s =set([1,12,3,4,5,9,1,1,8])
print(s)

s = {1,2,3}
s.add(5)
print(s)

s = {1,2,3}
s.update([5,6,3,2,1,1],{10,12,3})
print(s)

s = {1,2,3,4,5,7}
s.remove(7)
print(s)

s = {1,2,3,4,5,7}
s.pop()
print(s)

s = {1,2,3,4,5,7}
s.clear()
print(s)

set1  = {1,2,3,4,5,6}
set2 = {5,6,7,8}
print(set1 | set2)

set1  = {1,2,3,4,5,6}
set2 = {5,6,7,8}
print(set1.union(set2))

set1  = {1,2,3,4,5,6}
set2 = {5,6,7,8}
print(set1 & set2)
print(set2 - set1) #difference

print(set2 ^ set1) #Symmertic difference

x = {"a","b","c","d"}
y = {"c","d"}

print(y.issubset(x))

set1 = frozenset([1,2,3,4,5])  #immutable sets
set1.add(4)
print(set1)

print(set1[2])

