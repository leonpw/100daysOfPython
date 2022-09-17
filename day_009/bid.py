import os
from art import logo

def clear():
    if os.name == "posix":
        _ = os.system("clear")


clear()
print(logo)

bidders = {}
moreBidders = True

while moreBidders:

    name = input("What is your name: ")
    bid = int(input("What is your bid: $ "))

    # bidders["name"] = {"bid": bid}
    bidders[name] = bid

    print(f'Your bid of {bid} has been received, {name} ....')
    
    
    if input("Are there more bidders? [yes][no]") == "no":
        moreBidders = False
    clear()


highestbid = 0
name = ''

for bidder in bidders:
    bid = bidders[bidder]
    if bid > highestbid:
        highestbid = bid
        name = bidder
    
print(f"The highest bidder is: {name} with $ {bid}")