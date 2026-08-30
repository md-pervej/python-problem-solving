
# -----:81:Python Program to Represent enum-----

from enum import Enum

class Day(Enum):
    MONDAY=1
    THURSDAY=2
    FRIDAY=3

print(Day.MONDAY)
print(Day.THURSDAY.name)
print(Day.FRIDAY.value)