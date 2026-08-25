
# -----69: Python Program to Check If a String Is a Number (Float)-----

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isFloat('12.50'))
print(isFloat('12s'))