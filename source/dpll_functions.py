from copy import copy, deepcopy


def simplify_clause(clause, clause_state, clause_lenght, literal, lit):
    """Given a literal. Affect True to this literal and simplify clauses
    """
    new_clause = dict()
    new_clause_lenght = copy(clause_lenght)
    new_clause_state = copy(clause_state)
    new_literal = deepcopy(literal)

    for c, lits_in_clause in clause.items():
        new_clause[c] = lits_in_clause

        if lit in lits_in_clause:

            for other_lits in clause[c]:
                new_literal[other_lits].remove(c)

            new_clause[c] = set()
            new_clause_lenght[c] = 0
            new_clause_state[c] = 1

        elif (lit % 2 == 0) and (lit + 1 in lits_in_clause):
            new_clause[c].remove(lit + 1)
            new_clause_lenght[c] -= 1
            new_literal[lit + 1].remove(c)

        elif (lit % 2 == 1) and (lit - 1 in lits_in_clause):
            new_clause[c].remove(lit - 1)
            new_clause_lenght[c] -= 1
            new_literal[lit - 1].remove(c)

        if new_clause_lenght[c] == 0:
            del new_clause[c]

    return new_clause, new_clause_state, new_clause_lenght, new_literal


def update_literal_state(literal_state, lit):
    new_literal_state = copy(literal_state)
    new_literal_state[lit] = 1

    return new_literal_state


def is_satisfied(clause, clause_state):
    if len(clause) == 0:

        if clause_state == [1 for i in range(len(clause_state))]:
            return True
        else:
            return False

    else:
        return False


def is_unsatisfactory(clause_lenght, clause_state):
    for i in range(len(clause_lenght)):
        if clause_lenght[i] == 0 and clause_state[i] != 1:
            return True

    return False
