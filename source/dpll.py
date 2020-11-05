from source.dpll_functions import update_clause, update_literal_state, is_satisfied, is_unsatisfactory
from source.model import load, initialisation
from source.heuristics import literal_choice


def dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False):
    lit = literal_choice(clause, clause_lenght, literal, literal_state)
    running_literal.append([lit, True])

    stop_algorithm = False

    while stop_algorithm != True:
        clause_state_1, clause_lenght_1 = update_clause(clause, clause_state, clause_lenght, running_literal[-1][0])

        literal_state_1 = update_literal_state(literal_state, running_literal[-1][0])

        if is_satisfied(clause_lenght_1, clause_state_1):
            if find_all_solutions is False:
                return running_literal

        elif is_unsatisfactory(clause_lenght_1, clause_state_1):

            lit, v = running_literal.pop()
            if lit % 2 == 0 and literal_state_1[lit + 1] == 0:
                running_literal.append([lit + 1, v])
            elif lit % 2 == 1 and literal_state_1[lit - 1] == 0:
                running_literal.append([lit - 1, v])
            else:
                lit = running_literal.pop()
                running_literal.append([lit, True])
        else:
            lit = literal_choice(clause, clause_lenght_1, literal, literal_state_1)
            running_literal.append([lit, True])

        clause_state, clause_lenght, literal_state = clause_state_1, clause_lenght_1, literal_state_1


file_path = "../data/test.txt"
f = open(file_path, "r")
literal, clause = load(f)
literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)

print(dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal))
