# -*- coding: utf-8 -*-
"""While_Loop(Practice).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NFIp3H3fXhhUCKAEm46s8632AI-yVDv4
"""

i = 5
while(i > 0):
  print("The value of is is: ",i)
  i = i-1

i = 5
while(i >0):
  print("Hello", i)
  i = i - 1

i = 0
while(i<10):
  print(i)
  i = i+1
print('Done with the loop!')

i = -10
while(i < 0):
  print(i)
  i =i+1
else:
  print("Hello there!!")

for i in range(12):
  print("5 X",i+1,"=",5*(i+1))
  if (i==10):
    break
print("break skips part of code and terminates the loop")

for i in range(12):
  if (i==10):
    print("Skips the iteration and moves forward")
    continue
  print("5 X",i,"=",5*i)

i = 0
while (i<12):
  i = i+1
  if (i == 10):
   print("Skips this interation and moves forward")
   continue
  print("5X", i,"=",5*i)

x = int(input())
match x:
  case 0:
    print("x is zero")
  case 1:
    print("x is one")
  case 4:
    print("x is four")
  case _:   #Indicates default case,if above cases don't match,this takes up the value.
    print("x is", x)

x = int(input())
match x:
  case 0:
    print("x is zero")
  case 1:
    print("x is one")
    #case with if condition:
  case 16 if x%2==0:
    print("x %2 ==0 and case is 4")
    #Empty case with if condition:
  case _ if x <10:
    print("x is less than 10")
  case _:
    print(x)

