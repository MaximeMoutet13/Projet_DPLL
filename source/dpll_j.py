from source.dpll_functions import update_clause, update_literal_state, is_satisfied, is_unsatisfactory
from source.model import load, initialisation
from source.heuristics import literal_choice

file_path = "../data/test.txt"
f = open(file_path, "r")
f_literals, f_clauses = load(f)


def dpll(heuristic_choice, clauses, literals, clauses_lenght=None, literals_state=None, clauses_state=None, running_literals=None, find_all_solutions=False):
    """SECOND VERSION"""

    """Initialisation"""
    if not clauses_state:
        models = list()
        running_literals = list()
        literals_state, clauses_state, clauses_lenght, running_literals = initialisation(literals, clauses)
        if not clauses:
                return []

    """Base"""
    nb_empty_clauses = 0
    for i in range(len(clauses)):
        if clauses_lenght[i] == 0:
            nb_empty_clauses += 1
            if clauses_state[i] == 0:
                return []
    if nb_empty_clauses == len(clauses):
        return clauses_state

    """Induction"""
    l = literal_choice(clauses, clauses_lenght, literals, literals_state)
    if l != None:
        """Mono-litteral or monotone litteral"""
        literals_state = update_literal_state(literals_state, l)
        running_literals = [l] + running_literals
        clauses_state, clauses_lenght = update_clause(clauses, clauses_state, clauses_lenght, l)
        if (state == 0 for state in clauses_state):
            models += [i for i in dpll(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals)]
        else:
            return dpll(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals)

    else:
        """Heuristic choice of a litteral"""
        l_1 = heuristic_choice(clauses, clauses_lenght, literals, literals_state)
        literals_state_1 = update_literal_state(literals_state, l_1)
        running_literals_1 = [l_1] + running_literals
        clauses_state_1, clauses_lenght_1 = update_clause(clauses, clauses_state, clauses_lenght, l_1)
        if l % 2 == 0:
            l_2 = l_1 + 1
        else:
            l_2 = l_1 - 1
        literals_state_2 = update_literal_state(literals_state, l_2)
        running_literals_2 = [l_2] + running_literals
        clauses_state_2, clauses_lenght_2 = update_clause(clauses, clauses_state, clauses_lenght, l_2)
        if (state == 0 for state in clauses_state):
            models += [i for i in dpll(heuristic_choice, clauses, literals, clauses_lenght_1, literals_state_1, clauses_state_1, running_literals_1)]
            models += [i for i in dpll(heuristic_choice, clauses, literals, clauses_lenght_2, literals_state_2, clauses_state_2, running_literals_2)]
        else:
            return dpll(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals)

    return models


dpll(literal_choice, f_clauses, f_literals)