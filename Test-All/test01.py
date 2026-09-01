
base=int(input("Enter base: "))
exponent=int(input("Enter exponent: "))

result=1

while exponent !=0:
    result *=base
    exponent -=1

print("Answer=: "+ str(result))

