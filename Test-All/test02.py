
with open("../Ps-All/data.txt") as f:
    file_content=[line for line in f]

print(file_content)

with open("../Ps-All/data.txt") as f:
    file_content=[line.strip() for line in f]
print(file_content)