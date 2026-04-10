# board.py
# ------------------------------------------
# Author: Michael Blaich
# Datum: 21.03.2025
# Beschreibung: Template für die Implementierung des A* Algorithmus
# ------------------------------------------
import heapq
from collections import deque
from board import Board
from typing import Optional


class Node:
    """
    Repräsentiert einen Knoten im Suchbaum für den A*-Algorithmus.

    Attribute:
        board (Board): Der aktuelle Zustand des Spielfelds.
        parent (Node, optional): Der Vorgängerknoten (Elternknoten) in der Pfadsuche.
        g (int): Die bisherigen Pfadkosten von Start bis zu diesem Knoten.
        h (int): Der geschätzte Abstand zum Zielzustand (Heuristik).
        f (int): Die geschätzten Gesamtkosten f = g + h.
    """

    def __init__(self, board: Board, parent: 'Node' = None, g=0):
        self.board = board
        self.parent = parent
        self.g = g  # Pfadkosten
        self.h = board.h2()  # Heuristikwert
        self.f = self.g + self.h  # f = g + h

    def __lt__(self, other):
        """
        Vergleichsmethode für die Prioritätswarteschlange.
        Knoten mit kleineren f-Werten werden bevorzugt.
        """
        return self.f < other.f  # Für PriorityQueue


def reconstruct_path(node: Node) -> deque[Board]:
    """
    Rekonstruiert den Pfad vom Startzustand bis zum Zielzustand.
    """
    path = deque()

    # Durclaufe aller Knoten mit Eltern Knoten
    while node.parent is not None:

        # Board des aktuellen Knotens vorne in path einfügen
        path.appendleft(node.board)
        node = node.parent
    
    # Am schluss noch den Startknoten vorne einfügen   
    path.appendleft(node.board)

    return path


def a_star(start_board: Board) -> Optional[deque[Board]]:
    """
    Führt den A*-Algorithmus zur Lösung des 8-Puzzle-Problems aus.
    Es empfiehlt sich hierbei heapq für die open_list und set() für die
    closed_list zu verwenden.
    """
    open_list = []
    heapq.heappush(open_list, Node(start_board))
    closed_list = set()

    # Solange noch Knoten in der open_list sind:
    while len(open_list) > 0:
        # 1. Knoten mit geringstem f-Wert aus open_list holen
        current_node = heapq.heappop(open_list)

        # 2. Prüfen ob aktueller Knoten schon das Ziel-Board enthält
        if current_node.board.is_solved():
            return reconstruct_path(current_node)

        # 3. Aktuelles Board zur close_list hinzufügen
        closed_list.add(current_node.board)


        # 4. Durchlaufe ale Möglichen Folge-Boards des aktuelen Boards
        for board in current_node.board.possible_actions():

            # Falls das board bereits in der closed_list ist überspringe es
            if board in closed_list:
                continue;
            
            # Ansonsten erstelle für das board einen neuen Node und sortiere es in den Heap ein
            new_node = Node(board, current_node, current_node.g + 1)
            heapq.heappush(open_list, new_node)


    return None  # Kein Pfad gefunden
