
# -----87:Python Program to Iterate Through Two Lists in Parallel-----
import itertools
list_1=[1,2,3,4,5]
list_2=['a','b','c','d','e','f']

# for i,j in zip(list_1,list_2):
#     print(i,j)

for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)