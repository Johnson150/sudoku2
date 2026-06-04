## sudoku solver as a CSP and solved using recursive backtracking

from dataclasses import dataclass

Board = list[list[int]]

## stat tracking for placements and backtracking
@dataclass
class SolverStats:
    placements: int = 0
    backtracks: int = 0


## check if the starting board is valid
def validateBoard(board: Board):
    if len(board) != 9:
        raise ValueError("Sudoku board must have exactly 9 rows.")

    for row in board:
        if len(row) != 9:
            raise ValueError("Each row must have exactly 9 columns.")

        for value in row:
            if not isinstance(value, int) or value < 0 or value > 9:
                raise ValueError("Board values must be numbers from 0 to 9.")

    for row in range(9):
        for column in range(9):
            value = board[row][column]

            if value != 0:
                board[row][column] = 0

                if not satisfiesConstraints(board, row, column, value):
                    board[row][column] = value
                    raise ValueError("Starting board violates Sudoku rules.")

                board[row][column] = value


## return the next empty cell as row or column or none if solved.
def findEmptyCell(board: Board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column

    return None


# return possible values for a cell
def getDomain(board: Board, row: int, column: int):
    domain = []

    for number in range(1, 10):
        if satisfiesConstraints(board, row, column, number):
            domain.append(number)

    return domain


# checks constraints, row, column and 3x3 box constraints
def satisfiesConstraints(board: Board, row: int, column: int, number: int):
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
# - select an empty variable
# - get its domain
# - try values that satisfy the constraints
# - backtrack if a choice is invalid
def solveCsp(board: Board, stats: SolverStats):
    emptyCell = findEmptyCell(board)

    if emptyCell is None:
        return True

    row, column = emptyCell
    domain = getDomain(board, row, column)

    for value in domain:
        board[row][column] = value
        stats.placements += 1

        if solveCsp(board, stats):
            return True

        board[row][column] = 0
        stats.backtracks += 1

    return False


## main function used by main.py
def solveSudoku(board: Board, stats: SolverStats):
    validateBoard(board)
    return solveCsp(board, stats)


## check if the board is fully solved
def isSolved(board: Board):
    try:
        validateBoard(board)
    except ValueError:
        return False

    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return False

    return True


# print sudoku board
def printBoard(board: Board):
    for rowIndex, row in enumerate(board):
        if rowIndex > 0 and rowIndex % 3 == 0:
            print("-" * 21)

        values = []

        for colIndex, value in enumerate(row):
            if colIndex > 0 and colIndex % 3 == 0:
                values.append("|")

            values.append(str(value) if value != 0 else ".")

        print(" ".join(values))