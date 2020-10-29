import random


heads = 0
tails = 0
flips = 0
flip=0
while flips < 100:
    possValue = random.randint(0,1)
    print(possValue, end = ' ')
    if possValue == 0:
        heads +=1
    else:
        tails += 1
    flips += 1

print("The total statistic for a 100 flips:")
print("No of Heads: ", heads, "No of Tails: ",tails)


##while flips < 100:
##    flip = random.randint(0,1)
##    #print(flips, end = ' ')
##    if flips:
##        heads +=1
##    else:
##        tails += 1
##    flips += 1
    
print("The total statistic for a 100 flips:")
print("No of Heads: ", heads, "No of Tails: ",tails)
