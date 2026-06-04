# Sudoku solver using CSP and backtracking

# Overview 

This project is an AI-based sudoku solver written in python. It models sudoku as a CSP and solves puzzles using recursive backtracking.

the program lets the user choose an either pre built easy or hard sudoku puzzle. It then solves the selected puzzle and then display performance statistics like number of backtrackign steps, time taken and number of placements.

# Group members
Esak Mehari 
Johnson Giang
Zain Naeem

# AI concepts used 

# Contraint Satisfaction problem (CSP)

- variables: empty cells in sudoku grid
- domains: possible values from 1 to 9
- constraints: No repeated number in any row, column or 3x3 subgrid

# backtracking 

the solver uses backtracking:

1. find an empty cell.
2. generate the possible values for that cell.
3. check whether each value satisfies the Sudoku constraints.
4. place a valid value
5. continue solving the next empty cell.
6. return to the last step if the current choice is invalid. 

# how to run

1. open a terminal
2. navigate to the src folder
3. run main.py 

# output 
Choose difficulty: easy or hard: hard

Selected difficulty: hard

Original Sudoku board:
. . . | . . . | . 1 2
. . . | . 3 5 | . . .
. . . | 6 . . | . 7 .
---------------------
7 . . | . . . | 3 . .
. . . | 4 . . | 8 . .
1 . . | . . . | . . .
---------------------
. . . | 1 2 . | . . .
. 8 . | . . . | . 4 .
. 5 . | . . . | 6 . .

Solved Sudoku board:
6 7 3 | 8 9 4 | 5 1 2
9 1 2 | 7 3 5 | 4 8 6
8 4 5 | 6 1 2 | 9 7 3
---------------------
7 9 8 | 2 6 1 | 3 5 4
5 2 6 | 4 7 3 | 8 9 1
1 3 4 | 5 8 9 | 2 6 7
---------------------
4 6 9 | 1 2 8 | 7 3 5
2 8 7 | 3 5 6 | 1 4 9
3 5 1 | 9 4 7 | 6 2 8

Placements attempted: 10373
Backtracking steps: 10309
Time Taken: 1.934713 seconds

Choose difficulty: easy or hard: easy

Selected difficulty: easy

Original Sudoku board:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
---------------------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
---------------------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Solved Sudoku board:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

Placements attempted: 4208
Backtracking steps: 4157
Time Taken: 0.017311 seconds

Choose difficulty: easy or hard: medium
Invalid difficulty. Using easy mode.

Selected difficulty: easy

Original Sudoku board:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
---------------------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
---------------------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Solved Sudoku board:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

Placements attempted: 4208
Backtracking steps: 4157
Time Taken: 0.021389 seconds