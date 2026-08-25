

with open("../Ps-All/data.txt") as file:
    file_content=file.readlines()

# print(file_content)

file_data=[data.strip() for data in file_content]
# print(file_data)

with open("../Ps-All/data.txt") as file:
    file_content=[data for data in file]
print(file_content)

with open("../Ps-All/data.txt") as file:
    file_data=[data.rstrip()  for data in file]
print(file_data)