

base=int(input("Enter a Base:"))
exponent=int(input("Enter a exponent:"))

result=1

while exponent !=0:
    result *=base
    exponent -=1
print("Answer is: "+ str(result))