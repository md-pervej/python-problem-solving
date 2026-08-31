

import os
from pathlib import  Path

file_stat=os.stat('data.txt')
print(file_stat.st_size)

file=Path('data.txt')
print(file.stat().st_size)