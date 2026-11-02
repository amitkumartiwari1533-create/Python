# #Question1:-
# arr=[1,2,4,5]
# n=len(arr)
# og_n=n+1
# og_sum=((og_n)*(og_n+1))//2
# real_sum=0
# for elem in arr:
#     real_sum+=elem
# missing=og_sum-real_sum
# print(missing)

##Question2:-assending order List
# arr=[10,30,20,40,50]
# is_sorted=True
# for i in range(0,n-1):
#     if arr[i]>arr[i+1]:
#         is_shorted=False
#         break
# if is_shorted:
#     print("list is shorted")
# else:
#     print("list is un sorted")

##Question3:-Palindromic List
# arr=[2,3,15,15,3,2]
# n=len(arr)
# is_palindrome=True
# for i in range(n//2):
#     if arr[i]!=arr[n-1-i]:
#         is_palindrome=False
#         break
# if is_palindrome:
#     print("list is palindrome")
# else:
#     print("list is not palindrome")