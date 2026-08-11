
<<<<<<< HEAD

num=int(input("How many terms:"))
result = list(map(lambda x:2**x,range(num)))
for i in range(num):
    print("2 raised to power: ",i,"is:",result[i])
=======
my_list=[2,6,10,15,20,36]

result=list(filter(lambda x: (x % 2==0),my_list))
print("Numbers divisible by 2 are:",result)
>>>>>>> 3f7224878af0ad5eaf045defe2a23ac4c7d0c558
