

import itertools,random

deck = list(itertools.product(range(1,11),['BD','UK','USA','IND']))
random.shuffle(deck)

for i in range(1,10):
    print(deck[i][0],"of",deck[i],[1])
