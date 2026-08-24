
from datetime import datetime

my_date="10 Mar 2026 11:20AM"

my_date_time=datetime.strptime(my_date,'%d %b %Y %I:%M%p')
print(type(my_date_time))
result=my_date_time.strftime('%d %b %Y %I:%M%p')
print(result)
print(my_date_time)