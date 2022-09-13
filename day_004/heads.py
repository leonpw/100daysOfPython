import random

seed = float(input("What is your seed? \n"))

random.seed(seed)
rand = random.randint(0,1)

if rand == 1:
    print("Heads")
else :
    print("Tail")