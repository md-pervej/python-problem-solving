


num=int(input("Enter a number:"))

def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
        521
    print(n%2, end='')


convertToBinary(num)