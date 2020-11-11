def queens_generator(n, f):
    """Queens problem generator, for n queens on a n x n chessboard"""

    f = open(f, "w")
    d = {}
    state = {}

    """Variables and State creation"""
    nb_literal = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                f.write(str(nb_literal) + " ")
                d[(i, j, k)] = nb_literal
                for i_2 in range(n):
                    for j_2 in range(n):
                        for k_2 in range(n):
                            state[frozenset([(i, j, k), (i_2, j_2, k_2)])] = False
                nb_literal += 1
    f.write("\n")
    f.write("\n")

    """Clauses creation : a queen is in one and only one position on the board"""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                f.write(str(d[(i, j, k)]) + " ")
        f.write("\n")
        for j in range(n):
            for k in range(n):
                for j_2 in range(n):
                    for k_2 in range(n):
                        if (j, k) != (j_2, k_2) and not state[frozenset([(i, j, k), (i, j_2, k_2)])]:
                            f.write("-" + str(d[(i, j, k)]) + " ")
                            f.write("-" + str(d[(i, j_2, k_2)]) + " ")
                            f.write("\n")
                            state[frozenset([(i, j, k), (i, j_2, k_2)])] = True

    """Clauses creation : there is one queen max per column"""
    # f.write("column \n")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for i_2 in range(i + 1, n):
                    for j_2 in range(n):
                        if not state[frozenset([(i, j, k), (i_2, j_2, k)])]:
                            f.write("-" + str(d[(i, j, k)]) + " ")
                            f.write("-" + str(d[(i_2, j_2, k)]) + " ")
                            f.write("\n")
                            state[frozenset([(i, j, k), (i_2, j_2, k)])] = True

    """Clauses creation : there is one queen max per line"""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for i_2 in range(i + 1, n):
                    for k_2 in range(n):
                        if not state[frozenset([(i, j, k), (i_2, j, k_2)])]:
                            f.write("-" + str(d[(i, j, k)]) + " ")
                            f.write("-" + str(d[(i_2, j, k_2)]) + " ")
                            f.write("\n")
                            state[frozenset([(i, j, k), (i_2, j, k_2)])] = True

    """Clauses creation : there is one queen max per diagonal NW to SE"""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for i_2 in range(i + 1, n):
                    for m in range(-min(k, j), n - max(k, j)):
                        if not state[frozenset([(i, j, k), (i_2, j + m, k + m)])]:
                            f.write("-" + str(d[(i, j, k)]) + " ")
                            f.write("-" + str(d[(i_2, j + m, k + m)]) + " ")
                            f.write("\n")
                            state[frozenset([(i, j, k), (i_2, j + m, k + m)])] = True

    """Clauses creation : there is one queen max per diagonal NE to SW"""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for i_2 in range(i + 1, n):
                    for m in range(-min(n - k - 1, j), min(k + 1, n - j)):
                        if not state[frozenset([(i, j, k), (i_2, j + m, k - m)])]:
                            f.write("-" + str(d[(i, j, k)]) + " ")
                            f.write("-" + str(d[(i_2, j + m, k - m)]) + " ")
                            f.write("\n")
                            state[frozenset([(i, j, k), (i_2, j + m, k - m)])] = True
    f.close()


f = "../../data/queens/5Q.txt"
queens_generator(5, f)
