from source.first_literal_choice import mono_choice_bis


def first_satisfy(literal, literal_state, clause, clause_state):
    lit_occ = [[0, i] for i in range(len(literal))]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                if lit % 2 == 0:
                    if literal_state[lit] + literal_state[lit + 1] == 0:
                        lit_occ[lit][0] += 1
                else:
                    if literal_state[lit] + literal_state[lit - 1] == 0:
                        lit_occ[lit][0] += 1

    lit_occ.sort()
    for j in range(len(literal) - 1, -1, -1):
        lit = lit_occ[j][1]

        if literal_state[lit] == 0:
            return lit

    return "No first satisfy"


def first_fail(literal, literal_state, clause, clause_state):
    lit_occ = [[0, i] for i in range(len(literal))]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                if lit % 2 == 0:
                    if literal_state[lit] + literal_state[lit + 1] == 0:
                        lit_occ[lit][0] += 1
                else:
                    if literal_state[lit] + literal_state[lit - 1] == 0:
                        lit_occ[lit][0] += 1

    lit_occ.sort()
    for j in range(len(literal) - 1, -1, -1):
        lit = lit_occ[j][1]

        if lit % 2 == 0 and literal_state[lit + 1] == 0:
            return lit + 1

        elif lit % 2 == 1 and literal_state[lit - 1] == 0:
            return lit - 1

    return "No first fail"


def no_heuristic(literal, literal_state, clause, clause_state):
    for i in range(len(literal)):
        if i % 2 == 0:
            if literal_state[i] + literal_state[i + 1] == 0:
                return i
        else:
            if literal_state[i] + literal_state[i - 1] == 0:
                return i


def literal_choice(literal, literal_state, clause, clause_state, clause_lenght, heuristic):
    lit = mono_choice_bis(literal, literal_state, clause, clause_state, clause_lenght)
    if not isinstance(lit, int):
        lit = heuristic(literal, literal_state, clause, clause_state)
    return lit
