
my_list=[3,8,6,13,15,18,21]

result = list(filter(lambda x:(x % 3==0),my_list))
print("Numbers divisible by 5 are:",result)