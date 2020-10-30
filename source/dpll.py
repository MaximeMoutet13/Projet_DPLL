from source.dpll_functions import simplify_clause, update_literal_state, is_satisfied
from source.model import load, initialisation
from source.heuristics import literal_choice


def dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False):
    lit = literal_choice(clause, clause_lenght, literal, literal_state)
    running_literal.append([lit, True])

    while len(clause) != 0:
        clause_1, clause_state_1, clause_lenght_1, literal_1 = simplify_clause(clause, clause_state, clause_lenght,
                                                                               literal, lit)
        update_literal_state(literal_state, running_literal)

        if is_satisfied(clause, clause_lenght, clause_state):
            if find_all_solutions == False:
                return running_literal

        else:
            [lit, v] = running_literal.pop()
            running_literal.append([lit, not (v)])

# literal, clause = load(file)
# literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)
#
# print(dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False))
