# -----:90Python Program to Compute the Power of a Number-----
# Example 1: Calculate power of a number using a while loop
# base=int(input("Enter a base:"))
# exponent=int(input("Enter a exponent:"))
# result=1
#
# while exponent !=0:
#     result *=base
#     exponent -=1
# print("Answer is :",result)

# base=int(input("Enter Base:"))
# exponent=int(input("Enter exponent:"))
# result=1
#
# for exponent in range(exponent,0,-1):
#     result *=base
# print("Answer is :",result)

base=int(input("Enter a base:"))
exponent=int(input("Enter a exponent:"))

result=pow(base,exponent)
print("Answer is:",result)



