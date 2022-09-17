import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def show_winner(user, comp):
    if user["score"] == comp["score"]:
        print("It's a draw!")
    elif user["score"] > comp["score"]:
        print("You won!")
    elif user["score"] < comp["score"]:
        print("You lost!")


def print_cards(dict):
    cards_text = f' cards: {dict["cards"][0]}'
    for i in range(1, len(dict["cards"])):
        cards_text += f", {dict['cards'][i]}"
    return cards_text


def update_score(dict):
    dict["score"] = sum(dict["cards"])


def draw_card(dict):
    dict["cards"].append(random.choice(cards))
    update_score(dict)


def play_game():
    user = {
        "cards": [random.choice(cards), random.choice(cards)],
    }
    comp = {
        "cards": [random.choice(cards), random.choice(cards)],
    }
    update_score(user)
    update_score(comp)

    print("Your " + print_cards(user))

    print(f"The computer has a {comp['cards'][0]} and ??? ")

    userdraw = True
    userLost = False
    while userdraw:
        userdraw = input("Do you want to draw another card? [y][n]: ") == "y"
        if userdraw:
            draw_card(user)
            print("Your " + print_cards(user))
            print(f'Your score: {user["score"]}')
        if user['score'] > 21:
            userdraw = False
            userLost = True
            print('You lost!')

    compdraw = True
    while compdraw and not userLost:
        score = comp["score"]
        if score < 18:
            draw_card(comp)
        else:
            compdraw = False

    print("Computer " + print_cards(comp))

    print()
    if not userLost:
        print('Let`s show winners')
        show_winner(user, comp)
    print()

if input("Do you want to play a game of blackjack? [y][n]: ") == "y":
    play_game()
    shouldContinue = True
else:
    shouldContinue = False

while shouldContinue:
    shouldContinue = (
        input("Do you want to play another game of blackjack? [y][n]: ") == "y"
    )
    if shouldContinue:
        play_game()

print("Thank you for playing with us :D")
