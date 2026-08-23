

def split(list,chunk_size):
    for i in range(0, len(list),chunk_size):
        yield list[i:i + chunk_size]



chunk_size=2
my_list=[1,2,3,4,5,6,7,8]
print(list(split(my_list,chunk_size)))