
base=int(input("Enter base:"))
# 2
exponent=int(input("Enter exponent:"))
# 3
result=1
# 4
for exponent in range(exponent,0,-1):
     result *=base

print("Answer is: "+ str(result))