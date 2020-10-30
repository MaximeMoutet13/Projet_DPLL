def mono_literal(clause, clause_lenght):
    """ Mono-literal heuristic
    """
    for i in range(len(clause_lenght)):

        if clause_lenght[i] == 1:
            return clause[i]

    return "No unitary clause"


def pure_literal(literal):
    """Pure literal heuristic
    """
    for i in range(int(len(literal) / 2)):

        if len(literal[2 * i]) == 0 and len(literal[2 * i + 1]) != 0:
            return literal[2 * i + 1]
        elif len(literal[2 * i]) != 0 and len(literal[2 * i + 1]) == 0:
            return literal([2 * i])
        else:
            continue

    return "No pure literal"


def literal_choice(clause, clause_lenght, literal, literal_state):
    """Choose the best literal to use in DPLL step. Assume that there is still non affected literals
    """
    lit = mono_literal(clause, clause_lenght)
    if isinstance(lit, int):
        return lit

    lit = pure_literal(literal)
    if isinstance(lit, int):
        return lit

    for i, lit in enumerate(literal_state):
        if lit == 0:
            return i
