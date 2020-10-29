# Counter
# Demonstrates the range() function

name = "Madhuri"
numbers = [[12,30,40],
           [30,40,50]]
categories = [[100,200,400],
              [300,200,500]]
for c in numbers:
   print(c)
    
print(name[4])
print(numbers[1][2])

numcat=zip(numbers,categories)
#sprint(len(numcat))
for i in numcat:
    print(i)
print("Array confusion down below")
total_arry = sum(numbers,categories)
for c in total_arry:
   print(c)
print(total_arry)

for j in sum(numbers,categories):
    print(j)
    
print("Counting:")
for i in range(10):
   print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
   print(i, end=" ")

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
   print(i, end=" ")

input("\n\nPress the enter key to exit.\n")

