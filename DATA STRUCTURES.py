##DATA STRUCTURES:------->>>>>>>>>>>
"""
1.list:- it is a collection of items in a particular order
*square brackets are used to define a list
*list heterogeneous data types are allowed in a list(list can store different data types together)
*list allows storing duplication value
marks=[80,1,99,80]
*list are orderd-because they have indexing 
and indexing starts from 0.
*list are mutable-> we can change any value anytime and anywhere.
marks[1]=amit # it can change the old value to new value
marks=[] # empty list
marks=[10,20,30,40,50] #list with values"""
# marks=[80,78,90,65,88,87,75,"amit",True,3.14]
# print(marks[3])
# print(marks[1:6])
# marks=[80,78,80,90,"amit",3.14]
# marks[3]="modiji"
# print(marks)

##Traversing:-
"""for i in a:
    print(i)"""

"""
*agar kisi keyword ke aage (.)dot nhi laga that is a function
*agar '.'(dot) laga hai to method hai
"""

#Method in List
#1. *append():- add the value at the last of list
"""marks=[10,20,30,40,50]
marks.append(90)
print(marks)
"""
#2. *extend()
"""marks2=[70,80,90]
marks.extend(marks2)
marks2.extend(marks)
print(marks)
print(marks2)
"""
#3. imsert(index,value)
"""marks.insert(7,90)
print(marks)"""