
num=int(input("Enter a number:"))

factor_list=[]
def find_factors(x):
    for i in range(1,x+1):
        if x%i==0:
            factor_list.append(i)
find_factors(num)
print("The factor of ",num,"are:",",".join(map(str,factor_list)))
