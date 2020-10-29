#restruant bill and tip


waiter="madhu"
print(''' Welcome to Hotel Califonia ''')
num1=float(input("enter bill: "))
tip1=num1* 0.15
tip2 =num1* 0.20
print("Your bill is " , num1, "\nplease tip to waiter: ", waiter.upper())
print("Sugested tip 15%",tip1,"you pay a total", num1+tip1,end="")
print( "\t\t\t Suggested tip 20%", tip2,"you pay a total", num1+tip2)
print("\a")


