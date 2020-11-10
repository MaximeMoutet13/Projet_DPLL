def pigeon_generator(n, m, f):
    f = open(f, "w")
    d = {}
    nb_literal = 0
    for i in range(n):
        for j in range(m):
            f.write(str(nb_literal) + " ")
            d[(i, j)] = nb_literal
            nb_literal += 1
    f.write("\n")
    f.write("\n")

    for i in range(n):
        for j in range(m):
            f.write(str(d[(i, j)]) + " ")
        f.write("\n")
        for j in range(m):
            for k in range(j + 1, m):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(i, k)]) + " ")
                f.write("\n")

    for j in range(m):
        for i in range(n):
            for k in range(i + 1, n):
                f.write("-" + str(d[(i, j)]) + " ")
                f.write("-" + str(d[(k, j)]) + " ")
                f.write("\n")
    f.close()


f = "../../data/2p2P.txt"
pigeon_generator(2, 2, f)
