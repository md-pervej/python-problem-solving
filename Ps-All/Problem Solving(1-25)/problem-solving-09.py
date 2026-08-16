# --------09:Python Program to Convert Celsius To Fahrenheit---------

celsius=float(input("Enter a value in celsius:"))

fahrenheit=(celsius*1.8)+32

print("%.1f degree celsius = %.1f degree fahrenheit" %(celsius,fahrenheit))
print("{:.1f} degree celsius = {:.1f} degree fahrenheit".format(celsius,fahrenheit))
print(f"{celsius:.1f} degree celsius = {fahrenheit:.1f} degree fahrenheit")
