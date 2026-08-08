
num=int(input("Enter a numbe:"))

<<<<<<< HEAD
flag=False

if num==0 or num==1:
    print(num, "is not prime number.")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
    if flag:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")
=======
lower=int(input("Enter a lower number:"))
upper=int(input("enter upper number:"))

print("prime numbers between ",lower,"and",upper,"are:")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
>>>>>>> 01c82e7ecdff19f17785e15132af6fbd34537673
