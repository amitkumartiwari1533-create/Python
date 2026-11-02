##Question 1: Write a python program to check whether a number is palindrome or not.
a=121
rev=0
copy=a
while a!=0:
    rev=rev*10+a%10
    a=a//10
if copy==rev:
    print("palindrome")
else:
    print("not palindrome")

"""function
how function are created"""
##inbult function:-



##user defined function:- user can create their own function
##defining a function
# def hello():
#     print("hello world")
##calling a function
# hello()

##return
# def hey():
#     return "hello bhai" """return the value to the function"""
# a=hey() """calling block captures the value returned by the function"""
# print()



##PARAMETERS AND ARGUMENTS
# def addtion(a,b): #you accept the parameters
#     print(a+b)
# addtion(10,20) #and you provide the arguments to the parameters
# addtion(100,200)

# def palindrome(a):
#     rev=0
#     copy=a
#     while a!=0:
#         rev=rev*10+a%10
#         a=a//10
#     if copy==rev:
#         print(copy)

# for i in range(1,1000):
#     palindrome(i)

