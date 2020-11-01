from source.dpll_functions import simplify_clause, update_literal_state, is_satisfied, is_unsatisfactory
from source.model import load, initialisation
from source.heuristics import literal_choice


def dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False):
    lit = literal_choice(clause, clause_lenght, literal, literal_state)
    running_literal.append([lit, True])

    dpll_tree = dict()
    dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))] = []

    while len(clause) != 0:
        clause_1, clause_state_1, clause_lenght_1, literal_1 = simplify_clause(clause, clause_state, clause_lenght,
                                                                               literal, running_literal[-1][0])

        literal_state_1 = update_literal_state(literal_state, running_literal[-1][0])

        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))].append(clause_1)
        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))].append(clause_state_1)
        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))].append(clause_lenght_1)
        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))].append(literal_1)
        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))].append(literal_state_1)

        if is_satisfied(clause_1, clause_state_1):
            if find_all_solutions is False:
                return running_literal

        elif is_unsatisfactory(clause_lenght_1, clause_state_1):
            lit, v = running_literal.pop()
            if lit % 2 == 0:
                running_literal.append([lit + 1, not v])
            else:
                running_literal.append([lit - 1, not v])

        else:
            lit = literal_choice(clause_1, clause_lenght_1, literal_1, literal_state_1)
            running_literal.append([lit, True])

        clause, clause_state, clause_lenght, literal, literal_state = clause_1, clause_state_1, clause_lenght_1, literal_1, literal_state_1
        dpll_tree[tuple(tuple(running_literal[i]) for i in range(len(running_literal)))] = []


path_file = "../data/test3.txt"
file = open(path_file, "r")
literal, clause = load(file)
file.close()

literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)

print(dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False))
