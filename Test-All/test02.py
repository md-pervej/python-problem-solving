

import itertools,random
deck=list(itertools.product(range(1,8),['HTML','CSS','Java','Python']))
print(deck)

random.shuffle(deck)

print("You got:")
for i in range(1,10):
    print(deck[i][0],"of",deck[i][1])
