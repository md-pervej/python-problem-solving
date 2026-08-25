

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(isFloat('12.s'))
print(isFloat('12.5'))