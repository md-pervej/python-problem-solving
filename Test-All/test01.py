

<<<<<<< HEAD
X=[[12,7,3],
    [4,5,6],
   [7,8,9]]

Y=[[5,8,1],
    [6,7,3],
    [4,5,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

for r in result:
    print(r)
=======

num=int(input("Enter a number:"))

def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
        521
    print(n%2, end='')

>>>>>>> 9b6d6fe76ca31194474b326654752e274d5c22fb

