

num=int(input("How many terms:"))

result = list(map(lambda x:2**x,range(num)))
for i in range(num):
    print("2 raised to power is:",i,"is",result[i])