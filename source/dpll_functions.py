from copy import copy, deepcopy


def simplify_clause(clause, clause_state, clause_lenght, literal, lit):
    """Given a literal. Affect True to this literal and simplify clauses
    """
    simplified_clause = dict()
    simplified_clause_lenght = copy(clause_lenght)
    simplified_clause_state = copy(clause_state)
    simplified_literal = deepcopy(literal)

    for c, lits_in_clause in clause.items():
        simplified_clause[c] = lits_in_clause

        if lit in lits_in_clause:

            for other_lits in clause[c]:
                simplified_literal[other_lits].remove(c)

            simplified_clause[c] = set()
            simplified_clause_lenght[c] = 0

        elif (lit % 2 == 0) and (lit + 1 in lits_in_clause):
            simplified_clause[c].remove(lit + 1)
            simplified_clause_lenght[c] -= 1
            simplified_literal[lit + 1].remove(c)

        elif (lit % 2 == 1) and (lit - 1 in lits_in_clause):
            simplified_clause[c].remove(lit - 1)
            simplified_clause_lenght[c] -= 1
            simplified_literal[lit - 1].remove(c)

        if simplified_clause_lenght[c] == 0:
            del simplified_clause[c]
            simplified_clause_state[c] = 1

    return simplified_clause, simplified_clause_state, simplified_clause_lenght, simplified_literal


def update_literal_state(literal_state, lit):
    literal_state[lit] = 1

    if lit % 2:
        literal_state[lit + 1] = 1
    else:
        literal_state[lit - 1] = 1


def is_satisfied(clause, clause_lenght, clause_state):
    if len(clause) == 0:

        if clause_state == [1 for i in range(len(clause_lenght))]:
            return True
        else:
            return False

    else:
        for l in clause_lenght:
            if l == 0 and clause_state == 0:
                return False
