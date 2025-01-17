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


def display(literal, models, file):
    f = open(file, "w")

    for i in range(int(len(literal) / 2)):
        f.write(chr(i + 97) + " ")
    f.write("\n" + "\n")

    for m in models:
        line = ["_" for i in range(int(len(literal) / 2))]

        for x in m:
            if x % 2 == 0:
                line[int(x / 2)] = 1
            else:
                line[int((x - 1) / 2)] = 0

        for s in line:
            f.write(str(s) + " ")
        f.write("\n")
    f.close()


def initialisation(literal, clause):
    """Construct needed structures to run DPLL algorithm
    """

    literal_state = [0 for i in range(len(literal))]
    clause_state = [0 for i in range(len(clause))]
    clause_lenght = [len(clause[i]) for i in range(len(clause))]

    return literal_state, clause_state, clause_lenght


def count_models(literal, model):
    n = int(len(literal) / 2)

    if model is True:
        return 2 ** n

    else:
        res = 0
        for mod in model:
            m = len(mod)
            free_lit = n - m
            res += 2 ** free_lit

        return res
