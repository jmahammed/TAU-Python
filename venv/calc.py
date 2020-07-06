def addition():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    print(a+b)

def substraction():
    a=float(input("Enter number"))
    b=float(input("Enter another number"))
    print(a-b)

def mul():
    a=float(input("Enter numer"))
    b=float(input("Enter another number"))
    print(a*b)

def div():
    a=float(input("Enter number"))
    b=float(input("enter another number"))
    print(a/b)

operation=input("please select +,_,*,?")
if operation=="+":
    addition()
elif operation=="-":
    substraction()
elif operation=="*":
    mul()
elif operation=="/":
    div()
else:
    print("There is no such operation")