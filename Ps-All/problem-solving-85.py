
# -----85:Python Program to Get File Creation and Modification Date-----
import pathlib,os,time
file=pathlib.Path('data.txt')

print("Modification time is : %s" % time.ctime(os.path.getmtime(file)))
print("Medata change time is : %s" % time.ctime(os.path.getctime(file)))
