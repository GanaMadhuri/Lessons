

num_pnt = int(input("Enet a number to loop "))


while num_pnt > 0:
    #num_pnt -= 1
    num_pnt -= 1

    if num_pnt == 13:
        continue

    if num_pnt == 0:
        break
    else:
        print("T- Minus", num_pnt ,"seconds for blastoff")
   
print("Have a nice day!")
