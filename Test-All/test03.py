<<<<<<< HEAD
=======

def convertToDecimal(n):
    if n>1:
        convertToDecimal(n//2)
    print(n%2,end='')
num=int(input("Enter a number:"))
convertToDecimal(num)
>>>>>>> 901d4fba66d1079b6bf7696521607988ca342e80
