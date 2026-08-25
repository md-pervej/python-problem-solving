
# -----74: Python Program to Extract Extension From the File Name-----

import os
import pathlib
file_details=os.path.splitext('data.txt')
print(file_details)
print(file_details[1])
file_details=pathlib.Path('data.txt').suffix
print(file_details)
