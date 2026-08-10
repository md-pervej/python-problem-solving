
num=int(input("How many terms:"))
result=list(map(lambda x:2**x,range(num+1)))
for i in range(num+1):
    print("2 raisef of power",i,"is:",result[i])