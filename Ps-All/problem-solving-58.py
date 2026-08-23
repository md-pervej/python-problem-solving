

# -----58:Python Program to Concatenate Two Lists-----
list1=[1,'a']
list2=[1,2,3,4,5]

# joined_list=list1 + list2

# print(joined_list)

# joined_list=[*list1,*list2]
# print(joined_list)

# joined_list=list(set(list1+list12))
# print(joined_list)

list2.extend(list1)
print(list2)