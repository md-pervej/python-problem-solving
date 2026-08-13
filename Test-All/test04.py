
def recur_fibo(n):
    if n<=1:
        return
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))



num=int(input("Enter a number:"))

if num<=0:
    print("Enter a positive number:")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(recur_fibo(i))