
# -----48:Python Program to Merge Two Dictionaries-----

# Example 1: Using the | Operator
dic1={1:"HTML",2:'CSS'}
dic2={2:'Python', 3:'Java'}
# print(dic1 | dic2)


# -------------------------------
# Example 2: Using the ** Operator
color1={1:'Red',2:'Green'}
color2={2:'Yellow',3:'Black'}
# print({**color1,**color2})

# ------------------------------------
# Example 3: Using copy() and update()
course1={1:'HTML',2:'PHP'}
course2={3:'Python',1:'Java'}

new_course=course2.copy()
new_course.update(course1)
print(new_course)