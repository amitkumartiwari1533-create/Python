##TUPLE
"""
1.ANNOTED BY (PARANTHESIS).
2.TUPLES ARE ORDERED.
3.TUPLES ARE IMMUTABLE.
4.TUPLES CAN STORE DUPLICATION VALUES.
5.HETROGENOUS-> CAN STORE MIXED TYPE OF DATA.
"""
#T=() #empty tuple
# t=(1,2,3,4)
# print(t)


"""
METHODS IN TUPLE
#1. .index() -> return index of any value
# 2. .count() -> count occurence of any value
"""
# t=(1,1,2,2,3,1)
# print(t.count(1))


"""
OPERATIONS:-

+ -> Concatenation
* -> Repetition
"""
# t1=(1,2)
# t2=(3,4)
# print(t1+t2)
# print(t1*5)

# t=(1,2,[3,4,5])
# t[2][2]=100
# print(t)

# t=(1,2,[3,4,5])
# t[2].append(100)
# print(t)

# t=(1,2,3,4,5)
# for i in range(len(t)):
#     print(i,t[i])

# t=((1,2),(3,4))
# print(t[1][0])

# t=(1,2,3,4,5,6,7,8)
# print(t[1:6])

# t=(1,2,3,4,5,6,7,8)
# t=tuple(reversed(t))
# print(t)

# t=(1,2,3,4,5,6,7,8)
# print(t[::-1])

#print((1,2))