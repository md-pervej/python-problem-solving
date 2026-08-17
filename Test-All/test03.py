

user_input=input("Enter a word to check vowels:")
lowercase_test=user_input.casefold()
vowels='aeiou'
vowels_count={}.fromkeys(vowels,0)

for char in lowercase_test:
    if char in vowels_count:
        vowels_count[char]+=1
print(vowels_count)

