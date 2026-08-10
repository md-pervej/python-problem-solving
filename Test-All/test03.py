
my_list=[2,6,10,15,20,36]

result=list(filter(lambda x: (x % 2==0),my_list))
print("Numbers divisible by 2 are:",result)