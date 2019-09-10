
def convert(temp):
    ctemp = (temp - 32) *5/9
    return ctemp


##temp = int(input("ENTER the temperature to convert: "))
##ctemp = convert(temp)
##print("Here is the temperature in celsius: %3.2f"%ctemp)



capture = {}
temp1 = [13,21,36,45,52,66,73,89,96,100]
listed_temp = set()

for i in range(10,100,10):
    ctemp1 = convert(i)
    listed_temp.add(ctemp1)
    #listed_temp.append(ctemp1)
    #print(ctemp1)

print(listed_temp)

print("\n\n\nEnd of list in the range of 10s ctemp1!!!!!!!")
for key in temp1:
    value = convert(key)
    print(value)
    capture[key] = value

print("End of keys list:\n\n")

for i in capture:
    print(i,"=======>",capture[i])
    text_file = open("temperature.txt", "a")
    text_file.write("temperatures\n\n")
    text_file.write(capture[i])
    text_file.close()
##text_file = open("temperature.txt", "a")
##text_file.write("temperatures\n\n")
##text_file.write(capture)
##text_file.close()


