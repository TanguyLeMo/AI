# idfs.py
# ------------------------------------------
# Author: Michael Blaich
# Datum: 21.03.2025
# Beschreibung: Implementierung der Iterativen Tiefensuche für
# das 8-Puzzle-Problem.
# ------------------------------------------
from board import Board
from collections import deque

i = 1


def dfs(cur_board, path, limit, visited):
    global i
    if cur_board.is_solved():
        return path

    if limit == 0:
        return None

    visited.add(cur_board)

    for move in cur_board.possible_actions():
        i = i + 1
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
            print("Durchlaufene Nodes: " + str(i))
            return result
    print("Durchlaufene Nodes: " + str(i))
    return None
