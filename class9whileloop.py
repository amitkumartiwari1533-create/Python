"""
While Loop
KAHA SE JANA HAI -> KQH TAK JANA HAI -> KAISE JANA HAI

WHILE JAB TAK YEH CONDITION TRUE HAI:
    TAB TAK YEH CODE CHALAYEGA.
    """

##Question: 1-50 TAK PRINT KARNA HAI 
# i=1
# while i<=50:
#     print(i)
#     i+=1

##Question: 10-1 print karna hai
# i=10
# while i>=1:
#     print(i)
#     i-=1

##Question: user se password input lena hai aur jab tak user sahi password nahi dalta tab tak password input karte rahe
# password="amit"
# while True:
#     user_password=input("Enter your password :")
#     if user_password=="amit123":
#         print("You are logged in")
#         break
#     else:
#         print("Wrong password please try again")

""" WHILE LOOP IS USE FOR REPATE THE CODE UNTIL THE CONDITION IS TRUE. """

# password=""
# while password!="amit123":
#     password=input("Enter your password :")
# print("You are logged in")

##Question: print table of any number 
# n=int(input("Enter a number :"))
# i=1
# while i<=10:
#     print(f"{n} x {i} = {n*i}")
#     i+=1

##Question: print even number from 2 to 20
# i=2
# while i<=20:
#     print(i)
#     i+=2

##Question: print even number from 2 to 20 sum all even number from 2 to 20
# i=2
# sum=0
# while i<=20:
#     sum+=i
#     i+=2     
# print(sum)

##Question: print a number in reverse order example:- 1234 -> 4321
"""
%-> last digit ko print karta hai
//-> last digit ko remove karta hai
"""
# n=1234
# while n!=0:
#     print(n%10,end=" ")
#     n=n//10

# n=int(input("enter a number :"))
# a=0
# while n>0:
#     last=n%10
#     count+=1
#     a=a*10+last
#     n=n//10
#print(a)
#print(count)

##Question: count the number of digits in a number
n=int(input("enter a number :"))
count=0
while n>0:
    n=n//10
    count+=1
print(count)