# -*- coding: utf-8 -*-
"""loopsprobemsset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qsx-JrFCeQkdbb_Dr3PkKGB9eNhvuhDz
"""

#Sum of first n natural numbers:
n = 5
sum =0
for i in range(1,n+1):
  sum +=i
print(sum)

n = 5
sum = 0
i = 1
while i <=n:
  sum+=i
  i+=1
print(sum)

#Printing even numbers till 10:
n =10
for i in range(1,n+1):
  if (i%2==0):
    print(i)

n =5
fact = 1
i = 1
while i<=n:
  fact=fact*i
  i = i+1
print(fact)

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print(fact)