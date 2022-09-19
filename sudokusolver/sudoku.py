def create(grid = []):
    
    # A 9x9 grid
    
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append(0)
    return grid

# puts value on position x, y on grid grid
def put(grid, x, y, value):
        grid[x-1][y-1] = value

def printgrid(grid):
    
    for i in range(0,9,3):
            for j in range(0,9,3):
                print(f"{grid[i][j]}",end = '')
                print(f"{grid[i][j+1]}",end = '')
                print(f"{grid[i][j+2]}",end = ' ')
            print('')
            for j in range(0,9,3):
                print(f"{grid[i+1][j]}",end = '')
                print(f"{grid[i+1][j+1]}",end = '')
                print(f"{grid[i+1][j+2]}",end = ' ')
            print('')
            for j in range(0,9,3):
                print(f"{grid[i+2][j]}",end = '')
                print(f"{grid[i+2][j+1]}",end = '')
                print(f"{grid[i+2][j+2]}",end = ' ')
            print('\n')
   
# checks if the whole block is valid, block should be 9 int's
def isInValidBlock(block):
    # print(f"Our block: {block}")
    for i in range(0,9):
        if block[i] != 0:
            for j in range(0,9):
                if i != j and block[i] == block[j]:
                    return True
    return False
    
 
# check if a grid is a valid sudoku
def isValid(grid):
    
    # check horizontal
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] != 0:
                for k in range(0,9):
                    # on line grid[i] there should be no 2 numbers the smae
                    if grid[i][j] == grid[i][k] and j != k:
                        return False
    #[0][0] [0][1] [0][2]
    print("Horizontal valid")
        
    # check vertical
    for i in range(0,9):
        for j in range(0,9):
            if grid[j][i] != 0:
                for k in range(0,9):
                    # on line grid[0][i] there should be no 2 numbers the smae
                    if grid[j][i] == grid[k][i] and j != k:
                        return False
    #[0][0] [1][0] [2][0]
    
    print("Vertical   valid")
    
    # check square
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = []
            for k in range(0,3):
                for l in range(0,3):
                    block.append(grid[i +k][j +l])
            if isInValidBlock(block):
                return False
    
    print("Square     valid")
    return True

def solve(grid):
    if not isValid(grid):
        print("I cannot solve an invalid sudoku's!")
        return
    
    if isSolved(grid):
        print("sudoku is already solved!")
    
    i = 0
    j = 0
    k = 1
    while not isSolved(grid):
        if grid[i][j] == 0:
            grid[i][j] = k
        if isValid(grid):
            # advance
            i,j,k = advance(i,j,k)
            
        else:
            # guess next
            k += 1
            while k != 10:
            # if k == 10:
                # backtrack
                grid[i][j] = 0 
                j -= 1
                if j == -1:
                    i -=1
                    j = 9
                
                k = grid[i][j] +1
                if k == 10:
                    
                   
            else:
                grid[i][j] = k
            

def advance(i,j,k):
    j += 1
    if j == 9:
        j = 0
        i += 1  
    k = map[i][j]
    return i,j,k
            
def isSolved(grid):
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True
    
        
    