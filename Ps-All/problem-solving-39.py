

-----39:Python Program to Check Whether a String is Palindrome or Not-----
user_input=input("Enter a word to check palindrome: ")
normalized_word=user_input.casefold()
reversed_word=reversed(normalized_word)


if list(normalized_word) == list(reversed_word):
    print(normalized_word+" is palindrome.")
else:
    print(normalized_word+"is not palindrome.")