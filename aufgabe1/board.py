
# board.py
# ------------------------------------------
# Author: Michael Blaich
# Datum: 21.03.2025
# Beschreibung: Implementierung der Board-Klasse für das 8-Puzzle-Problem.
# ------------------------------------------
import random


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

    def parity(self):
        """
        Paritätsprüfung:
        Gibt True zurück, wenn das Board lösbar ist.
        TODO: Implementiere die Berechnung der Parität
        """
        return False

    def h1(self):
        """
        Heuristikfunktion h1 (siehe Aufgabenstellung).
        TODO: Implementiere einfache Heuristik
        """
        return 0  # Dummywert

    def h2(self):
        """
        Heuristikfunktion h2 (siehe Aufgabenstellung).
        TODO: Implementiere verbesserte Heuristik
        """
        return 0  # Dummywert

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
