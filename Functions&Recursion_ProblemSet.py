# -*- coding: utf-8 -*-
"""Functions&RecursionProblemset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z4KgU_Djm15lEhM61a0FcPwwhemsDipn
"""

def sum(x):
  if(x==0):
    return 0
  return sum(x-1)+x
print(sum(5))

def list_print(list,idx=0):
  if(idx==len(list)):
   return
  print(list[idx])
  list_print(list,idx+1)
fruits=['Mango','Banana','Litchi','Fig']
list_print(fruits,1)
