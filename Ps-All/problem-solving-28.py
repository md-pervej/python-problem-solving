# -----:28.Python Program to Find the Factors of a Number-----

num=int(input("Enter a number:"))
factors_list=[]
def find_factors(x):
    for i in range(1, x+1):
        if x%i==0:
            factors_list.append(i)
find_factors(num)

print("Factors of ",num,"are:"," ".join(map(str,factors_list)))
