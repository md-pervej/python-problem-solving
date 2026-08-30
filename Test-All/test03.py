
import os
import glob
# os.chdir("dirA/dirB/dirC/")
# for file in glob.glob("*.txt"):
#     print(file)

# for file in os.listdir("./dirA/dirB/dirC/"):
#     if file.endswith(".txt"):
#         print(file)

for root,dir,files in os.walk("./dirA/dirB/dirC"):
    for file in files:
        if file.endswith(".txt"):
            print(file)

