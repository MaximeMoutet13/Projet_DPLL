from copy import copy


def update_clause(clause, clause_state, clause_lenght, lit):
    new_clause_state = copy(clause_state)
    new_clause_lenght = copy(clause_lenght)

    for c, lits_in_clause in enumerate(clause):
        if lit in lits_in_clause:

            new_clause_lenght[c] = 0
            new_clause_state[c] = 1

        elif (lit % 2 == 0) and (lit + 1 in lits_in_clause) and (new_clause_lenght[c] != 0):

            new_clause_lenght[c] -= 1

        elif (lit % 2 == 1) and (lit - 1 in lits_in_clause) and (new_clause_lenght[c] != 0):

            new_clause_lenght[c] -= 1

    return new_clause_state, new_clause_lenght


def update_literal_state(literal_state, lit):
    new_literal_state = copy(literal_state)
    new_literal_state[lit] = 1
    if lit % 2 == 0:
        new_literal_state[lit+1] = 0
    else :
        new_literal_state[lit-1] = 0
    return new_literal_state
