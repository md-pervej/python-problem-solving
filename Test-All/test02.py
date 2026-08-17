


user_input=input("Enter a word to check vowels:")
vowels='aeiou'
lowercase_text=user_input.casefold()
count_vowels={}.fromkeys(vowels,0)

for char in lowercase_text:
    if char in count_vowels:
        count_vowels[char] +=1
print(count_vowels)

