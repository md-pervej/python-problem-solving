
num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
num3=float(input("Enter num3:"))

# if(num1>num2) and (num1>num3):
#     print("%.1f is largest number" %num1)
# elif (num2>num1) and (num2>num3):
#     print("%.1f is largest number"%num2)
# else:
#     print("%.1f is largest number" %num3)


if num1 == num2 == num3:
    print("All three numbers are equal.")
elif (num1 == num2) and (num1 > num3):
    print("%.1f and %.1f are the largest numbers." % (num1, num2))
elif (num1 == num3) and (num1 > num2):
    print("%.1f and %.1f are the largest numbers." % (num1, num3))
elif (num2 == num3) and (num2 > num1):
    print("%.1f and %.1f are the largest numbers." % (num2, num3))
elif (num1 > num2) and (num1 > num3):
    print("%.1f is the largest number." % num1)
elif (num2 > num1) and (num2 > num3):
    print("%.1f is the largest number." % num2)
else:
    print("%.1f is the largest number." % num3)