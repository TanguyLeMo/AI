"""
Aufgabe 4 – Packungsproblem als CSP
Variablen: (x, y, gedreht) je Rechteck | Constraints: keine Überlappung
"""

from constraint import Problem

GRID_BREITE = 8
GRID_HOEHE  = 7

# (breite, hoehe) der 6 kleinen Rechtecke
RECHTECKE = [
    (6, 4),  # 0
    (8, 1),  # 1
    (4, 1),  # 2
    (5, 2),  # 3
    (2, 2),  # 4
    (3, 2),  # 5
]


def berechne_positionen(breite, hoehe):
    """Alle gültigen (x, y, gedreht)-Platzierungen für ein Rechteck im Grid.

    Iteriert alle (x, y)-Startpunkte bei denen das Rechteck noch ins Grid passt.
    Wiederholt das Ganze mit getauschten Maßen für die gedrehte Variante.
    """
    positionen = []

    for x in range(GRID_BREITE - breite + 1):
        for y in range(GRID_HOEHE - hoehe + 1):
            positionen.append((x, y, False))

    # Gedreht nur wenn kein Quadrat (sonst Duplikate)
    if breite != hoehe:
        for x in range(GRID_BREITE - hoehe + 1):
            for y in range(GRID_HOEHE - breite + 1):
                positionen.append((x, y, True))

    return positionen


def keine_ueberlappung(p1, p2, r1, r2):
    """True wenn die zwei platzierten Rechtecke sich nicht überlappen.

    Berechnet die tatsächlichen Maße je nach Orientierung, dann prüft ob
    die Rechtecke auf der x- oder y-Achse komplett getrennt sind (Separating Axis).
    """
    x1, y1, g1 = p1
    x2, y2, g2 = p2

    b1 = r1[1] if g1 else r1[0]
    h1 = r1[0] if g1 else r1[1]
    b2 = r2[1] if g2 else r2[0]
    h2 = r2[0] if g2 else r2[1]

    return (x1 + b1 <= x2) or (x2 + b2 <= x1) or \
           (y1 + h1 <= y2) or (y2 + h2 <= y1)


def mache_constraint(r1, r2):
    """Gibt eine Constraint-Funktion für ein konkretes Rechteck-Paar zurück.

    r1/r2 werden als Parameter der äußeren Funktion eingefroren, damit die
    innere Funktion immer das richtige Paar referenziert (Closure).
    """
    def constraint(p1, p2):
        return keine_ueberlappung(p1, p2, r1, r2)
    return constraint


def loese():
    """Baut das CSP auf und gibt die erste gefundene Lösung zurück.

    Fügt für jedes Rechteck seine möglichen Positionen als Domäne ein,
    dann für jedes Paar eine Überlappungs-Constraint (n*(n-1)/2 Paare).
    """
    problem = Problem()

    for i, (b, h) in enumerate(RECHTECKE):
        problem.addVariable(i, berechne_positionen(b, h))

    for i in range(len(RECHTECKE)):
        for j in range(i + 1, len(RECHTECKE)):
            problem.addConstraint(
                mache_constraint(RECHTECKE[i], RECHTECKE[j]),
                [i, j]
            )

    return problem.getSolution()


def drucke_grid(loesung):
    """Gibt die Lösung als ASCII-Grid aus, jedes Rechteck mit seiner Nummer.

    Füllt ein leeres Grid mit '.' und trägt für jede belegte Zelle
    die Rechteck-Nummer ein, dann zeilenweise ausgeben.
    """
    if loesung is None:
        print("Keine Lösung gefunden!")
        return

    grid = [['.' for _ in range(GRID_BREITE)] for _ in range(GRID_HOEHE)]

    for i, (b, h) in enumerate(RECHTECKE):
        x, y, gedreht = loesung[i]
        bx = h if gedreht else b
        hy = b if gedreht else h
        for dx in range(bx):
            for dy in range(hy):
                grid[y + dy][x + dx] = str(i)

    for zeile in grid:
        print(' '.join(zeile))


def main():
    """Löst das Packungsproblem und gibt das Ergebnis aus."""
    print("Löse Packungsproblem ...")
    loesung = loese()
    drucke_grid(loesung)


if __name__ == "__main__":
    main()
