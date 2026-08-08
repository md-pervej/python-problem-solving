
num=int(input("Enter a number:"))

# if num<0:
#     print("sorry,Factorial does not exists for negativ enumber")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     factorial=1
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("Factorial of",num,factorial)

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return (x*factorial(x-1))
result=factorial(num)
print("Factorial 0f",num,"is:",result)
