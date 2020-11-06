__author__ = 'julesmichaud'
__filename__ = 'dpll_j.py'
__date__ = '06/11/20'

from source.dpll_functions import update_clause, update_literal_state, is_satisfied, is_unsatisfactory
from source.model import load, initialisation
from source.heuristics import literal_choice

def dpll(clause, clause_lenght, literal_state, clause_state, running_literal, literal, find_all_solutions=False):
    return 0

