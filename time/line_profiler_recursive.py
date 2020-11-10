import numpy as np
import line_profiler

from source.model import load
from source.recursive.dpll_recursif import dpll_recursif
from source.heuristics import literal_choice, no_heuristic, first_satisfy, first_fail

func_test = dpll_recursif


class dpll:
    def __init__(self, literal, clause):
        self.g = literal
        self.s = clause

    def time_dpll(self):
        g = self.g
        s = self.s
        t = func_test(first_satisfy, s, g)


def main(params, n_runs=4):
    for i in range(n_runs):
        print('Run', i)
        n = np.random.randint(0, 3)
        res = dpll(params[n][0], params[n][1])
        res.time_dpll()


if __name__ == '__main__':
    path_file_1 = "../data/5p4P.txt"
    f_1 = open(path_file_1, "r")
    literal_1, clause_1 = load(f_1)

    path_file_2 = "../data/6p5P.txt"
    f_2 = open(path_file_2, "r")
    literal_2, clause_2 = load(f_2)

    path_file_3 = "../data/7p6P.txt"
    f_3 = open(path_file_3, "r")
    literal_3, clause_3 = load(f_3)

    my_params = [(literal_1, clause_1), (literal_2, clause_2), (literal_3, clause_3)]

    lp = line_profiler.LineProfiler()
    lp.add_function(func_test)
    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'profile_generation.lprof'
    lp.dump_stats(stats_file)
    print('Run the following command to display the results:')
    print('$ python -m line_profiler {}'.format(stats_file))
