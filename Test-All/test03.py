
import os,pathlib,time

file=pathlib.Path('my_file.txt')
print("Last MOdifcation time is: %s" % time.ctime(os.path.getmtime(file)))
print("Metadata change time or path creation tiem: %s" % time.ctime(os.path.getctime(file)))