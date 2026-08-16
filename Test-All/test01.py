
# define punctuation
punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
user_str=input("Enter a string to remove punctuation:")
no_punct=""

for char in user_str:
    if char not in punctuations:
        no_punct=no_punct+char
print(no_punct)
