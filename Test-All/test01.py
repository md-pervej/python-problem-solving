import re
string="  I love Python"

print(string)
# print(string)
# print(string.strip())

print(re.sub(r'^\s+|\s+$','',string))