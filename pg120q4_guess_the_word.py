# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:58:43 2019

@author: madhu
"""
import random

words = ["tough","scotch","poppin", "burrito", "pictures", "help", "dinner"]
#num = int(input("Enter a number from the pile"))
notrials = 1
flag = 0
computerword = random.choice(words)
print(computerword)
userword = input(" Enter the word the computer is thinking:  ")

while notrials < 3:
        
    if userword == computerword:
        flag = 1
        break
       
    else:
        print("try again!!!")
        print("YOu have tried %d"%notrials)
        userword = input("Enter the word:  ")
        notrials += 1
        
        #print(notrials)
    
    
if flag == 1:
    print("You GUESSED it!! in %d tries = "%notrials)
else:
    print("Play again: Better luck next time")
    
input("Hit Enter to escape")