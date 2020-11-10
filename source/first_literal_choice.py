def mono_literal(literal_state, clause, clause_lenght):
    for i in range(len(clause)):

        if clause_lenght[i] == 1:
            for lit in clause[i]:

                if literal_state[lit] == 0:
                    return lit

    return "No unitary clause"


def pure_literal(literal, literal_state, clause, clause_state):
    lit_occurencies = [0 for i in range(len(literal))]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                if literal_state[lit] == 0:
                    lit_occurencies[lit] += 1

    for i in range(int(len(literal) / 2)):

        if lit_occurencies[2 * i] != 0 and lit_occurencies[2 * i + 1] == 0 and literal_state[2 * i] == 0:
            return 2 * i

        elif lit_occurencies[2 * i + 1] != 0 and lit_occurencies[2 * i] == 0 and literal_state[2 * i + 1] == 0:
            return 2 * i + 1

    return "No pure literal"


def mono_choice(literal, literal_state, clause, clause_state, clause_lenght):
    lit = mono_literal(literal_state, clause, clause_lenght)
    if isinstance(lit, int):
        return lit

    lit = pure_literal(literal, literal_state, clause, clause_state)
    if isinstance(lit, int):
        return lit

    return "No first choice"


def mono_literal_bis(literal_state, clause, clause_lenght):
    for i in range(len(clause)):

        if clause_lenght[i] == 1:
            for lit in clause[i]:
                if lit % 2 == 0 and literal_state[lit] + literal_state[lit + 1] == 0:
                    return lit
                elif lit % 2 == 1 and literal_state[lit] + literal_state[lit - 1] == 0:
                    return lit

    return "No unitary clause"


def pure_literal_bis(literal, literal_state, clause, clause_state):
    lit_occurencies = [0 for i in range(len(literal))]

    for i in range(len(clause)):
        if clause_state[i] == 0:

            for lit in clause[i]:
                if lit % 2 == 0 and literal_state[lit] + literal_state[lit + 1] == 0:
                    lit_occurencies[lit] += 1
                elif lit % 2 == 1 and literal_state[lit] + literal_state[lit - 1] == 0:
                    lit_occurencies[lit] += 1

    for i in range(int(len(literal) / 2)):

        if lit_occurencies[2 * i] != 0 and lit_occurencies[2 * i + 1] == 0 and literal_state[2 * i] == 0:
            return 2 * i

        elif lit_occurencies[2 * i + 1] != 0 and lit_occurencies[2 * i] == 0 and literal_state[2 * i + 1] == 0:
            return 2 * i + 1

    return "No pure literal"


def mono_choice_bis(literal, literal_state, clause, clause_state, clause_lenght):
    lit = mono_literal_bis(literal_state, clause, clause_lenght)
    if isinstance(lit, int):
        return lit

    lit = pure_literal_bis(literal, literal_state, clause, clause_state)
    if isinstance(lit, int):
        return lit

    return "No first choice"

