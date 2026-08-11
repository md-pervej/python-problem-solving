# -----22: Python Program to Display Powers of 2 Using Anonymous Function-----

num=int(input("How many terms:"))

result=list(map(lambda x:2**x,range(num+1)))
for i in range(num+1):
    print("2 raised power of ",i,"is:",result[i])
