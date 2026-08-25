
import os
import pathlib
file_details=os.path.splitext('file2.txt')
# print(file_details)
# print(file_details[1])

file_details=pathlib.Path('file2.txt').suffix
print(file_details)