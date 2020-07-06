def total(s=100,c=0):
    temp=s-apple-c
    print(temp)
def total2(s=100):
    temp2=s-apple
    print(temp2)

apple = int(input("Enter how much apples you want?"))
while apple <= 5:
    b = input("these apples are very fresh last long..you want to buy more?")
    if b == "yes":
        c = int(input("how many apples you want ?"))
        print("remaining")
        total()
        continue
    elif b == "no":
        print("Thank you for shopping with us.visit again!")
    print("remaining")
    total2()
    break
else:
    while apple >> 5:
        print("Thank you for shopping with us.visit again!")







