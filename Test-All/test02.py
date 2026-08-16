

user_input=input("Enter a word to check palindrome:")
case_user_input=user_input.casefold()
rev_str=reversed(case_user_input)
if list(case_user_input)==list(rev_str):
    print(case_user_input+" is a plindrome")
else:
    print(case_user_input+" is not palindrome")