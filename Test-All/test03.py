
def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isFloat('12s'))
print(isFloat('25.4'))