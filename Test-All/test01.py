

num=int(input("Enter a number:"))

if num<0:
    print("Sorry factorial does not exists for negative numbers")
elif num==0:
    print("The factorial of 0 ia 1")
else:
    factorial=1
    for i in range(1,num+1):
        factorial =factorial*i
    print("The factorila of ",num, "is",factorial)
