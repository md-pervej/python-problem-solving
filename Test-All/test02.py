
import os,pathlib
import time

file=pathlib.Path('my_file.txt')
print("Last Modification date is: %s" % time.ctime(os.path.getmtime(file)))
print("Last medata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))
