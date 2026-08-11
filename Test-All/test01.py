

<<<<<<< HEAD
num=int(input("How many terms: "))

result = list(map(lambda x:2**x,range(num)))
print("The total terms are:",num)
for i in range(num):
    print("2 raised to power is",i,"is",result[i])
=======
my_list = [12, 65, 54, 39, 102, 339, 221,]
result= list(filter(lambda x: (x%13==0),my_list))

print("Numbers divisible by 13 are:",result)
>>>>>>> 3f7224878af0ad5eaf045defe2a23ac4c7d0c558
