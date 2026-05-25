from constraint import *

def solve():
    problem =Problem()
    variables = ["Maier","Huber","Muller","Schmidt","Deutsch","Englisch", "Mathe","Physik"]
    problem.addVariables(variables,[1,2,3,4])
    problem.addConstraint(AllDifferentConstraint(), variables[:4])
    problem.addConstraint(AllDifferentConstraint(), variables[4:])
    problem.addConstraint(lambda Maier: Maier != 4, ["Maier"])
    problem.addConstraint(lambda Muller, Deutsch: Muller == Deutsch, ["Muller", "Deutsch"])
    problem.addConstraint(lambda Schmidt, Müller: abs(Schmidt + Müller) >= 2, ["Schmidt", "Muller"])
    problem.addConstraint(lambda Maier, Mathe  : Maier == Mathe, ["Maier", "Mathe"])
    problem.addConstraint(lambda Physik: Physik == 4, ["Physik"] )
    problem.addConstraint(lambda Deutsch, Englisch: (Deutsch != 1) and Englisch != 1, ["Deutsch", "Englisch"])
    tmp =  problem.getSolution()
    return tmp


def main():
    solutions = solve()
    print(solutions)
        

if __name__ == "__main__":
    main()