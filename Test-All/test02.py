
import os
from pathlib import Path
file_name=os.path.basename('../Ps-All/data.txt')
print(os.path.splitext(file_name)[0])

print(Path('./file2.txt').stem)




