# num=int(input("Enter a number:"))
#
# if num<0:
#     print("Sorry factorial does not exists for negative numbers")
# elif num==0:
#     print("The factorial of 0 is 1")
# else:
#     factorial=1
#     # 1,2,3
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("Factorial of",num,"is:",factorial)


def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return (x*(factorial(x-1)))

num=int(input("Enter a number:"))
result =factorial(num)
print("Factorial of ",num,"is:",result)