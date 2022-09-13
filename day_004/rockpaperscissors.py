import random

rps =["🪨 (rock)", "🧻 (paper)", "✂ (scissors)"]

user = int(input("Rock [0], paper [1] or scissors [2] ? "))

print(f"You choose {rps[user]} !") 

comp = random.randint(0, 2)
print(f"The computer choose {rps[comp]}")

map = [
    [[0, "draw"], [1, "won"], [2, "lost"]],
    [[0, "lost"], [1, "draw"], [2, "won"]],
    [[0, "won"], [1, "last"], [2, "draw"]],
]

print(f"It's a: {map[comp][user][1]}")