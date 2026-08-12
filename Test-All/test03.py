

import itertools,random

deck=itertools.product(range(1,11),['Bangladesh','India','Srilanka','Canada'])
random.shuffle(deck)

print("You got:")
for i in range(1,6):
    print(deck[i][0],"of",deck[i][1])
