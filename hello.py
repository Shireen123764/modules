# what is modular?....modular hum function banaty hen..  function in python.. is a modular programming in python..
#user defined modules in python

def shereen():
    select=input("what you want to use ?\n1. calc \n2. marksheet \n3.nothing")
    if select=="1":
        num1=int(input("enter a number"))
        num2=int(input("enter a number"))
        print(f"this is addition:{num1+num2} \nthis is subtraction:{num1-num2} \nthis is multiplication:{num1*num2} \nthis is division:{num1/num2}")
                 
    elif select=="2":
        obtain=int(input("enter your obtain marks:"))
        total=500
        per=(obtain/total)*100
        if per>=70:
            grade="A+"
        else:
            grade="fail"
        print(grade)           
                 
           
             
