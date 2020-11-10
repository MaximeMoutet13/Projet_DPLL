from source.dpll_functions import update_clause_bis, update_literal_state_bis, is_satisfied, is_unsatisfactory
from source.model import load, initialisation
from source.first_literal_choice import mono_choice
from source.heuristics import *

from copy import copy

def dpll_backtrack(literal_state, running_literal):
    if len(running_literal) == 0:
        return True, None

    lit = running_literal.pop()

    if lit % 2 == 0:
        if literal_state[lit + 1] == 0:
            return True, lit + 1
    else:
        if literal_state[lit - 1] == 0:
            return True, lit - 1

    return False, None


def dpll_backtracj_bis(literal, clause, running_literal):
    literal_state, clause_state, clause_lenght, useless = initialisation(literal, clause)
    for i in range(len(running_literal)):
        lit = running_literal[i]
        update_literal_state_bis(literal_state, lit)
        update_clause_bis(clause, clause_state, clause_lenght, lit)

    print(literal_state)


def dpll(literal, clause, heuristic, find_all_solutions=False):
    if len(clause) == 0:
        return True

    elif [] in clause:
        return False

    else:
        models = []

        literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)

        lit = mono_choice(literal, literal_state, clause, clause_state, clause_lenght)
        if not isinstance(lit, int):
            lit = heuristic(literal, literal_state, clause, clause_state)

        running_literal.append(lit)
        
        loop = True
        while loop:
            update_literal_state_bis(literal_state, lit)
            update_clause_bis(clause, clause_state, clause_lenght, lit)

            if is_satisfied(clause_lenght, clause_state):
                models.append(copy(running_literal))

                if not find_all_solutions:
                    return models
                else:
                    back_track = False, False
                    while back_track[0] is False:
                        back_track = dpll_backtrack(literal_state, running_literal)
                    dpll_backtracj_bis(literal, clause, running_literal)
                    lit = back_track[1]
                    if lit is None:
                        loop = False
                    running_literal.append(lit)

            elif is_unsatisfactory(clause_lenght, clause_state):
                back_track = [False, False]
                while back_track[0] is False:
                    back_track = dpll_backtrack(literal_state, running_literal)

                dpll_backtracj_bis(literal, clause, running_literal)
                lit = back_track[1]
                if lit is None:
                    loop = False
                running_literal.append(lit)

            else:
                lit = mono_choice(literal, literal_state, clause, clause_state, clause_lenght)
                if not isinstance(lit, int):
                    lit = heuristic(literal, literal_state, clause, clause_state)

                running_literal.append(lit)
        return models


path_file = "../data/test2.txt"
f = open(path_file, "r")

literal, clause = load(f)
print(dpll(literal, clause, first_satisfy, find_all_solutions=True))
