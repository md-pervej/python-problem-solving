

import os
from pathlib import Path
file_size=os.stat('my_file.txt')
print(file_size.st_size)

file=Path('my_file.txt')
print(file.stat().st_size)


