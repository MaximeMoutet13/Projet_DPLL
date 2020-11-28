from source.iterative.dpll_iterative_functions import update_clause, satisfy
from source.model import load, initialisation, display
from source.heuristics import literal_choice, no_heuristic, first_satisfy, first_fail
from source.iterative.backtrack import backtrack

from copy import copy
from time import time


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
        while loop is True:
            i += 1
            literal_state[lit] = 1
            update_clause(literal, clause_state, clause_lenght, lit)
            running_literal.append(lit)

            sat = satisfy(clause, clause_state, clause_lenght)
            if sat is True:
                models.append(copy(running_literal))

                if not find_all_solutions:
                    return models

                else:
                    next_lit, clause_state, clause_lenght = backtrack(literal, clause, literal_state, running_literal)
                    if next_lit is None:
                        loop = False
                    else:
                        lit = next_lit

            elif sat is False:
                next_lit, clause_state, clause_lenght = backtrack(literal, clause, literal_state, running_literal)
                if next_lit is None:
                    loop = False
                else:
                    lit = next_lit

            else:
                lit = literal_choice(literal, literal_state, clause, clause_state, clause_lenght, heuristic)

        return models, i


# path_file = "../data/pigeon_hole/7p6P.txt"
# f = open(path_file, "r")
#
# literal, clause = load(f)
#
# d = time()
# print(dpll(literal, clause, no_heuristic, find_all_solutions=True))
# print("time:", time() - d)
