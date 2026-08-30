

# -----82:Python Program to Return Multiple Values From a Function-----

# Example 1: Return values using comma

def name():
    return "Habibur","Rahman"

print(name())
name1,name2=name()
print(name1,name2)


def course():
    course1="HTML"
    course2="Java"
    return {1:course1,2:course2}

print(course())