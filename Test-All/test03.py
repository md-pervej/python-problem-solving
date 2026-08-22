
dic={5:4,2:8,3:4,1:2}

sorted_dic={key:value for key,value in sorted(dic.items(),key=lambda item:item[1])}

print(sorted_dic)