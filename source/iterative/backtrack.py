from source.model import initialisation
from source.iterative.dpll_iterative_functions import update_literal_state, update_clause


def backtrack(literal, literal_state, clause, clause_state, clause_lenght, running_literal):
    loop = True
    lit = None
    if len(running_literal) == 0:
        loop = False

    else:
        stop_backtrack = False,
        while stop_backtrack[0] is False:
            if len(running_literal) == 0:
                loop = False
                return loop, literal_state, clause_state, clause_lenght, None
            stop_backtrack = up_node(literal_state, running_literal)

        lit = stop_backtrack[1]
        if lit is None:
            loop = False
        else:
            literal_state, clause_state, clause_lenght = reconstruct(literal, literal_state, clause, running_literal, lit)
    return loop, literal_state, clause_state, clause_lenght, lit


def up_node(literal_state, running_literal):
    lit = running_literal.pop()
    if lit % 2 == 0:
        if literal_state[lit + 1] == 0:
            return True, lit + 1
    else:
        if literal_state[lit - 1] == 0:
            return True, lit - 1

    return False, lit


def reconstruct(literal, literal_state, clause, running_literal, lit):
    new_literal_state, new_clause_state, new_clause_lenght = initialisation(literal, clause)
    for i in range(len(running_literal)):
        current_literal = running_literal[i]
        update_literal_state(new_literal_state, current_literal)
        update_clause(literal, new_clause_state, new_clause_lenght, current_literal)
        if current_literal % 2 == 0:
            new_literal_state[current_literal + 1] = literal_state[current_literal + 1]
        else:
            new_literal_state[current_literal - 1] = literal_state[current_literal - 1]

    if lit % 2 == 0:
        new_literal_state[lit + 1] = literal_state[lit + 1]
    else:
        new_literal_state[lit - 1] = literal_state[lit - 1]

    return new_literal_state, new_clause_state, new_clause_lenght
