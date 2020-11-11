from source.model import initialisation
from source.iterative.dpll_iterative_functions import update_literal_state, update_clause


def conjugate_literal(lit):
    if lit % 2 == 0:
        return lit + 1
    else:
        return lit - 1


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
        literal_state, clause_state, clause_lenght = reconstruct(literal, literal_state, clause, running_literal, lit)
    return loop, literal_state, clause_state, clause_lenght, lit


def up_node(literal_state, running_literal):
    lit = running_literal.pop()
    not_lit = conjugate_literal(lit)

    if literal_state[not_lit] == 0:
        return True, not_lit

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






def backtrack_better(literal, clause, literal_state, clause_state, clause_lenght, running_literal):
    go_up = True
    while go_up:
        current_literal = running_literal.pop()
        no_current_literal = conjugate_literal(current_literal)

        reconstruct_better(literal, clause, literal_state, clause_state, clause_lenght, current_literal)

        if literal_state[no_current_literal] == 0:
            return no_current_literal

        else:
            if len(running_literal) == 0:
                return None
            else:
                literal_state[current_literal] = 0
                literal_state[no_current_literal] = 0


def reconstruct_better(literal, clause, literal_state, clause_state, clause_lenght, lit):
    no_lit = conjugate_literal(lit)

    visited_clauses = set()

    for c in literal[lit]:
        visited_clauses.add(c)
        clause_state[c] = 0
        clause_lenght[c] = 1

        for p in clause[c]:
            if p != lit:

                if literal_state[p] == 1:

                    if p == no_lit:
                        clause_lenght[c] += 1

                    else:
                        clause_state[c] = 1
                        clause_lenght[c] = 0
                        return

                else:
                    clause_lenght[c] += 1

    for c in literal[no_lit]:
        if not (c in visited_clauses):
            if clause_state[c] == 0:
                clause_lenght[c] += 1
