# step 4

import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
end_of_game = False
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)

word_length = len(word_list)

# todo-1  create  a variable  called 'lives '  to keep track of the number of lives left
# set 'lives' to equal 6. 
lives = 0

# testing code
print(f"pssst, the solution is {chosen_word}")

# create blanks
    
display = []
word_length =len(chosen_word)
for position in range(word_length):
    display +="_"

print(display)

while not end_of_game:
    guess =input("guess a letter:").lower()

    # print(guess)

    # check guessed letter 

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"current position:{position}\n current letter: {letter}\n guessed letter {guess }")
        if letter == guess:
            display[position] = letter

    print(display)

# todo-2  if guess is not a letter in the chosen_word, then reduce 'lives by 1
# if lives goes down to 0 then the game should stop and it should print "you lose"
# join all the elements in the list and turn it into a string .
    if guess not in chosen_word:
        lives += 1
        if lives ==6:
            print("You lost")
            end_of_game = True

    print(f"{''.join(display)}")  

    # check if user has got all letters 
    if "_" not in display:
        end_of_game = True
        print("you win!")

# todo-3  print the ASCII art from 'stages' that corresponds to the 
# current number of 'lives' the user has remaining    
    print(stages[lives])