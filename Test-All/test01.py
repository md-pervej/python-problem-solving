
vowels='aeiou'

user_input=input("Enter a sentence to check vowel:")

lowercase_text=user_input.casefold()
vowels_count={}.fromkeys(vowels,0)

for char in lowercase_text:
    if char in vowels_count:
        vowels_count[char]+=1
print(vowels_count)