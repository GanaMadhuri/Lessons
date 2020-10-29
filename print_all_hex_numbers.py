# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:30:14 2019

@author: madhu
"""

#def this_fails():
#    x = 1/0
#    
#try:
#     this_fails()
#except ZeroDivisionError as err:
#            print('Handling run-time error:', err)

 
#result = ["0x%02x" % x for x in range(256) if x % 2 == 0] 
#print(result)
#print(type(result))
value = []

for i in range(25):
    print(i, end = " ")
    value.append(i)

print(value)
for i in value:
    print(i,f"===> 0x%x"%i,end = "   ")