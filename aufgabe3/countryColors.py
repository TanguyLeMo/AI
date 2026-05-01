from constraint import *

Germany = {
    "Baden-Württemberg": ["Bayern", "Hessen", "Rheinland-Pfalz"],
    "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
    "Saarland": ["Rheinland-Pfalz"],
    "Rheinland-Pfalz": ["Saarland", "Hessen", "Baden-Württemberg", "Nordrhein-Westfalen"],
    "Hessen": ["Rheinland-Pfalz", "Nordrhein-Westfalen", "Niedersachsen", "Thüringen", "Bayern", "Baden-Württemberg"],
    "Thüringen": ["Bayern", "Sachsen", "Sachsen-Anhalt", "Niedersachsen", "Hessen"],
    "Nordrhein-Westfalen": ["Rheinland-Pfalz", "Hessen", "Niedersachsen"],
    "Niedersachsen": ["Nordrhein-Westfalen", "Hessen", "Thüringen", "Sachsen-Anhalt", "Brandenburg", "Mecklenburg-Vorpommern", "Schleswig-Holstein", "Hamburg", "Bremen"],
    "Sachsen-Anhalt": ["Niedersachsen", "Brandenburg", "Sachsen", "Thüringen"],
    "Sachsen": ["Bayern", "Thüringen", "Sachsen-Anhalt", "Brandenburg"],
    "Brandenburg": ["Mecklenburg-Vorpommern", "Sachsen-Anhalt", "Sachsen", "Niedersachsen"],
    "Mecklenburg-Vorpommern": ["Schleswig-Holstein", "Niedersachsen", "Brandenburg"],
    "Schleswig-Holstein": ["Niedersachsen", "Hamburg", "Mecklenburg-Vorpommern"],
    "Hamburg": ["Schleswig-Holstein", "Niedersachsen"],
    "Bremen": ["Niedersachsen"],
    "Berlin": ["Brandenburg"]
}



def solve():
    problem =Problem()
    colours = ["Green", "Blue", "Red", "Yellow"]
    problem.addVariables(Germany.keys(),colours)    
    for state, neighbours in Germany.items():
        for neighbour in neighbours:
            problem.addConstraint(lambda colour1, colour2: colour1 != colour2, [state, neighbour])
    return problem.getSolutions()


def main():
    solution = solve()[0]
    print(solution)

    passt = True
    for state, colour in solution.items():
        for neighbor in Germany[state]:
            if colour == solution[neighbor]:
                print(f"fehler gefunden: zwischen {state}{neighbor}")
                passt = False
    if passt:
        print("All good")
        

if __name__ == "__main__":
    main()