

# -----54:Python Program to Sort a Dictionary by Value-----
my_dic = {5:4, 1:6, 6:3}

sorted_dic={key:value for key,value in sorted(my_dic.items(), key=lambda item:item[1])}
print(sorted_dic)