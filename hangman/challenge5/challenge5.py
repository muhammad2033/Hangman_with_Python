# step 5

import random
# todo-1 update the word list to use the word_list
# from hangman_words.py

# delete this line :word_list =["ardvark","baboon","camel"]

# import hangman_words
# chosen_words = random.choice(hangman_words.chosen_word)

                # or 

from hangman_words import chosen_word

chosen_words = random.choice(chosen_word)
word_length = len(chosen_words)
end_of_game = False

lives = 0

# todo-3  import the logo from hangman_art.py print it at the start of the game

from hangman_art import logo , stages
print(logo)

# testing code
print(f"pssst, the solution is {chosen_words}")

# create blanks
    
display = []
for position in range(word_length):
    display +="_"

print(display)

while not end_of_game:
    guess =input("guess a letter:").lower()
    # print(guess)
    


    # todo-4 if the user has entered a letter they have already 
    # guessed , print the letter and let them know  
    if guess in display:
        print(f"you have already guessed: {guess}")


    # check guessed letter 

    for position in range(word_length):
        letter = chosen_words[position]
        # print(f"current position:{position}\n current letter: {letter}\n guessed letter {guess }")
        if letter == guess:
            display[position] = letter

    print(display)

    # check if user is wrong 

    if guess not in chosen_words:
    # todo-5 if the letter is not in the chosen_word , 
    # print out the letter and let them know it's not in the word 
        print(f"you guessed {guess}.that's not in the word .you lose a life")

        lives += 1 
        if lives ==6:
            print("You lost")
            end_of_game = True

    print(f"{''.join(display)}")  

    # check if user has got all letters 
    if "_" not in display:
        end_of_game = True
        print("you win!")
# todo-2 import the stages from hangman_art.py and make this error go away 

    print(stages[lives])