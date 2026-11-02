##Question: Write a python program to count the number of factors of a given number.
# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print(f"Number of factors of {n} is {count}")

##Question: Check whether a given number is prime or not.
# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#n=int(input("Enter a number :"))
##1and number itself is always a factor of the number so we can start from 2 to n-1
# for i in range(2,n):
#     if n%i==0:
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is a prime number") 

##Question
# name="AbhiSHEK"
# upper=0
# lower=0
# for i in name:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
# print(f"Upper case letters are {upper} and lower case letters are {lower}") 