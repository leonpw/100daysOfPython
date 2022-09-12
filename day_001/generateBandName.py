from os import read
from time import sleep

print("What city do you come from?")
city = str(input())
print(f"So you are from {city} ?")
sleep(0.5)
print("And what is your pets name? I need it to reset your g00gle password...")
petname = str(input())
bandname = city + " " + petname
print("Generating band name ... This may take a while")
sleep(2)

print(f"You band name: {bandname}")
