

user_str=input("Enter a word to check palindrom:")

case_str=user_str.casefold()
rev_str=reversed(case_str)

if list(user_str)==list(rev_str):
    print(user_str+" is palindrome")
else:
    print(user_str+" is not palimdrome")
