
# Bonus calculator

X = 5
y = 0

try:
    while y > 5 or y < 1:
        y = int(input("Enter a number less than five: "))
except ValueError as e:
            print(e)

try:
    bonus = 1000 / (X - y)           
except (ZeroDivisionError,NameError,ValueError) as e:
    print("Please check your INPUT.")
    print(e)
else:
    print("Your bonus is $%3.2f" % bonus)

