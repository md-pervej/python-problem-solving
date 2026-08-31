
import itertools
list_1=[1,2,3,4,5,6]
list_2=['a','b','c','d','e']

for i,j in zip(list_1,list_2):
    pass
    # print(i,j)

for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)