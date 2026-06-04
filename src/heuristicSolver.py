"""Sudoku solver using the MRV heuristic."""

from __future__ import annotations

from sudokuSolver import Board, SolverStats, getDomain, validateBoard


def findBestEmptyCell(board: Board) -> tuple[int, int] | None:
    bestCell: tuple[int, int] | None = None
    bestDomainSize = 10

    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                domainSize = len(getDomain(board, row, column))

                if domainSize < bestDomainSize:
                    bestDomainSize = domainSize
                    bestCell = (row, column)

                if bestDomainSize == 0:
                    return bestCell

    return bestCell


def solveWithHeuristic(board: Board, stats: SolverStats | None = None) -> bool:
    if stats is None:
        stats = SolverStats()

    emptyCell = findBestEmptyCell(board)

    if emptyCell is None:
        return True

    row, column = emptyCell
    domain = getDomain(board, row, column)

    for value in domain:
        board[row][column] = value
        stats.placements += 1

        if solveWithHeuristic(board, stats):
            return True

        board[row][column] = 0
        stats.backtracks += 1

    return False


def solveSudokuHeuristic(board: Board, stats: SolverStats | None = None) -> bool:
    validateBoard(board)
    return solveWithHeuristic(board, stats)