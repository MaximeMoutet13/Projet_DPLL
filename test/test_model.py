import unittest

from source.model import load


class TestLoad(unittest.TestCase):

    def test_3_clauses(self):
        file_path = "../data/test2.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = {0: {0}, 1: {0}, 2: {2}, 3: {2}, 4: {1}, 5: {1}}
        clause_expected = {0: {0, 1}, 1: {4, 5}, 2: {2, 3}}

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)

    def test_5_clauses(self):
        file_path = "../data/test.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = {0: {0, 2}, 1: {2}, 2: {0}, 3: {3}, 4: {4}, 5: {1}, 6: {2, 3}, 7: set(), 8: {3}, 9: {1}}
        clause_expected = {0: {0, 2}, 1: {5, 9}, 2: {0, 1, 6}, 3: {3, 6, 8}, 4: {4}}

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)

    def test_2_clauses(self):
        file_path = "../data/test3.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = {0: {0}, 1: {1}}
        clause_expected = {0: {0}, 1: {1}}

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)
