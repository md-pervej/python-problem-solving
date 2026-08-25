

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isFloat('15a'))
print(isFloat('10.50'))
