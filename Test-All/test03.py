
year=int(input("Ente a year:"))

if year %400==0 or year % 4==0 and year % 100 !=0:
    print(f"{year} is leap hear")
else:
    print(f"{year} is not leap year")