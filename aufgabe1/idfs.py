# idfs.py
# ------------------------------------------
# Author: Michael Blaich
# Datum: 21.03.2025
# Beschreibung: Implementierung der Iterativen Tiefensuche für
# das 8-Puzzle-Problem.
# ------------------------------------------
from board import Board
from collections import deque


def dfs(cur_board, path, limit, visited):
    if cur_board.is_solved():
        return path

    if limit == 0:
        return None

    visited.add(cur_board)
    for move in cur_board.possible_actions():
        if move in visited:
            continue

        path.append(move)

        result = dfs(move, path, limit - 1, visited)
        if result:
            return result
        path.pop()

    return None


def idfs(start_board: Board, limit=1000):  # max. Tiefe arbiträr gesetzt
    """
    Iterative Tiefensuche mit Schleife zur Erhöhung des Tiefenlimits.
    Gibt den Lösungspfad als deque zurück oder None, wenn keine Lösung gefunden
    wurde.
    """
    for depth in range(limit):
        path = deque([start_board])
        visited = set()
        result = dfs(start_board, path, depth, visited)
        if result:
            return result
    return None
