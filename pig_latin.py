# Get sentence from user

original = input("What sentence would you like to convert?: ").lower().strip()

# Split sentence into individual words

words = original.split()
print(words)

# Loop through words and convert to pig latin 

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        consonants = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + consonants + "ay"
        new_words.append(new_word)

# Stick words back together

output = (" ".join(new_words))

# Output final string

print(output)