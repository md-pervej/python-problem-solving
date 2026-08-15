
def recur_num(n):
    if n<=1:
        return n
    else:
        return n + recur_num(n-1)

num=int(input("Enter a number:"))

if num<1:
    print("Enter a positive number:")
else:
    print("The sum is: ",recur_num(num))