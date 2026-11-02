##Question: Number is Armstrong or not.
# n=123
# sum=0
# temp=n
# while n>0:
#     last=n%10
#     sum=sum+last**3
#     n=n//10
# if sum==temp:
#     print("arstrong")
# else:
#     print("not arstrong")

n=13457
length=len(str(n))
sum=0
temp=n
while n>0:
    last=n%10
    sum=sum+last**length
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")


