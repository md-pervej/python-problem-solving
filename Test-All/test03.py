

punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''

user_input=input("Enter a word to remove punctuation:")

not_punct=""
for char in user_input:
    if char not in punctuations:
        not_punct=not_punct+char
print(not_punct)