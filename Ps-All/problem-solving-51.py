import itertools
# -----51:Python Program to Flatten a Nested List-----

# Example 1: Using List Comprehension
my_list=[[1,2],[3,4],[5,6,7],[8,9,10]]
# flat_list=[num for sublist in my_list for num in sublist]
# print(flat_list)


# Example 2: Using Nested for Loops (non pythonic way)
flat_list=[]
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)
print(flat_list)

# Example 3: Using itertools package

flat_list=list(itertools.chain(*my_list))
print(flat_list)