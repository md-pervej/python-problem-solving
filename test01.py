
num1=1.5
num2=1.6

total=num1 + num2

# print('The sum of {0} and {1} is {2}'.format(num1,num2,total))
# print(f"The sum of {num1} and {num2} is : {total}")
# -------------------------------------------
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

total=float(num1) + float(num2)

print("The sum of {:.1f} and {:.1f} is {:.1f}".format(num1,num2,total))