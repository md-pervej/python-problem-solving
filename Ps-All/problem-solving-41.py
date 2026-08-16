
# -----41:Python Program to Sort Words in Alphabetic Order-----
user_input=input("Enter a word:")

words=[word.lower() for word in user_input.split()]
words.sort()
for word in words:
    print(word)