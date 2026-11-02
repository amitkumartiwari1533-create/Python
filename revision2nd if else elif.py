#Question1
num=int(input("enter the num"))
if num>0:
    print("num is positive")
    if num>=10:
        print("and num>10")
    else:
        print("and num<10")
else:
    print("num is negative")

#Question2
num1=int(input("enter the num1:-"))
if num1%2==0:
    if num1%4==0:
        print("num is even and div by 4")
    else:
        print("num is even and not div by 4")
else:
    print("num is odd")

#Question3ATM WITHDRAWAL
pin=int(input("enter the pin:-"))
if pin==1975:
    amount=int(input("enter the amount:-"))
    if amount<=5000:
        print("withdraw done")
    else:
        print("garib ho tum")
else:
    print("chor ho aap")

#Question4 
num2=int(input("enter a number:- "))
if num2>0:
    print("number is positive")
    if num2%2==0:
        if num2%4==0:
            print("number is positive and even and div by 4")
        else:
            print("number is positive and even but not div by 4")
    else:
        ("nummber is odd")
else:
    print("number is negative")

#Question5
a=int(input("enter a 1st num"))
b=int(input("enter a 2nd num"))
if a>=b:
    if a%2==0:
        print()

    