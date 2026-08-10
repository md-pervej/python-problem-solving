
num=int(input("Enter a number to calculate sum:"))

if num<0:
    print("Enter a positive number.")
else:
    total=0
    while num>0:
        total+=num
        num-=1
    print("Total is:",total)