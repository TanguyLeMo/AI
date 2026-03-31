
# board.py
# ------------------------------------------
# Author: Michael Blaich
# Datum: 21.03.2025
# Beschreibung: Implementierung der Board-Klasse für das 8-Puzzle-Problem.
# ------------------------------------------
import random
import math

class Board:
    """
    Repräsentiert ein 8-Puzzle-Board.

    Methoden:
    - parity(): Prüft, ob das Puzzle lösbar ist.
    - h1(), h2(): Platzhalter für Heuristikfunktionen.
    - possible_actions(): Liefert gültige Nachfolgezustände.
    - is_solved(): Prüft, ob das Ziel erreicht ist.
    """

    N = 8  # Problemgröße

    def __init__(self, board=None):
        """
        Initialisiert das Board.
        Wenn kein Board übergeben wird, wird ein zufälliges, lösbares Board
        erzeugt.
        """
        if board:
            self.board = list(board)
        else:
            self.board = list(range(Board.N + 1))
            while True:
                random.shuffle(self.board)
                if self.parity():
                    break

    def __str__(self):
        """
        Gibt das Board als String aus.
        """
        return f"Puzzle{{board={self.board}}}"

    def __eq__(self, other):
        """
        Zwei Boards sind gleich, wenn ihr Zustand gleich ist.
        """
        return isinstance(other, Board) and self.board == other.board

    def __hash__(self):
        """
        Ermöglicht das Nutzen von Board in Sets oder als Dictionary-Keys.
        """
        return hash(tuple(self.board))

    def parity(self) -> bool:
        list_without_zero = [x for x in self.board if x != 0]
        tupleValues: list[tuple[int, int]] = [(list_without_zero[index], list_without_zero[index + 1])
        for index in range(0, len(list_without_zero), 2)]

        parity_count = 0
        for tuple_entry in tupleValues:
            if tuple_entry[0] > tuple_entry[1]:
                parity_count += 1
        return parity_count % 2 == 0

    def h1(self)-> int:
        """
        Heuristikfunktion h1 (siehe Aufgabenstellung).
        TODO: Implementiere einfache Heuristik
        """
        current_heuristic = len(self.board) - 1 # dont count the empty field / Zero
        for index in range(0, len(self.board)):
            if index == self.board[index] :
                current_heuristic -= 1
        return current_heuristic  # Dummywert

    def h2(self):
        current_heuristic = 0
        board_width =  math.sqrt(len(self.board))
        for index in range(0, len(self.board)):
            if index == self.board[index]:
                continue
            difference = abs(index - self.board[index])
            skip_rows = math.floor(difference / board_width)
            skip_blocks =  abs(skip_rows * board_width - difference)
            current_heuristic += skip_rows + skip_blocks
            print(f"current heuristic: {current_heuristic}")
        """
        Heuristikfunktion h2 (siehe Aufgabenstellung).
        TODO: Implementiere verbesserte Heuristik
        """
        return current_heuristic  # Dummywert

    def possible_actions(self):
        """
        Gibt eine Liste aller möglichen Folge-Boards zurück,
        die durch einen gültigen Zug entstehen.
        TODO: Diese Methode muss noch implementiert werden.
        """
        return []

    def is_solved(self):
        """
        Prüft, ob das Board im Zielzustand ist (0,1,2,3,...,8).
        TODO: Implementiere die Prüfung ob das Board gelöst ist.
        """
        return False


def main():
    b = Board([7, 2, 4, 5, 0, 6, 8, 3, 1])  # Startzustand manuell setzen
    # b = Board()  # Lösbares Puzzle zufällig generieren
    print("Startzustand:", b)

    print("Parität:,", b.parity())

    print("Heuristik h1: ", b.h1())
    print("Heuristik h2: ", b.h2())

    for child in b.possible_actions():
        print(child)

    print("Ist gelöst:", b.is_solved())


if __name__ == "__main__":
    main()
