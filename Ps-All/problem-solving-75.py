

# -----75:Python Program to Measure the Elapsed Time in Python-----
from timeit import default_timer as timer
# Example 1: Using time module
# start=time.time()
#
# print(23*45)
# time.sleep(2)
# end=time.time()
#
# print(end-start)

# Example 2: Using timeit module
start=timer()
print(33*33*33+25)
end=timer()
print(end-start)



