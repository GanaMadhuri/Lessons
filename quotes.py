user_entry = input("Enter your Desired Quote:: ")
by = input(" Enter the person quotes:: ")
text_file = open("Quotes.txt", "w+")
text_file.writelines(user_entry.upper())
text_file.writelines("\n\n")
text_file.writelines(by.title())
text_file.writelines("\n\n")
text_file.close()

print("\nReading one line at a time.")

text_file = open("Quotes.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()


f = open("Quotes.txt", "a")
f.write("MANY QUOTES by MANY GREAT PPL")
f.close()

print("\nLooping through the file, line by line.")
text_file = open("Quotes.txt", "r")
for line in text_file:
    print(line)
text_file.close()
