

import glob,os
# os.chdir('Test-All')

for file in glob.glob("*.txt"):
    print(file)
print(os.getcwd())