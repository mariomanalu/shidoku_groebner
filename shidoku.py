import numpy as np
import sys
import sympy
from sympy import solve
from sympy.abc import a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p

# Declare variables needed to store variables that represent every cell
variables = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
cells = 16

# Check whether the input shidoku is of length 16 and there are at least 4 clues
def check_shidoku(shidoku):
    counter = 0
    if len(shidoku)!= cells:
        sys.exit("Check your shidoku board again")
    
    for index in range(cells):
        if shidoku[index] != 0:
            counter += 1
    
    if counter < 4:
        sys.exit("Not enough clues are given")


# Encode the shidoku board. Fill in empty cells with the corresponding variables.
def encode_shidoku(shidoku):
    new_shidoku = [0 for index in range(cells)]
    empty_cells = 0
    for index in range(cells):
        if shidoku[index] != 0:
            new_shidoku[index] = shidoku[index]
        else:
            empty_cells += 1
            new_shidoku[index] = variables[index]

    return new_shidoku, empty_cells

# Generate the equations restricting the rows
def generate_row_equations(shidoku):
    row_equations = [0 for index in range(8)]

    for index in range(0, 4):
        offset = index * 4
        sum = shidoku[offset] + shidoku[offset + 1] + shidoku[offset + 2] + shidoku[offset + 3] - 10
        product = (shidoku[offset] * shidoku[offset + 1] * shidoku[offset + 2] * shidoku[offset + 3]) - 24
        row_equations[2*index] = sum
        row_equations[2*index + 1] = product

    return row_equations

# Generate the equations restricting the columns
def generate_column_equations(shidoku):
    column_equations = [0 for index in range(8)]

    for index in range(0, 4):
        sum = shidoku[index] + shidoku[index + 4] + shidoku[index + 8] + shidoku[index + 12] - 10
        product = (shidoku[index] * shidoku[index + 4] * shidoku[index + 8] * shidoku[index + 12]) - 24
        column_equations[2*index] = sum
        column_equations[(2*index) + 1] = product

    return column_equations

# Generate the equations restricting the squares
def generate_square_equations(shidoku):
    square_equations = [0 for index in range(8)]
    
    for index in range(0, 2):
        offset = index * 2
        sum_1 = shidoku[offset] + shidoku[offset + 1] + shidoku[offset + 4] + shidoku[offset + 5] - 10
        product_1 = (shidoku[offset] * shidoku[offset + 1] * shidoku[offset + 4] * shidoku[offset + 5]) - 24
        sum_2 = shidoku[offset + 8] + shidoku[offset + 1 + 8] + shidoku[offset + 4 + 8] + shidoku[offset + 5 + 8] - 10
        product_2 = (shidoku[offset + 8] * shidoku[offset + 1 + 8] * shidoku[offset + 4 + 8] * shidoku[offset + 5 + 8]) - 24
        
        square_equations[(4*index)] = sum_1
        square_equations[(4*index) + 1] = product_1
        square_equations[(4*index) + 2] = sum_2
        square_equations[(4*index) + 3] = product_2

    return square_equations

# Solve shidoku
def solve_shidoku(initial_shidoku_board):
    check_shidoku(initial_shidoku_board)
    shidoku, empty_cells = encode_shidoku(initial_shidoku_board)
    
    # Obtain equations that encode the rows
    row = generate_row_equations(shidoku)

    # Obtain equations that encode the columns
    column = generate_column_equations(shidoku)

    # Obtain equations that encode the squares
    square = generate_square_equations(shidoku)

    # Store all the equations obtained in one list
    equations = row + column + square
    print(equations)
    # Compute the grobner basis for the equations
    grobner_basis = sympy.groebner(equations, a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, order = 'lex')
    print(grobner_basis)
    # Solve the system of equations
    system = [grobner_basis[i] for i in range(empty_cells)]
    answers = solve(system, dict = True)

    iterator = 0
    for index in range(cells):
        if (initial_shidoku_board[index] == 0):
            shidoku[index] = answers[0].get(variables[index])
            iterator += 1
    
    # Convert the one-dimensional array into the two-dimensional form
    final_shidoku = [0 for index in range(4)]
    for index in range(4):
        offset = index * 4
        row = shidoku[offset: offset + 4]
        final_shidoku[index] = row
    
    return np.matrix(final_shidoku)