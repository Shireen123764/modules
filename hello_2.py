def table():
    num = int(input("enter a table number:"))
    range_limit = int(input("enter a table range:"))

    for i in range(1, range_limit +1):
        result = num * i
        if result > 50:
            print("Result exceeded 50. Loop stopped.")
            break
        
        if result % 2 == 0:
             print(f"{num} X {i} = {result} (even)")

        elif result % 2 != 0:
             print(f"{num} X {i} = {result} (odd)")



def gassing():

    secret=12

    for chance in range(1,4):
        guess=int(input(f"attempt {chance} :guess the number:"))
        if guess == secret:
            print("hey you win!")
            break
        elif guess != secret:
            print("Do you want hint?(1.yes/2.No")
            hint=int(input("choose one:"))
            if hint==1:        
                print("8,10,12,15")
            else:
                print("no worries try your self")
        else:
            print(" try again")
                
    
def atm():    
    control = True
    while control:
        card=int(input("Insert Your Card:\n1. Insert Card \n2.Card Error: Enter your Choice:"))
        if card == 1:
             chance=3
             while chance >0:
                 pin=int(input("enter your pin:"))
                 if pin == 1234:
                    print("\n Welcome to the ATM")
                    control = False
                    menu=int(input("what do you want to do:\n1. fast cash \n2. withdraw \n3.balance Inquiry \n4. exit \nEnter Choice:"))
                    if menu == 1:
                        print("proceed to fast cash....")
                    elif menu == 2:
                        print("proceed to withdrawal....")
                    elif menu == 3:
                        print("your balance is 100000")
                    else:
                        print("exiting...")
                    break
                 else:  
                      chance -=1
                      print(f"wrong pin! {chance} left chance.")
                      
             else:                   
                print("card has been captured")
                
                
        else:
             print("card error")
             rerun=int(input("do you want to Insert card again?\n 1. yes \n2. No"))
             if rerun== 1:
                 continue
                       
             else:
                print(" Thank you for visiting us!")
                break
                       
    
    