# -*- coding: utf-8 -*-
"""Lambda_Func.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sd7nLEKcD2bOPqa9_-NeX5ItBYjE0MR6
"""

double = lambda x:x*x

print(double(5))

cube = lambda x:x*x*x
print(cube(5))

print(double(cube(3)))

avg = lambda x,y:(x+y)/2
print(avg(2,3))

prod = lambda x,y:x*y
prod(2,3)

prod = lambda x,y:print(f"{x}*{y} = {x * y}")
prod(2,3)

