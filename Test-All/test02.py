

num=int(input("Enter a number:"))
#
# if num<0:
#     print("Sorry, Factorial does not exists for negetive numbers")
# elif num==0:
#     print("Factorial of  0 is 1")
# else:
#     factorial=1
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("Factorial of ",num,"is:",factorial)

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return (x*(factorial(x-1)))

    3*factorial(2)
    2*(factorial(1))
    1*(factorial(1))

result=factorial(num)
print("Factorial ",num,"is:",result)


