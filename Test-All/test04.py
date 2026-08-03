
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print("The area of the triangle is: %.2f" %area)
print("The area of the triangle is : {:.2f}".format(area))
print(f"The area of the triangle is {area:.2f}")