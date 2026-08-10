
num=int(input("Enter a numbet to sum:"))

if num<0:
    print("Pls. Enter a positive number.")
else:
    sum=0
    while num>0:
        sum+=num
        num -=1
    print("The sum is",sum)

