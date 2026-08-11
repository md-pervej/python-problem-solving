

num1=int(input("Enter number-1:"))
num2=int(input("Enter number-2:"))

def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y

    while(True):
        if((greater % x==0) and (greater %y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
result=compute_lcm(num1,num2)
print("The L.C.M of ",num1,"and",num2,"is:",result)
