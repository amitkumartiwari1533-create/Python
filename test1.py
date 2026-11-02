"""QUESTION1:-Check palindrome number (10 marks)

        Take an integer N as input and check whether              the number remains the same when its digits               are reversed.

      Example:
      Input: 121

      Output : Palindrome"""
a=int(input("tell the number:-"))
rev=0
copy=a
while a!=0:
    rev=rev*10+a%10
    a=a//10
if copy==rev:
    print("palindrome")
else:
    print("not palindrome")


"""Question2:- Given a non-negative integer, check whether it is an Armstrong number. Raise each digit to the power equal to the number of digits, then check whether the sum equals the original number.

**Example:** Input: 153 → Output: Armstrong Number (1³ + 5³ + 3³ = 153)"""
n=153
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


"""Question3. **Second Largest Digit (10 marks)**
    
    Take an integer N as input and find the second largest distinct digits present in the number.
    
    Example: Input: 58382
    
    Output: Second Largest: 5
    
     Check Palindrome Number"""

# n=int(input("tell the number"))
# largest=0
# second_largest=0
# while n>0:
#     digit=n%10
#     n=n//10

#     if digit>largest:
#         second_largest=largest
#         largest=digit
#     elif digit>second_largest and digit!=largest:
#         second_largest=digit
# print("second_digit")




"""Question4. **Prime Numbers from 1 to N (10 marks)**
    
    Take a positive integer N as input and print all prime numbers from 1 to N (inclusive). 
    
    Note: 1 is not a prime number.
    
    **Example:** Input: 10 → Output: 2, 3, 5, 7"""


n = int(input("Enter a positive integer: "))

print("Prime numbers from 1 to", n, "are:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")



