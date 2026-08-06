
year=int(input("Enter a year:"))

# if (year%400 ==0) and (year%100==0):
#     print("%s is leap year" %year)
#
# elif (year %4 ==0) and (year %100 !=0):
#     print("%s is leap year"%year)
# else:
#     print("%s is not a leap year"%year)


if (year%400==0) or (year%4==0) and(year%100!=0):
    print("{} is leap year".format(year))
else:
    print("%s is not a learp year" %year)