

def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
        # 5,2,1

    print(n%2,end='')
    1010


num=int(input("Enter a number: "))

convertToBinary(num)