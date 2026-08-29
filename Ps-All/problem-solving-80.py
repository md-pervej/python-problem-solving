

# -----80:Python Program to Get the File Name From the File Path-----
# Example 1: Using os module
import os
file_name=os.path.basename('../Ps-All/data.txt')

print(os.path.splitext(file_name)[0])

# Example 2: Using Path module

from pathlib import Path
print(Path('./file2.txt').stem)