
# -----43:Python Program to Count the Number of Each Vowel-----
user_input=input("Enter a word to check vowels:")
lowercase_text=user_input.casefold()

vowels='aioeu'
vowels_count={}.fromkeys(vowels,0)
for char in lowercase_text:
    if char in vowels_count:
        vowels_count[char]+=1
print(vowels_count)
