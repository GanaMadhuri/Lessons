# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:38:21 2019

@author: madhu
"""

start = int(input("Enter the start range: "))
end = int(input("Enter the start range: "))
step = int(input("Enter the skip beat that you want:  "))
value = []
for i in range(start,end,step):
    value.append(i)
    print(i, end = " ")
    
    
print("\n\n\n value list is",value)