##PARAMETERS AND ARGUMENTS
#TYPES OF PARAMETERS and ARGUMENTS
#1. Default parameters:- if you provide the default value to the parameter then it is called default parameter
# def hello(a,b=10): #b is default parameter
#     print(a+b)  
# hello(50,50) #here we are providing the value to the default parameter

#1.1.DEFAULT ARGUMENTS:- if you provide the value to the default parameter then it is called default argument
# def information(name,age,number):
#     print("hello your info is ")
#     print(name)
#     print(age)
#     print(number)
# information(number=1234567890,name="sachin",age=20) #here we are providing the value to the default parameter
# information("amit",20,"MP2025SDIA3420748")

"""print number from 1 to 30
you cannot use the for and while loop
you cannot uses print satatement more than 1 time"""


#recursion:- when a function calls itself then it is called recursion
# def number(n):
#     if n==12:
#         return "hello bhai"
#     print(n)
#     number(n+1)
# number(1)

# def hello1():
#     hello2()
#     print('hello1')

# def hello2():
#     hello3()
#     print('hello2')

# def hello3():
#     hello4()
#     print('hello3')

# def hello4():
#     print('hello4')
# hello1()

def number(n):
    if n==31:
        return
    number(n+1)
    print(n)
number(1)

def number(n):
    if n==31:
        return
    print(n)
    number(n+1)
    
number(1)









