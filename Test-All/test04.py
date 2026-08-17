

user_input=input("Enter a word to check vowsl:")

lowercase_text=user_input.casefold()
vowels='aioue'
vowels_count={}.fromkeys(vowels,0)

for char in lowercase_text:
    if char in vowels_count:
        vowels_count[char]+=1
print(vowels_count)
