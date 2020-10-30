from heuristics import literal_choice


def simplify_clause(clause, clause_state, clause_lenght, lit):
    """Given a literal. Affect True to this literal and simplify clauses
    """
    for c, lits in clause.items():

        if lit in lits:
            del clause[c]
            clause_state[c] = 1
            clause_lenght[c] = 0

        elif (lit % 2 == 0) and (lit + 1 in lits):
            clause[c].remove(lit + 1)
            clause_lenght[c] -= 1

            if clause_lenght[c] == 0:
                del clause[c]

        elif (lit % 2 == 1) and (lit - 1 in lits):
            clause[c].remove(lit - 1)
            clause_lenght[c] -= 1
            if clause_lenght[c] == 0:
                del clause[c]

def update(clause, clause_lenght, literal, literal_state, clause_state, running_literal):
    lit = literal_choice(clause, clause_lenght, literal, literal_state)
    running_literal.append([lit, True])

    simplify_clause(clause, clause_state, clause_lenght, lit)

    literal_state[lit] = 1


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


