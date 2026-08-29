
import re
# -----79:Python Program to Trim Whitespace From a String-----

# Example 1: Using strip()
string=" I love python "

print(string)
print(string.strip())

# Example 2: Using regular expression

print(re.sub(r'^\s+|\s+$','',string))
