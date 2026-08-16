
# ------:35 Python Program to Convert Decimal to Binary Using Recursion-----

def convertToDecimal(n):
    if n>1:
        convertToDecimal(n//2)
    print(n%2,end='')
num=int(input("Enter a number:"))

convertToDecimal(num)



