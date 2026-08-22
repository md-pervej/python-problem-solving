
dic={1:4,2:3,3:8,4:1}

sorted_dic={key:value for key,value in sorted(dic.items(), key=lambda item:item[1])}
print(sorted_dic)