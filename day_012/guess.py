import random


answer = random.randint(0, 100)

level = {"easy": 10, "medium": 8, "hard": 9, "extreme": 5}
level_choosen = input("Choose your level: [easy][medium][hard][extreme]: ")

guesses_left = level[level_choosen]

won = False
while guesses_left > 0 and not won:
    print(f"You have {guesses_left} guesses left...")
    
    guess = int(input("Make a guess between 0 and 100 ... "))
    
    if guess == answer:
        won = True
        print(f"You guessed the correct answer: {answer}!")
    elif guess > answer:
        print(f'Your guess of {guess} is too high')
    elif guess < answer:
        print(f'Your guess of {guess} is too low')
       
    guesses_left -= 1 
if not won:
    print('You have no attempts left. You lost.')
    