##sudoku solver as a CSP and solved using recursive backtracking

from dataclasses import dataclass

board = list[list[int]]

##stat tracking for placements and backtracking 
@dataclass
class SolverStats:
    placements: int = 0
    backtracks: int = 0

##return the next emprty cell as row or column or none if solved.
def findEmptyCell(board: board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
            
    return None

#return the next empty cell as (row, col), or None if solved.
def getDomain(board: board, row: int, column: int):
    domain = []

    for number in range(1,10):
        if satisfiesConstraints(board, row, column, number):
            domain.append(number)
        
    return domain

# checks constraints, row, column and 3x3 box constraints
def satisfiesConstraints(board: board, row: int, column: int, number: int):
    if number in board[row]:
        return False
    
    for currentRow in range(9):
        if board[currentRow][column] == number:
            return False
    boxStartRow = (row // 3) * 3
    boxStartColumn = (column // 3) * 3

    for currentRow in range(boxStartRow, boxStartRow + 3):
        for currentColumn in range(boxStartColumn, boxStartColumn + 3):
            if board[currentRow][currentColumn] == number:
                return False
    
    return True

# using backtracking:
# -select an empty vairable
# -get its domain
# -try values that satisfy the constraints
# -Backtrack if a choice is invalid
def solveCsp(board: board, stats: SolverStats):
    emptyCell = findEmptyCell(board)

    if emptyCell is None:
        return True

    row, column = emptyCell
    domain = getDomain(board, row, column)

    for value in domain:
        board[row][column] = value
        stats.placements += 1

        if solveCsp(board,stats):
            return True
        
        board[row][column]
        stats.backtracks += 1
    
    return False

#print sudoku board
def printBoard(board: board):
    for rowIndex, row in enumerate(board):
        if rowIndex > 0 and rowIndex % 3 == 0:
            print("-" * 21)

        values = []

        for colIndex, value in enumerate(row):
            if colIndex > 0 and colIndex % 3 == 0:
                values.append("|")
            
            values.append(str(value))

        print(" ".join(values))
    

