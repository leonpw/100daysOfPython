
import sudoku

s = sudoku.create()

sudoku.put(s, 1,1,1)
sudoku.put(s, 1,2,2)
sudoku.put(s, 1,3,3)

sudoku.put(s, 2,1,4)
sudoku.put(s, 2,2,5)
sudoku.put(s, 2,3,6)

sudoku.put(s, 3,1,7)
sudoku.put(s, 3,2,8)
sudoku.put(s, 3,3,9)

sudoku.put(s, 5,5,1)
sudoku.put(s, 6,6,2)




sudoku.printgrid(s)


print(f"is valid: {sudoku.isValid(s)}")

sudoku.solve(s)