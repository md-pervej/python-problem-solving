
# -----50:Python Program to Access Index of a List Using for Loop-----
courses=['HTML','CSS','Java','Python','SQL']

# for index,course in enumerate(courses):
#     print(index,course)

# for index,course in enumerate(courses,start=1):
    # print(index,course)

for index in range(len(courses)):

    value=courses[index]
    print(index,value)

