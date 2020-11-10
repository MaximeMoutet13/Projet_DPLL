def update_clause(literal, clause_state, clause_lenght, lit):
    for c in literal[lit]:

            clause_lenght[c] = 0
            clause_state[c] = 1
    if lit % 2 == 0:
        for c in literal[lit + 1]:
            if clause_lenght[c] != 0:
                clause_lenght[c] -= 1
    else:
        for c in literal[lit - 1]:
            if clause_lenght[c] != 0:
                clause_lenght[c] -= 1


def update_literal_state(literal_state, lit):
    literal_state[lit] = 1


def is_satisfied(clause_lenght, clause_state):
    if clause_lenght == [0 for i in range(len(clause_lenght))]:

        if clause_state == [1 for i in range(len(clause_lenght))]:
            return True
        else:
            return False

    else:
        return False


def is_unsatisfactory(clause_lenght, clause_state):
    for i in range(len(clause_lenght)):
        if clause_lenght[i] == 0 and clause_state[i] == 0:
            return True

    return False
