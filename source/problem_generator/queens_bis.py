def queens_bis_generator(n, f):
    """Queens problem generator, for n queens on a n x n chessboard. Queens are indistinguishable"""

    f = open(f, "w")
    d = {}
    nb_literal = 0

    """Variables and State creation"""
    for i in range(n):
        for j in range(n):
            f.write(str(nb_literal) + " ")
            d[(i, j)] = nb_literal
            nb_literal += 1
    f.write("\n")
    f.write("\n")

    """Clauses creation : a queen is in one and only one case"""
    for i in range(n):
        for j in range(n):
            f.write(str(d[(i, j)]) + " ")
        f.write("\n")
        for j in range(n):
            for k in range(j + 1, n):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(i, k)]) + " ")
                f.write("\n")

    """Clauses creation : there is one queen max per line"""
    for j in range(n):
        for i in range(n):
            for k in range(i + 1, n):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(k, j)]) + " ")
                f.write("\n")

    """Clauses creation : there is one queen max per diagonal NW to SE"""
    for i in range(n):
        for j in range(n):
            for m in range(-min(i, j), n - max(i, j)):
                if m != 0 :
                    f.write("-" + str(d[(i, j)]) + " ")
                    f.write("-" + str(d[(i + m, j + m)]) + " ")
                    f.write("\n")

    """Clauses creation : there is one queen max per diagonal NE to SW"""
    for i in range(n):
        for j in range(n):
            for m in range(-min(i, n - j - 1), min(n - i, j + 1)):
                if m != 0 :
                    f.write("-" + str(d[(i, j)]) + " ")
                    f.write("-" + str(d[(i + m, j - m)]) + " ")
                    f.write("\n")
    f.close()


f = "../../data/queens_bis/8Q.txt"
queens_bis_generator(8, f)
