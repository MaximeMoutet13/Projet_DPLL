def update_clause_bis(clause, clause_state, clause_lenght, lit):
    for c, lits_in_clause in enumerate(clause):
        if lit in lits_in_clause:

            clause_lenght[c] = 0
            clause_state[c] = 1

        elif (lit % 2 == 0) and (lit + 1 in lits_in_clause) and (clause_lenght[c] != 0):

            clause_lenght[c] -= 1

        elif (lit % 2 == 1) and (lit - 1 in lits_in_clause) and (clause_lenght[c] != 0):

            clause_lenght[c] -= 1


def update_literal_state_bis(literal_state, lit):
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
