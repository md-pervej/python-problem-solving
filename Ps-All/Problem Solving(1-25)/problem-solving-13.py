# -----13:Python Program to Find the Largest Among Three Numbers-----

num1=float(input("Enter number-1:"))
num2=float(input("Enter number-2:"))
num3=float(input("Enter number-3:"))

if num1==num2==num3:
    print("All numbers are equal.")
elif num1==num2 and num1>num3:
    print(f"{num1:.0f} and {num2:.0f} are the greatest number.")
elif num1==num3 and num1>num2:
    print(f"{num1:.0f} and {num:.0f} are the greatest numb er")
elif num2==num3 and num2>num1:
    print(f"{num2:.0f} and {num3:.0f} are the greatest number.")
elif num1>num2 and num1>num3:
    print(f"{num1:.of} is the greatest number")
elif num2>num1 and num2>num3:
    print(f"{num2:.0f} is the greatest number.")
else:
    print(f"{num3:.0f} is the greatest number.")