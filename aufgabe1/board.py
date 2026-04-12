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

    # Stimmt bisher glaub noch nicht ganz, weil aus einem Zustand [4,1,2,3] würde es nur (4,1) und (2,3) tupeln
    # richtig wäre (4,1), (4,2), (4,3)
    """
        def parity(self) -> bool:
        list_without_zero = [x for x in self.board if x != 0]
        tupleValues: list[tuple[int, int]] = [(list_without_zero[index], list_without_zero[index + 1])
                                              for index in range(0, len(list_without_zero), 2)]

        parity_count = 0
        for tuple_entry in tupleValues:
            if tuple_entry[0] > tuple_entry[1]:
                parity_count += 1
        return parity_count % 2 == 0 
    """

    # Hier mal mein Ansatz, hoffe der stimmt so
    def parity(self) -> bool:
        list_without_zero = [x for x in self.board if x != 0]

        false_tuples: list[tuple[int, int]] = []
        visited_numbers_list: list[int] = []

        # Durchlaufe alle Einträge der Liste
        for number in list_without_zero:
            for visited_number in visited_numbers_list:
                # Prüfe für jeden Eintrag der Liste ob er kleiner ist als irgendein Vorgänger
                if number < visited_number:
                    false_tuples.append((number, visited_number))  # Falls ja erstelle ein Tupel aus beiden
            visited_numbers_list.append(number)
        return len(false_tuples) % 2 == 0

    def h1(self) -> int:
        """
        Heuristikfunktion h1 (siehe Aufgabenstellung).
        """
        current_heuristic = len(self.board) - 1  # dont count the empty field / Zero
        for index in range(0, len(self.board)):
            if index == self.board[index]:
                current_heuristic -= 1
        return current_heuristic  # Dummywert

    def h2(self):
        current_heuristic = 0
        board_width = math.sqrt(len(self.board))
        for index in range(0, len(self.board)):
            if index == self.board[index]:
                continue
            difference = abs(index - self.board[index])
            skip_rows = math.floor(difference / board_width)
            skip_blocks = abs(skip_rows * board_width - difference)
            current_heuristic += skip_rows + skip_blocks
            #print(f"current heuristic: {current_heuristic}")
        """
        Heuristikfunktion h2 (siehe Aufgabenstellung).
        TODO: Implementiere verbesserte Heuristik
        """
        return current_heuristic  # Dummywert

    def possible_actions(self) :
        """
        Gibt eine Liste aller möglichen Folge-Boards zurück,
        die durch einen gültigen Zug entstehen.
        """
        possible_moves: list[Board] = []
        index_of_zero = self.board.index(0)  # Finde den Index des leeren Felds
        # Falls das Leere Feld nicht in der linken Spalte ist, kann es nach links verschoben werden
        if index_of_zero % 3 != 0:
            new_board = self.board[:]
            temp = new_board[index_of_zero - 1]  # Wert der Feldes links neben dem leeren Feld
            new_board[index_of_zero - 1] = 0  # leeres Feld nach links verschieben
            new_board[index_of_zero] = temp

            possible_moves.append(Board(new_board))

        # Falls das leere Feld nicht in der rechten Spalte ist, kann es nach rechts verschoben werden
        if (index_of_zero + 1) % 3 != 0:
            new_board = self.board[:]
            temp = new_board[index_of_zero + 1]
            new_board[index_of_zero + 1] = 0
            new_board[index_of_zero] = temp

            possible_moves.append(Board(new_board))

        # Falls das leere Feld nicht in der obersten Reihe ist, kann es nach oben verschoben werden
        if index_of_zero > 2:
            new_board = self.board[:]
            temp = new_board[index_of_zero - 3]
            new_board[index_of_zero - 3] = 0
            new_board[index_of_zero] = temp

            possible_moves.append(Board(new_board))

        # Falls das leere Feld nicht in der untersten Reihe ist, kann es nach unten verschoben werden
        if index_of_zero < 6:
            new_board = self.board[:]
            temp = new_board[index_of_zero + 3]
            new_board[index_of_zero + 3] = 0
            new_board[index_of_zero] = temp

            possible_moves.append(Board(new_board))

        return possible_moves

    def is_solved(self):
        """
        Prüft, ob das Board im Zielzustand ist (0,1,2,3,...,8).
        """
        return self.board == list(range(9))


def main():
    b = Board([7, 2, 4, 5, 0, 6, 8, 3, 1])  # Startzustand manuell setzen
    # b = Board()  # Lösbares Puzzle zufällig generieren
    print("Startzustand:", b)

    print("Parität:,", b.parity())

    print("Heuristik h1: ", b.h1())
    print("Heuristik h2: ", b.h2())

    for child in b.possible_actions():
        print(child)
    print("Ist lösbar:", b.parity())
    print("Ist gelöst:", b.is_solved())


if __name__ == "__main__":
    main()
