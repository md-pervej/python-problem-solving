

with open("../Ps-All/data.txt") as file:
    file_content=[ data for data in file]

print(file_content)

with open("../Ps-All/data.txt") as file:
    file_data=[data.rstrip() for data in file]
print(file_data)