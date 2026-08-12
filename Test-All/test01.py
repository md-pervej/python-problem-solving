
import itertools,random


deck=list(itertools.product(range(1,5),['HTML','CSS','Python','Java']))
dl=random.shuffle(deck)


print("You got:")

for i in range(5):
    print(deck[i][0],"of",deck[i][1])