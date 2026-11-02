#in opertor use in place of or oprator 
#aeiouAEIOU
ch=input("enter a char")
if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonent")    

#STUDENT RESULT
maths=int(float(input("enter a maths marks :-")))
science=int(float(input("enter a science marks :-")))
english=int(float(input("enter a english marks :-")))
if maths>=40 and science>=40 and english>=40:
    print("pass")
else:
    print("fail")

#compare three number
num1=int(input("enter a num1 : "))
num2=int(input("enter a num2 : "))
num3=int(input("enter a num3 : "))
if num1==num2 and num2==num3 and num3==num1:
    print("all are equal")
elif num1==num2 or num2==num3 or num3==num1:
    print("two number are equal")
else:
    print("all are different")

#movie Ticket Discount
age=int(input("enter age :"))
if age<5:
    print("ticket price free")
elif age>=5 and age<=17:
    print("price is 100")
elif age>=18 and age<=59:
    print("price is 200")
else:
    print("price is 120")

ge=int(input("enter age :"))
if age<5:
    print("ticket price free")
elif age>=5 and age<=17:
    print("price is 100")
elif age>=18 and age<=59:
    print("price is 200")
else:
    print("price is 120")

ge=int(input("enter age :"))
if age<5:
    print("ticket price free")
elif age>=5 and age<=17:
    print("price is 100")
elif age>=18 and age<=59:
    print("price is 200")
else:
    print("price is 120")
#same but different but order cannot be different
age=int(input("enter age :"))
if age<5:
    print("ticket price free")
elif age<18:
    print("price is 100")
elif age<60:
    print("price is 200")
else:
    print("price is 120")

#number classification positive even odd and negative even odd and zero
num=int(input("enter a number :"))
if num>0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
elif num<0:
    if num%2==0:
        print("negative even")
    else:
        print("negative odd")
else:
    print("zero")
#same but different
num=int(input("enter a number :"))
if num==0:
    print("zero")
elif num>0 and num%2==0:
    print("positive even")
elif num>0 and num%2!=0:
    print("positive odd")
elif num<0 and num%2==0:
    print("negative even")
else:
    print("negative odd")
