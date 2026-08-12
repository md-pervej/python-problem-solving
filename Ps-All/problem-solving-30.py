
# -----30:Python Program to Shuffle Deck of Cards-----
import itertools,random

deck=list(itertools.product(range(1,10),['Bangladesh','USA','UK','Russia','Chaian']))
random.shuffle(deck)

print("You got:")
for i  in range(1,11):
    print(deck[i][0],"of",deck[i][1])
