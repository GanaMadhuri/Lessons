#restruant bill and tip

import random
from datetime import date, time, datetime

print('''                               Restraunt ala Food
                                        123 40th Ave NE
                                        Regal City WA 98072                      ''')
print('''                               SALES RECEIPT                            ''')
                                
dt = date.today()
 
print('''Transaction #:         ''' ,random.randint(100000,200000))
print('''Date:          ''', date.today() , datetime.now() ,dt.strftime("%A %d. %B %Y")
,'''\nRegister #: ''',random.randint(1,10))
waiter="madhu"
cheeseBurger = 5.95
bevRage=1.45
print(waiter.upper())
print('''ITEM           DESCRIPTION                 AMOUNT
      ----------        -----------                --------
      ----------        -----------                --------
         1              Cheese Burger              ''',cheeseBurger,
        '''\n\t\t 2              Beverage                    1.45''')
num1=float(input("ENTER BILL TOTAL: "))
tip1=num1* 0.15
tip2 =num1* 0.20
print("Your bill is " , num1, "\nplease tip to waiter: ", waiter.upper())

print("\nSugested tip for 15%,",tip1,"You pay a total", num1+tip1,end="")
print( "\nSuggested tip for 20%", tip2,"you pay a total", num1+tip2)
#print("\a")

