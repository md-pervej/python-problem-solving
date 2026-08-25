

with open("../Ps-All/data.txt") as f:
    file_content=f.readlines()
print(file_content)

file_content=[x.strip() for x in file_content]
print(file_content)