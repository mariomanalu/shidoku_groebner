import shidoku as S

# This program solves a 4x4 version of the famous Sudoku puzzle called Shidoku using the Gröbner bases
# How to use:
# 1. Store any "solvable" Shidoku board as a 1D array of length 16 with 0 representing the empty cells
# 2. Call solve_shidoku()
# 3. Print the answer in the form of 2D array

# We include eight tests for demonstration
# Tests:

# Test 1
shidoku_board_1 = [4, 0, 0, 0, 2, 1, 0, 0, 0, 4, 0, 2, 0, 0, 3, 0]
# The above shidoku looks like following
#[[4, 0, 0, 0]
# [2, 1, 0, 0]
# [0, 4, 0, 2]
# [0, 0, 3, 4]]

answer_1 = S.solve_shidoku(shidoku_board_1)
print("Solution 1")
print(answer_1)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
#[[4 3 2 1]
# [2 1 4 3]
# [3 4 1 2]
# [1 2 3 4]]

print("\n")
# Test 2
shidoku_board_2 = [0, 0, 0, 3, 3, 2, 4, 0, 0, 4, 3, 2, 2, 0, 0, 0]
# The above shidoku looks like following
#[[0, 0, 0, 3]
# [3, 2, 4, 0]
# [0, 4, 3, 2]
# [2, 0, 0, 0]]

answer_2 = S.solve_shidoku(shidoku_board_2)
print("Solution 2")
print(answer_2)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
#[[4 1 2 3]
# [3 2 4 1]
# [1 4 3 2]
# [2 3 1 4]]

print("\n")
# Test 3
shidoku_board_3 = [0, 0, 0, 4, 4, 0, 2, 0, 0, 3, 0, 1, 1, 0, 0, 0]
# The above shidoku looks like following
#[[0, 0, 0, 4]
# [4, 0, 2, 0]
# [0, 3, 0, 1]
# [1, 0, 0, 0]]

answer_3 = S.solve_shidoku(shidoku_board_3)
print("Solution 3")
print(answer_3)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
# [[3 2 1 4]
#  [4 1 2 3]
#  [2 3 4 1]
#  [1 4 3 2]]

print("\n")
# Test 4: A shidoku board with the minimum number of clues possible 
shidoku_board_4 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 3, 0, 0, 0]
# The above shidoku looks like following
#[[0, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 1, 0, 2]
# [3, 0, 0, 0]]

answer_4 = S.solve_shidoku(shidoku_board_4)
print("Solution 4")
print(answer_4)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
# [[1 4 2 3]
#  [2 3 4 1]
#  [4 1 3 2]
#  [3 2 1 4]]

print("\n")

# Test 5: A shidoku board with the minimum number of clues possible 
shidoku_board_5 = [0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 3, 0]
# The above shidoku looks like following
#[[0, 0, 0, 0]
# [0, 1, 0, 2]
# [0, 0, 0, 0]
# [1, 0, 3, 0]]

answer_5 = S.solve_shidoku(shidoku_board_5)
print("Solution 5")
print(answer_5)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
# [[2 4 1 3]
#  [3 1 4 2]
#  [4 3 2 1]
#  [1 2 3 4]]

print("\n")

# Test 6: A shidoku board with the minimum number of clues possible 
shidoku_board_6 = [0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0]
# The above shidoku looks like following
#[[0, 0, 0, 1]
# [4, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 3, 2, 0]]

answer_6 = S.solve_shidoku(shidoku_board_6)
print("Solution 6")
print(answer_6)

# The solution to the above shidoku, as returned by the solve_shidoku() function, is
# [[3 2 4 1]
#  [4 1 3 2]
#  [2 4 1 3]
#  [1 3 2 4]]