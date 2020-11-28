import matplotlib.pyplot as plt
from time import time

from source.iterative.dpll_iterative import dpll
from source.model import load
from source.heuristics import no_heuristic, first_satisfy, first_fail


def time_comparison(problem_sizes):
    times_no_heuristic = []
    times_first_satisfy = []
    times_first_fail = []

    for i in problem_sizes:
        path_file = "../data/queens_bis/{0}Q.txt".format(i)
        f = open(path_file, "r")
        literal, clause = load(f)

        start = time()
        dpll(literal, clause, first_satisfy)
        times_first_satisfy.append(time() - start)

        start = time()
        dpll(literal, clause, first_fail)
        times_first_fail.append(time() - start)

        start = time()
        dpll(literal, clause, no_heuristic)
        times_no_heuristic.append(time() - start)

    # plt.figure()
    # plt.title("Dames: temps des différentes heuristiques")
    # plt.xlabel("Taille du problème")
    # plt.ylabel("Temps (s)")
    # plt.plot(problem_sizes, times_no_heuristic, label="No heuristic")
    # plt.plot(problem_sizes, times_first_satisfy, label="First satisfy")
    # plt.plot(problem_sizes, times_first_fail, label="First fail")
    # plt.legend(loc='best')
    # plt.savefig("images/queens_heuristics.png")
    # plt.show()


def tree_comparison(problem_sizes):
    nodes_no_heuristic = []
    nodes_first_satisfy = []
    nodes_first_fail = []

    for i in problem_sizes:
        path_file = "../data/pigeon_hole/{0}Q.txt".format(i)
        f = open(path_file, "r")

        literal, clause = load(f)

        mod1, n1 = dpll(literal, clause, first_satisfy)
        mod2, n2 = dpll(literal, clause, first_fail)
        mode3, n3 = dpll(literal, clause, no_heuristic)

        nodes_first_satisfy.append(n1)
        nodes_first_fail.append(n2)
        nodes_no_heuristic.append(n3)

    # plt.figure()
    # plt.title("Dames: taille des arbres")
    # plt.xlabel("Taille du problème")
    # plt.ylabel("Nombre de noeuds")
    # plt.plot(problem_sizes, nodes_no_heuristic, label="No heuristic")
    # plt.plot(problem_sizes, nodes_first_satisfy, label="First satisfy")
    # plt.plot(problem_sizes, nodes_first_fail, label="First fail")
    # plt.legend(loc='best')
    # plt.savefig("images/queens_tree.png")
    # plt.show()

size = [2, 3, 4, 5, 6, 7, 8]
