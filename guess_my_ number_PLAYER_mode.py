# Guess My Number
#
# The player picks a random number between 1 and 100
# The player inputs it and the computer guesses
# 


import random

user_no = int(input("PLEASE ENTER YOUR NUMBER AND DO NOT SHOW IT TO THE COMPUTER:  "))
tries = 0
comp_no = random.randint(1,100)
print("The Computer's Guess First Time is %d"%comp_no)
while comp_no != user_no:
    print('keep guessing')
    tries = tries +1
    comp_no = random.randint(1,100)
    print("Computer Guessing : ", comp_no)
    
print("\nComputer Tries for %d"%tries,"times")
print("COMPUTER guesses the USER Input")

