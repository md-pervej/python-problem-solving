
# -----47------
# 1:Example 1: Program to print half pyramid using -----
# rows=int(input("Enter a number:"))

# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# Example 2: Program to print half pyramid a using numbers
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# rows=int(input("Enter a number:"))
# ascii_value=int(input("Enter a number :"))

# Example 3: Program to print half pyramid using alphabets
# for i in range(rows):
#     for j in range(i+1):
#         alphabet=chr(ascii_value)
#         print(alphabet,end=" ")
#     ascii_value+=1
#     print()


# Example 5: Inverted half pyramid using numbers
rows=int(input("Enter a number:"))

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()