
# define punctuation
punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''

user_input=input("Enter a word with punctuation: ")
remove_punct=""
for char in user_input:
    if char not in punctuations:
        remove_punct=remove_punct+char
print(remove_punct)