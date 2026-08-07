

lower=int(input("Enter a lower:"))
upper=int(input("Enter a upper:"))
prime_list=[]
flag=False
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_list.append(num)
            flag=True
if flag:
    print("Prime numbers between", lower, "and", upper, "are:",",".join(map(str,prime_list)))
else:
    print("There are no prime numbers between",lower,"and",upper)
