
lower=int(input("Enter a lower number:"))
upper=int(input("enter a upper number:"))

armstrong_list=[]
for num in range(lower,upper+1):
    total=0
    order=len(str(num))
    temp=num
    while temp>0:
        digit=temp %10
        total+=digit**order
        temp//=10
    if num==total:
        armstrong_list.append(num)
print("From",lower,"to",upper,"armstrong number is:"," ".join(map(str,armstrong_list)))
