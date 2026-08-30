
# -----84:Python Program to Find All File with .txt Extension Present Inside a Directory-----
import os, glob
# Example 1: Using glob
# os.chdir("./files/")
# for file in glob.glob('*.txt'):
#     print(file)

# Example 2: Using os
for file in os.listdir("./files/"):
    if file.endswith('.txt'):
        print(file)

# Using os.walk
for root,files,dirs in os.walk("./files"):
    for file in files:
        if file.endswith('.txt'):
            print(file)
    
    