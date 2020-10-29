# input example and overloading



#num1=input("enter number 1 ")
#num2=input("enter number 2 ")
# overloading the + operator

# casting string int(variable1)
num=float(input("Enter First number  "))
num2=float(input("Enter Second number  "))
numSum = num1+num2
print("Number Addition" , num1, "and", num2,"is", numSum)
tell=[num1,num2]
print(tell," is the list of the whole variables we used")
#test=(sum(num1,num2))
#print(test)
test2=sum(tell)
print(test2)