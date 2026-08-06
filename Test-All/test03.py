
year=int(input("Enter a year:"))

# if (year %400)==0:
#     print(f"{year} is leap year")
# elif (year % 4==0 and year % 100 !=0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year}

if (year % 400==0) or (year % 4==0) and (year % 100 !=0):
    print(f"{year} is leap year")
else:
    print("{} is not leap year".format(year))