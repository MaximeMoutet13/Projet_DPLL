from source.recursive.dpll_recursive_functions import update_clause, update_literal_state
from source.model import load, initialisation
from source.heuristics import no_heuristic, first_fail, first_satisfy

file_path = "../../../data/test1.txt"
f = open(file_path, "r")
f_literals, f_clauses = load(f)


def dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght=None, literals_state=None, clauses_state=None, running_literals=None, find_all_solutions=False):
    """SECOND VERSION"""
    models = list()

    """Initialisation"""
    if not clauses_state:
        if affichage:print("pass init")
        models = list()
        literals_state, clauses_state, clauses_lenght = initialisation(literals, clauses)
        running_literals = list()
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
        if affichage:print("pass base", running_literals)
        return [running_literals]

    """Induction"""
    # l = mono_choice(literals, literals_state, clauses, clauses_state, clauses_lenght)
    # if isinstance(l, int):
    #     """Mono-litteral or monotone litteral"""
    #     if affichage:print("pass mono-litt", l, clauses_state, literals_state, clauses_lenght)
    #     literals_state = update_literal_state(literals_state, l)
    #     running_literals = [l] + running_literals
    #     clauses_state, clauses_lenght = update_clause(clauses, clauses_state, clauses_lenght, l)
    #     if all(state == 0 for state in clauses_state):
    #         if affichage:print("pass new model", clauses_state, literals_state)
    #         # if affichage:print(dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals))
    #         for i in dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals):
    #             models += i
    #     else:
    #         if affichage: print("fin recursion :", dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals))
    #         return [dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght, literals_state, clauses_state, running_literals)]
    if True == False : return "a"
    else:
        """Heuristic choice of a litteral"""
        if affichage: print("pass heuristic", clauses_state, literals_state, clauses_lenght)
        l_1 = heuristic_choice(literals, literals_state, clauses, clauses_state)
        print(l_1)
        literals_state_1 = update_literal_state(literals_state, l_1)
        running_literals_1 = [l_1] + running_literals
        clauses_state_1, clauses_lenght_1 = update_clause(clauses, clauses_state, clauses_lenght, l_1)
        if l_1 % 2 == 0:
            l_2 = l_1 + 1
        else:
            l_2 = l_1 - 1
        literals_state_2 = update_literal_state(literals_state, l_2)
        running_literals_2 = [l_2] + running_literals
        clauses_state_2, clauses_lenght_2 = update_clause(clauses, clauses_state, clauses_lenght, l_2)
        if (state == 0 for state in clauses_state):
            if affichage:print("pass new model", clauses_state, literals_state)
            if affichage:print(dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_1, literals_state_1, clauses_state_1, running_literals_1),dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_2, literals_state_2, clauses_state_2, running_literals_2))
            models += dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_1, literals_state_1, clauses_state_1, running_literals_1)
            models += dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_2, literals_state_2, clauses_state_2, running_literals_2)
        else:
            if affichage:print("end recursion :", dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_1, literals_state_1, clauses_state_1, running_literals_1), dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_2, literals_state_2, clauses_state_2, running_literals_2))
            return [dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_1, literals_state_1, clauses_state_1, running_literals_1), dpll_recursif(heuristic_choice, clauses, literals, clauses_lenght_2, literals_state_2, clauses_state_2, running_literals_2)]

    return models


affichage = 0
print(dpll_recursif(first_fail, f_clauses, f_literals))
