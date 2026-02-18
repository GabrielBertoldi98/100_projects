import random

stages = [''' 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
''', ''' 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========
''', ''' 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========
''', ''' 
    +---+
    |   |
    O   |
    |\  |
        |
        |
===========
''', ''' 
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
''', ''' 
    +---+
    |   |
    O   |
        |
        |
        |
===========
''', ''' 
    +---+
    |   |
        |
        |
        |
        |
===========
''']

#Take a random word and transform in to a list
word_list = ["amor", "casa", "carro","australopiteco"]
chosen_word = random.choice(word_list)
print(chosen_word)

guessed_letter = []
display = ["_"] * len(chosen_word)
lives = 6

placeholder = ""
game_over = False

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

while not game_over:   
    #Player chose a letter
    guess = input("Guess a letter: ").lower()

    #Check if the player alredy guessed the letter
    if guess in guessed_letter:
        print("You alredy guessed this letter, try another")

    #Run the list and if the guess is equal the letter in the word, put the letter in the list
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess
            guessed_letter = guess
            
    #If the guess letter is not in the word, the player lose one live
    if guess.lower() not in chosen_word.lower():
            lives -= 1

    print(" ".join(display))

    #Print the Stage
    if lives == 6:
        print(stages[lives])
    elif lives == 5:
        print(stages[lives])
    elif lives == 4:
        print(stages[lives])
    elif lives == 3:
        print(stages[lives])
    elif lives == 2:
        print(stages[lives])
    elif lives == 1:
        print(stages[lives])
    elif lives == 0:
        print(stages[lives])
    
    #Check if the game ends
    if "_" not in display:
        game_over = True
        print("You Win")
    elif lives == 0:
        game_over = True
        print("You Lose")