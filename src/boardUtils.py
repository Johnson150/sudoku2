"""Utility functions for Sudoku boards."""

from __future__ import annotations

from sudokuSolver import Board


def copyBoard(board: Board) -> Board:
    return [row[:] for row in board]


def boardsEqual(first: Board, second: Board) -> bool:
    return first == second