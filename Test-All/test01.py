

user_input=input("Enter a word: ")

words=[word.lower() for word in user_input.split()]

words.sort()
print("The sorted words are:")
for word in words:
    print(word)