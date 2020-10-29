# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:59:38 2019

@author: madhu
"""


Strength = int(input("Enter your Point Choice for 1>Strength: "))
print("1> Strength: %d"%Strength, "You have remaining points", 30 - Strength)
Health = int(input("Enter your Point Choice for 2>Health: "))
print("2> Health: %d"%Health, "You have remaining points", 30 - (Strength + Health))
Wisdom = int(input("Enter your Point Choice for 3>Wisdom: "))
print("3> Wisdom: %d"%Wisdom, "You have remaining points", 30 - (Strength + Health+ Wisdom))
Dexterity = int(input("Enter your choice for 4>Dexterity: "))
print("4> Dexterity: %d"%Dexterity, "\nyou have no more points")

print(" Hit Enter")
