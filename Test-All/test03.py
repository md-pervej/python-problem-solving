
string=input("Enter a string:")

try:
    num=int(input("Enter a num:"))
    print(string+num)
except(TypeError,ValueError) as e:
    print(e)