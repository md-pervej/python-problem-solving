
my_dic={4:8,3:2,5:6,7:9}

dic_list={key:value for key,value in sorted(my_dic.items(), key=lambda item:item[1])}
print(dic_list)