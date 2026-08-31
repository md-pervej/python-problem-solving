
import os.path, time
import pathlib
file=pathlib.Path('my_file.txt')
print("Last Modification time is : %s"% time.ctime(os.path.getmtime(file)))