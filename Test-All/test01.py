
from functools import  reduce
my_list=[[1,2],[3,4],[5,6],[7,8,]]

# flat_list=[]
# for subList in my_list:
#     for num in subList:
#         flat_list.append(num)
# print(flat_list)

# flat_ist=sum(my_list,[])
# print(flat_ist)

print(reduce(lambda x,y:x+y,my_list))

