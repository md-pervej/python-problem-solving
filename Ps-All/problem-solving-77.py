
index=[1,2,3,4,5]
course=['HTML','CSS','Java','React','Python']

my_dict=dict(zip(index,course))
print(my_dict)

dic_one={k:v for k,v in zip(index,course)}
print(dic_one)
