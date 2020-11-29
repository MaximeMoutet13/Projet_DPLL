def conjugate_literal(lit):
    if lit % 2 == 0:
        return lit + 1
    else:
        return lit - 1


def mono_literal(literal_state, clause, clause_lenght):
    for i in range(len(clause)):

        if clause_lenght[i] == 1:
            for lit in clause[i]:
                no_lit = conjugate_literal(lit)

                if literal_state[lit] + literal_state[no_lit] == 0:
                    return lit

    return "No unitary clause"


def pure_literal(literal, literal_state, clause, clause_state):
    lit_occurencies = [0 for i in range(len(literal))]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                no_lit = conjugate_literal(lit)

                if literal_state[lit] + literal_state[no_lit] == 0:
                    lit_occurencies[lit] += 1

    for i in range(int(len(literal) / 2)):

        if lit_occurencies[2 * i] != 0 and lit_occurencies[2 * i + 1] == 0 and literal_state[2 * i] == 0:
            return 2 * i

        elif lit_occurencies[2 * i + 1] != 0 and lit_occurencies[2 * i] == 0 and literal_state[2 * i + 1] == 0:
            return 2 * i + 1

    return "No pure literal"


def first_satisfy(literal, literal_state, clause, clause_state):
    n = len(literal)
    lit_occ = [[0, i] for i in range(n)]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                no_lit = conjugate_literal(lit)
                if literal_state[lit] + literal_state[no_lit] == 0:
                    lit_occ[lit][0] += 1

    lit_occ.sort()
    for j in range(n):
        lit = lit_occ[n - j - 1][1]

        if literal_state[lit] == 0:
            return lit

    return "No first satisfy"


def first_fail(literal, literal_state, clause, clause_state):
    n = len(literal)
    lit_occ = [[0, i] for i in range(n)]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                no_lit = conjugate_literal(lit)

                if literal_state[lit] + literal_state[no_lit] == 0:
                    lit_occ[lit][0] += 1

    lit_occ.sort()
    for j in range(n):
        lit = lit_occ[n - j - 1][1]
        no_lit = conjugate_literal(lit)

        if literal_state[no_lit] == 0:
            return no_lit

    return "No first fail"


def no_heuristic(literal, literal_state, clause, clause_state):
    for i in range(len(literal)):
        if i % 2 == 0:
            if literal_state[i] + literal_state[i + 1] == 0:
                return i
        else:
            if literal_state[i] + literal_state[i - 1] == 0:
                return i


def mono_choice(literal, literal_state, clause, clause_state, clause_lenght):
    lit = mono_literal(literal_state, clause, clause_lenght)
    if isinstance(lit, int):
        return lit

    lit = pure_literal(literal, literal_state, clause, clause_state)
    if isinstance(lit, int):
        return lit

    return "No first choice"


def literal_choice(literal, literal_state, clause, clause_state, clause_lenght, heuristic):
    lit = mono_choice(literal, literal_state, clause, clause_state, clause_lenght)
    if not isinstance(lit, int):
        lit = heuristic(literal, literal_state, clause, clause_state)
    return lit
