import random
HANGMANPICS = ['''
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


#Step 1 

word_list = ["aardvark", "baboon", "camel"]
hangmanscore = 0

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0,len(word_list)-1)]

print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


guess_word = []
for i in range(0,len(chosen_word)):
    guess_word.append('_')

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

game_over = False
while(not game_over):
    
    guess = input("Guess a letter: ").lower()
    
    letter_found = False
    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess:
            letter_found = True
            guess_word[i] = chosen_word[i]



    if letter_found:        
        print(F"The letter was found!")
    else:
        print(HANGMANPICS[hangmanscore])
        hangmanscore += 1

    if hangmanscore > 6:
        game_over = True
        print('game_over')

    shouldStop = True
    for i in guess_word:
        if i == '_':
            shouldStop = False

    if shouldStop:
        game_over = True
        print("Game over, you won!")
    print(''.join(guess_word))