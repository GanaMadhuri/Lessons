# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:45:44 2019

@author: madhu
"""
import random
value= []

words = ["tough","scotch","poppin", "burrito", "pictures", "help", "dinner"]
num = len(words)
print("here is the big start: ")
#     
#for i in words:
#    value.append(random.choice(words))
#print(value)

print(words)
random.shuffle(words)
print(words)
  

#
#import random
#
#b = []
#a = int(input(print("How many items you want to shuffle? ")))
#for i in range(0, a):
#    n = input('Please enter a item: ')
#    b.append(n)
#
#random.shuffle(b)
#
#print(b)
