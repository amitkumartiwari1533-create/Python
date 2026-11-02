#if,else,elif
#question1
a=int(float(input("enter a number (a>0 or a<0):")))
if a>0 or a==0:
      print("postive")
else:
      print("negative")

#question2
a=int(float(input("enter a number ")))
if (a%2)==0:
      print("even")
else:
      print("odd")      

#Questio3
a=int(float(input("enter a 1st number:")))
b=int(float(input("enter a 2nd number:")))
if a>b:
      print(f"{a} is grater then {b}")
else:
      print(f"{a} is less then {b}")   

#Question4
a=int(input("enter a 1st number:"))
b=int(input("enter a 2nd number:"))   
if a==b:
      print(f"{a} and {b} is equal")
else:
      print(f"{a} and {b} is not equal")  

#Question5
marks=int(float(input("enter your marks(marks>40 or marks<40):-")))
if marks>=40:
      print("you are pass")
else:
      print("you are fail")  

#Question6
num=int(float(input("enter a number:")))
if num==0:
      print("zero")
else:
      print("not zero")    

#Question7
age=int(input("enter your age (age<18 or age>=18 or age>=50):"))
if age<18:
      print("Minor")
elif age>=18:
      print("adult")
else:
      print("old age")   

#Question8
num=float(int(input("enter a number:"))) 
if (num%2)==0:
      print("it is divisible by 2")
else:
      print("it is not divisible by 2")      
                
#Question9
temperature=float(int(input("enter your temperature:-")))
if temperature>=30:
      print("Hot Temperature")
else:
      print("Cold Temperature2")      

#Question10
num=float(int(input("enter a number:")))
if num>=10:
      print("Greater")
else:
      print("Smaller")            