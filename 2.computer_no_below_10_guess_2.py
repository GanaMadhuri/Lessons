# Granted or Denied
# Demonstrates an else clause

import random

print("Guess the Number from 1 to 10")
guess_no  = int(input("Enter your number: "))
random_no = random.randint(1,10)
i = 0
no_of_tries = 5
#guess_no = random_no

while i < no_of_tries:

    if guess_no == random_no:
        print("you guessed right")
        
    elif guess_no < random_no:
        print("the no is lesser")
        #guess_no = int(input("enter a no: ")
       
    elif guess_no > random_no:
        print("the no is greater")
        #guess_no = int(input("enter a no: ")
        break
        #continue
    else:
        print("NOPE! NOT IT")

print("computer no is %f"%random_no)
input("\n\nPress the enter key to exit.")
