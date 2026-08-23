

string=input("Enter string")
try:
    num=int(input("Enter numb er"))
    print(string + num)
except(TypeError,ValueError) as e:
    print(e)


