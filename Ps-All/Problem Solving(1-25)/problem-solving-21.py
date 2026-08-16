# -----21: Python Program to Find the Sum of Natural Numbers-----

num=int(input("Enter a number:"))

if num<0:
    print("Enter a positive number:")
else:
    while num>0:
        total=0
        total+=num
        num-=1
print("Total is:",total)















