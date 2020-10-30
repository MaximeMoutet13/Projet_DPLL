import unittest

from source.dpll_functions import simplify_clause, update_literal_state, is_satisfied
from source.model import load, initialisation
from source.heuristics import literal_choice


class TestSimplifyClause(unittest.TestCase):
    def test_one_simplification(self):
        file_path = "../data/test3.txt"
        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)
        lit = literal_choice(clause, clause_lenght, literal, literal_state)
        c, cs, cl, l = simplify_clause(clause, clause_state, clause_lenght, literal, lit)

        self.assertTrue(c == {1: {2}})
        self.assertTrue(cs == [1, 0])
        self.assertTrue(cl == [0, 1])
        self.assertTrue(l == {0: set(), 1: set(), 2: {1}, 3: set()})

    def test_one_simplification2(self):
        file_path = "../data/test2.txt"
        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)
        lit = literal_choice(clause, clause_lenght, literal, literal_state)
        c, cs, cl, l = simplify_clause(clause, clause_state, clause_lenght, literal, lit)

        self.assertTrue(c == {1: {4, 5}, 2: {2, 3}})
        self.assertTrue(cs == [1, 0, 0])
        self.assertTrue(cl == [0, 2, 2])
        self.assertTrue(l == {0: set(), 1: set(), 2: {2}, 3: {2}, 4: {1}, 5: {1}})

    def test_simplify(self):
        file_path = "../data/test.txt"
        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_state, clause_state, clause_lenght, running_literal = initialisation(literal, clause)
        lit = literal_choice(clause, clause_lenght, literal, literal_state)
        c, cs, cl, l = simplify_clause(clause, clause_state, clause_lenght, literal, lit)

        self.assertTrue(c == {0: {0, 2}, 1: {9}, 2: {0, 1, 6}, 3: {3, 6, 8}})
        self.assertTrue(cs == [0, 0, 0, 0, 1])
        self.assertTrue(cl == [2, 1, 3, 3, 0])
        self.assertTrue(
            l == {0: {0, 2}, 1: {2}, 2: {0}, 3: {3}, 4: set(), 5: set(), 6: {2, 3}, 7: set(), 8: {3}, 9: {1}})


# class TestIsSatisfied(unittest.TestCase):
