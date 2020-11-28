def pigeon_generator(n, m, f):
    """Pigeon hole problem generator, for n pigeons and m holes"""

    f = open(f, "w")
    d = {}
    nb_literal = 0

    """Variables and State creation"""
    for i in range(n):
        for j in range(m):
            f.write(str(nb_literal) + " ")
            d[(i, j)] = nb_literal
            nb_literal += 1
    f.write("\n")
    f.write("\n")

    """Clauses creation : a pigeon is in one and only one hole"""
    for i in range(n):
        for j in range(m):
            f.write(str(d[(i, j)]) + " ")
        f.write("\n")
        for j in range(m):
            for k in range(j + 1, m):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(i, k)]) + " ")
                f.write("\n")

    """Clauses creation : there is one pigeon max per hole"""
    for j in range(m):
        for i in range(n):
            for k in range(i + 1, n):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(k, j)]) + " ")
                f.write("\n")
    f.close()


f = "../../data/pigeon_hole/2p1P.txt"
pigeon_generator(2, 1, f)
