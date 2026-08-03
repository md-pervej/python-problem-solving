
# -----03:Python Program to Find the Square Root-----
# method-01:    % formatting
# method-02:   .format()
# method-03  f-string

num=float(input("Enter a number:"))

num_sqrt=num ** 0.5

print("The square root of %.0f is %.2f" %(num,num_sqrt))
print("The square root of {:.0f} is {:.2f}" .format(num,num_sqrt))
print(f"The square root of {num:.0f} is {num_sqrt:.2f}")