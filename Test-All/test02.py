
import re
string="  I am learning Python "

print(string)
print(string.strip())
print(re.sub(r'^\s+|\s$','',string))
