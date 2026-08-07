
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))


if num1==num2==num3:
    print("All three numbers are equal")
elif num1==num2 and num1>num3:
    print(f"{num1} and {num2} are the greatest number")
elif num1==num3 and num1>num2:
    print(f"{num1} and {num3} are the greatest number")
elif num2==num3 and num2>num1:
    print(f"{num2} and {num3} are the greatest number")
elif num1>num2 and num1>num3:
    print(f"{num1:.0f} is the greatest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest number")
else:
    print(f"{num3} are the greatest number")

