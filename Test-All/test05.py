

num1=int(input("Enter number-1:"))
num2=int(input("Enter number-2:"))

def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

result=compute_hcf(num1,num2)
print("The H.C.F  between",num1,"and",num2,"is:",result)