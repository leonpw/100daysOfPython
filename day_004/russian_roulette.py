
import random

names = input("Who are the payers? \n").split(', ')

print(names)

payer = random.randint(0,len(names)-1)

print(f"{names[payer]} is gonna pay today!")
