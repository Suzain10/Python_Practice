# -*- coding: utf-8 -*-
"""ifelseprobset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XDYj03hX5IASn-dqMayX3XKMbBsem3wH
"""

##Checking if the number is even/odd:
num = int(input("Enter the value for num: "))
if(num%2==0):
  print("The number is even.")
else:
  print("The number is odd.")

#Finding the largest of three numbers:
x =int(input("Enter the value for  x: "))
y =int(input("Enter the value for  y: "))
z =int(input("Enter the value for  z: "))

if(x == y == z):
    print("All values are same")
elif(x>y and x>z):
  print("x is the largest number")
elif(y>x and y>z):
  print("y is the largest number")
elif(z>x and z>y):
  print("z is the largest number")
else:
    print("Two values are same")

#Checking if a num is multiple of 7:
x =int(input("Enter the value for  x: "))
if(x%7==0):
  print(f"{x} is the multiple of 7.")
else:
  print(f"{x} is not the multiple of 7.")

#Checking if a person can drive:
age = int(input("Enter your age:"))
if age>=18:
  if age>=80:
    print("Old cannot drive")
  else:
    print("Can drive")
else:
  print("Cannot drive")