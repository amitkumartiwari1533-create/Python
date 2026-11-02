#Question1
a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))
if a>0:
    if a>b:
        print(f"{a} is positive and {a} is greater then {b}")
    else:
        print(f"{a} is positive and {a} is less then {b}")
else:
    print(f"{a} is not positive")

#Question2
sub1=int(input("enter a 1s subject marks:- "))
sub2=int(input("enter a 2nd subject marks:- "))
if sub1>=33:
    if sub2>=33:
        print("Pass")
else:
    print("Fail")

#Question3
