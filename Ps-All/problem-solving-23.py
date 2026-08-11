
# -----23: Python Program to Find Numbers Divisible by Another Number-----
my_list=[5,8,10,15,17,19,20]

result = list(filter(lambda x:(x % 5==0),my_list))

print("Numbers divisible by 5 are:",result)