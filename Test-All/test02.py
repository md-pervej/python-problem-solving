
year=int(input("Enter a year:"))


# if (year %400 ==0) and (year %100==0):
#     print("{0} is leap year")
# elif (year %4==0) and (year% 100 !=0):
#     print("{0} is leap year".format(year))
# else:
#     print("{0} is not leap year".format(year))

if(year %400 ==0) or (year %4==0 and year % 100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
