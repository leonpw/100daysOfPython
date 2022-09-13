
gridsize = int(input("How big is your size? "))

map = []
for i in range(0,gridsize):
    map.append([])
    for j in range(0,gridsize):
        map[i].append('⬜')

for i in range(0,len(map)):
    print(f"{[map[i]]}")
    
input = input("Where do you want to put the treasure?\n")

map[int(input[1])-1][int(input[0])-1] = "💰"

for i in range(0,len(map)):
    print(f"{[map[i]]}")
