
my_dic={5:8,6:9,3:2,4:1,9:4}

dic_list={key:value for key,value in sorted(my_dic.items(),key=lambda item:item[1])}
print(dic_list)