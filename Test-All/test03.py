
from datetime import datetime

my_date_time="Mar 10 2026 12:30PM"

date_time_object=datetime.strptime(my_date_time,'%b %d %Y %I:%M%p')
result=date_time_object.strftime('%d-%b-%Y %I:%M%p')
# print(type(date_time_object))
print(result)