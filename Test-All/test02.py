my_list=[5,6,10,13,15,17,20]

<<<<<<< HEAD

num=int(input("How many terms:"))

result = list(map(lambda x:2**x,range(num)))
for i in range(num):
    print("2 raised to power is:",i,"is",result[i])
=======
result=list(filter(lambda x:x%5==0,my_list))
print("Number divisible by 5 are:",result)
>>>>>>> 3f7224878af0ad5eaf045defe2a23ac4c7d0c558
