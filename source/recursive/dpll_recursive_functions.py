from copy import copy


def update_clause(literal, clause_state, clause_lenght, lit):
    new_clause_state = copy(clause_state)
    new_clause_lenght = copy(clause_lenght)
    for c in literal[lit]:

            new_clause_lenght[c] = 0
            new_clause_state[c] = 1
    if lit % 2 == 0:
        for c in literal[lit + 1]:
            if new_clause_lenght[c] != 0:
                new_clause_lenght[c] -= 1
    else:
        for c in literal[lit - 1]:
            if new_clause_lenght[c] != 0:
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
