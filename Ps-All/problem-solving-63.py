
# -----63:Python Program to Convert String to Datetime-----
# Example 1: Using datetime module
# from datetime import datetime
#
# my_date="Mar 10 2026 11:35AM"
#
# my_date_time=datetime.strptime(my_date,'%b %d %Y %I:%M%p')
# print(type(my_date_time))
# result=my_date_time.strftime('%d-%b-%Y %I:%M%p')
# print(my_date_time)
# print(result)


# Example 2: Using dateutil module
from dateutil import parser
my_date=parser.parse("Mar 15 2026 10:20AM")
result = my_date.strftime("%d %b %Y %I:%M%p")
print(result)
print(my_date)