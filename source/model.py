def load(f):
    """Load the file f and put the data in dictionaries

    literal_without_str: The key is the integer associated to the literal an the value is the index of clauses where the
        literal appears. Even integers are for positive literals, odd integers are for negative literals.

    clause: Key is the index of the clause. Value is a list of literals that appears in the clause
    """

    txt = [line.split() for line in f]

    literal = dict()  # this is a step to easily construct clause
    for i, lit in enumerate(txt[0]):
        literal[lit] = [2 * i, []]
        literal["-" + lit] = [2 * i + 1, []]

    clause = [[] for i in range(len(txt[2:]))]

    for i in range(len(txt[2:])):
        for j in txt[2 + i]:
            clause[i].append(literal[j][0])
            literal[j][1].append(i)

    literal_list = [[] for i in range(len(2 * txt[0]))]
    for key, values in literal.items():
        literal_list[values[0]] = values[1]

    return literal_list, clause


def initialisation(literal, clause):
    """Construct needed structures to run DPLL algorithm
    """

    literal_state = [0 for i in range(len(literal))]
    clause_state = [0 for i in range(len(clause))]
    clause_lenght = [len(clause[i]) for i in range(len(clause))]

    return literal_state, clause_state, clause_lenght
