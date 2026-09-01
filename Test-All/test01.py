
num=int(input("Enter a number to count digit:"))

count=0

while num !=0:
    num //=10
    count +=1
print("Numbers of digit is:",count)