from sudokuSolver import Board, SolverStats, printBoard, solveSudoku, validateBoard
from heuristicSolver import solveSudokuHeuristic
import time

PUZZLES: dict[str, Board] = {
    "easy": [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    "hard": [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 8, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
    ],
}


def main() -> None:
    difficulty = input("Choose difficulty: easy or hard: ").strip().lower()

    if difficulty not in PUZZLES:
        print("Invalid difficulty. Using easy mode.")
        difficulty = "easy"

    board = [row[:] for row in PUZZLES[difficulty]]

    validateBoard(board)

    stats = SolverStats()

    print(f"\nSelected difficulty: {difficulty}")
    print("\nOriginal Sudoku board:")
    printBoard(board)

    #start timer
    startTime = time.perf_counter()

    # Use heuristic solver for hard puzzles
    if difficulty == "hard":
        solved = solveSudokuHeuristic(board, stats)
    else:
        solved = solveSudoku(board, stats)

    #stop timer
    endTime = time.perf_counter()
    timeTaken = endTime - startTime

    if solved:
        print("\nSolved Sudoku board:")
        printBoard(board)
        print(f"\nPlacements attempted: {stats.placements}")
        print(f"Backtracking steps: {stats.backtracks}")
        print(f"Time Taken: {timeTaken:6f} seconds")
    else:
        print("\nNo valid solution exists.")


if __name__ == "__main__":
    main()