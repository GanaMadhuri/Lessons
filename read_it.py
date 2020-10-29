# Read It
# Demonstrates reading from a text file



print("\nReading one line at a time.")
try:
    text_file = open("hello_world.txt", "w+")
except FileNotFoundError as e:
    print(e)
    print("no file found\n")
else:
    text_file.writelines("hello world!!!!")
    text_file.close()

print("\nReading the entire file into a list.")
text_file = open("hello_world.txt", "r")
lines = text_file.readlines()
print(lines) 
print(len(lines))
for line in lines:
    print(line)
text_file.close()

##print("Texting lists.")
##f = open("texting_new_age.txt", "a+")
##variety = ["sweet", "hot", "dill"]
##shape = ["whole", "spear", "chip"]
##brand = ["Claussen", "Heinz", "Vlassic"]
##f.writelines("\n\n")
##f.writelines(variety)
##f.writelines("\n\n")
##f.writelines(shape)
##f.writelines("\n\n")
##f.writelines(brand)
##f.close()
