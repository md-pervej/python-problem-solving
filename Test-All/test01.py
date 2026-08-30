
from enum import Enum


class Day(Enum):
    Monday=1
    Tuesday=2
    Wednesday=3

print(Day.Monday)
print(Day.Tuesday.name)
print(Day.Monday.value)


