#library for the groebner function
import sympy

#library for writing functions
from sympy.abc import x,y

#library to generate a sudoku board
from sudokugen.generator import generate, Difficulty

F = [f1, f2] = [x*y - 2*x*y, x**2-2*y**2]

lst = sympy.groebner([f1, f2], x,y, order = 'lex')
print(lst)

new_board = generate(difficulty = Difficulty.MEDIUM)
#print(np.matrix(new_board))
print(type(new_board))
print(new_board[0])
print("Hello")