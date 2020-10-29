# Counter
# Demonstrates the range() function

name = "Madhuri"
numbers = [[12,30,40],
           [30,40,50]]

#Prints the lists
for c in numbers:
    print(c)

#prints 4th element in the set "madhuri" 
print(name[4])
#prints the no in the array
print(numbers[1][2])

array_ex = [[44,45,46,47,48],
            [55,56,57,58,59],
            [66,61,63,64,67]]

for i in array_ex:
    for i in enumerate(array_ex,start=0):
        print(i)
 
    
print("Counting:")
for i in range(10):
    print(i, end=" ")

#counts in steps of 5
print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

#countdown frm 10 to 0
print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")



