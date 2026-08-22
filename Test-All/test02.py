
from functools import reduce

my_list=[[1,2],[3,4,5],[6,7,8]]

# flat_list=[]
# for sublist in my_list:
#     for num in sublist:
#         flat_list.append(num)
# print(flat_list)

print(reduce(lambda x,y:x+y,my_list))
