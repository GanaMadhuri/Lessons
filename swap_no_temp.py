# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:08:53 2020

@author: madhu
# =============================================================================
# """# PROGRAM TO SWAP TWO NOS WITH NO TEMP
# =============================================================================
#
#a=10
#b=20
#a=a+b
#b=a-b
#a=a-b

#print(a,b)
# =============================================================================
# #PROGRAM TO ADD NOS WITH A SINGLE DIGIT
# # k+kk+kkk
# =============================================================================

#
#k=int(input("enter a digit no"))
#this=k+((k*10)+k)
#that=this+((k*100)+this)
##print(this)
#print(that)
# =============================================================================
# #PROGRAM TO CHECK THE NOS DIV BY NOT 2 OR 3 AND IN BETWEEN 1 TO 50
# =============================================================================
#
#div_arr=range(1,50)
##print(div_arr)
#for i in range(1,51):
#    
#    if(i%2==0&i%3==0):
#        pass
#    else:
#        print(i)
## =============================================================================
# #natural numbers summation pattern
#1=1
#1+1=2
#1+2+3=5
# =============================================================================

#k = int(input("enter a no less than 100: "))
#k=10
tot=0
a=[]
for i in range(1,10):
    print(i,"+")
    
    tot+=i
print("=")
print(tot)
for i in range(1,10):
    print(i,sep= " ",end=" ")
    a.append(i)
    print("+",sep=" ",end=" ")
print("=",tot)
a.append(tot)
print(a)
#a=[]   
#    
#for i in range(1,50):
#    print(i,sep=" ",end=" ")
#    if(i<50):
#        print("+",sep=" ",end=" ")
#    a.append(i)
#print("=",sum(a))
# =============================================================================
# # Prime Numbers print
# ========================================================================
#primes=[]
#flag=False
#for x in range(1,100):
#    for y in range(2,x):
#        if x%y==0:
#            flag==False
#            break
#    else:
#        print(x,"prime")
#        primes.append(x)
#print(primes)

# =============================================================================
# 1+1/2+1/3+1/4
# =============================================================================

number =10
tot=0.0
for i in range(1,10):
    j=1/i
    print("1/",i,"+")
    tot=tot+j
print(tot)
    
        


