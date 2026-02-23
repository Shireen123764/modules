import hello
import hello_2


# hello.shereen()
# hello_2.table()
# hello_2.gassing()
# hello_2.atm()                   

print("which one do you want?")
print("1.multiple function")
print("2.table ")
print("3. gassing game")
print("4.atm")
choose=int(input("choose one"))
if choose==1:
    hello.shereen()
elif choose==2:
    hello_2.table()
elif choose==3:
    hello_2.gassing()
elif choose==4:
    hello_2.atm()
else:
    print("invalid")