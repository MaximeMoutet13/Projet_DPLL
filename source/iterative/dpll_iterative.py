from source.iterative.dpll_iterative_functions import update_clause_bis, update_literal_state_bis, is_satisfied, \
    is_unsatisfactory
from source.model import load, initialisation, display
from source.heuristics import literal_choice, no_heuristic, first_satisfy, first_fail
from source.iterative.backtrack import backtrack

from copy import copy


def dpll(literal, clause, heuristic, find_all_solutions=False):
    if len(clause) == 0:
        return True

    elif [] in clause:
        return False

    else:
        models = []
        literal_state, clause_state, clause_lenght = initialisation(literal, clause)
        running_literal = []
        lit = literal_choice(literal, literal_state, clause, clause_state, clause_lenght, heuristic)

        loop = True
        i = 1
        while loop:
            i += 1
            update_literal_state_bis(literal_state, lit)
            update_clause_bis(clause, clause_state, clause_lenght, lit)
            running_literal.append(lit)

            if is_satisfied(clause_lenght, clause_state):
                models.append(copy(running_literal))

                if not find_all_solutions:
                    return models

                else:
                    loop, literal_state, clause_state, clause_lenght, lit = backtrack(literal, literal_state, clause,
                                                                                      clause_state, clause_lenght,
                                                                                      running_literal)

            elif is_unsatisfactory(clause_lenght, clause_state):
                loop, literal_state, clause_state, clause_lenght, lit = backtrack(literal, literal_state, clause,
                                                                                  clause_state, clause_lenght,
                                                                                  running_literal)

            else:
                lit = literal_choice(literal, literal_state, clause, clause_state, clause_lenght, heuristic)

        return models


path_file = "../data/test1.txt"
f = open(path_file, "r")

literal, clause = load(f)

g = "../data/res1.txt"
display(literal, dpll(literal, clause, first_satisfy, find_all_solutions=True), g)