
# -----83:Python Program to Get Line Count of a File-----
# Example 1: Using a for loop
def line_count(fname):
    with open(fname)as file:
        for i,l in enumerate(file):
            pass
    return i+1
print(line_count('data.txt'))

# Example 2: Using list comprehension

num_lines=sum( 1 for l in open('data.txt'))
print(num_lines)