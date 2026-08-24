
from datetime import datetime
date_string="Mar 10 2026 11:00AM"
my_date_time=datetime.strptime(date_string,'%b %d %Y %I:%M%p')
print(type(my_date_time))
result=my_date_time.strftime('%d %b %Y %I:%M%p')
print(result)