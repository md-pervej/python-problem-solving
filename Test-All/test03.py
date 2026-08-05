

celsius=float(input("Enter a celsius value:"))

fahrenheit=(celsius*1.8)+32
print("%.2f degree celcius = %.2f degree fahrenheit" %(celsius,fahrenheit))
print("{:.2f} degree celsius = {:.1f} degree rahrenheit".format(celsius,fahrenheit))
print(f"{celsius:.1f} degree celsius = {fahrenheit:.1f} degree fahrenheit")