
from dateutil import parser

my_date="Mar 10 2026 10:35AM"

date_time=parser.parse(my_date)
result=date_time.strftime("%d %b %Y %I:%M:%p")
print(result)
print(my_date)