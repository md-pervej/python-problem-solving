
num1=float(input("Enter number-1:"))
num2=float(input("Enter number-2:"))
num3=float(input("Enter number-3:"))

if num1==num2==num3:
    print("All theree numbers are equal.")
elif num1==num2 and num1>num3:
    print("%.0f and %.0f are the largest number" %(num1,num2))
elif num1==num3 and num1>num2:
    print("%.0f and %.0f are the largest number" %(num1,num3))
elif num2==num3 and num2>num1:
    print("%.0f and %.0f are the greatest number" %(num2,num3))
elif num1>num2 and num1>num3:
    print("%.0f is the largest number" %num1)
elif num2>num1 and num2>num3:
    print("%.0f is the largest number" %num2)
else:
    print("%.0f is the largest number"%num3)
