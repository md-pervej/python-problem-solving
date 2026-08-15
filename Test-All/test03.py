

num=int(input("Enter a number:"))

def recur_factorial(n):
    if n==1:
        return n
    else:
        return n* recur_factorial(n-1)

if num<0:
    print("Factorial does not exists for negative integer")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("The factorail of ",recur_factorial(num))
