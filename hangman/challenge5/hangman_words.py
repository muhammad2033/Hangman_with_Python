import random
import string

# Generate a list of 1000 random words
num_words = 1000
chosen_word = []

for i in range(num_words):
    # Generate a random word between 4 and 10 characters long
    word = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 10)))
    chosen_word.append(word)
# print(chosen_word)    

# chosen_words = random.choice(chosen_word)
# print(chosen_words)