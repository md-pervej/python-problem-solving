
import os
from pathlib import  Path
file_name=os.path.basename('./myfile.txt')

print(os.path.splitext(file_name)[0])

print(Path('./myfile.txt').stem)
