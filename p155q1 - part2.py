# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:27:23 2019

@author: madhu
"""
import random

value = {}
Daddyfin = {"mitchell" : "Jay", "sheldon" : "cooper", "luke" : "Darth", "walt" : "disney"}
trials=0
print("There are many Famous Dad:Son pairs")
print("how many do you know?")

while trials< 5:
    key = input("Enter a dad name : ")
    val = input("Enter a son name : ")
    Daddyfin[key]=val
    #flag = input("do you want to enter a new pair? 0/1  : ")
    trials += 1

print(Daddyfin.keys())
values = Daddyfin.values()
print(values)

