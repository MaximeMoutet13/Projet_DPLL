import unittest

from source.model import load


class TestLoad(unittest.TestCase):

    def test_3_clauses(self):
        file_path = "../data/test2.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = [[0], [0], [2], [2], [1], [1]]
        clause_expected = [[0, 1], [4, 5], [2, 3]]

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)

    def test_5_clauses(self):
        file_path = "../data/test.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = [[0, 2], [2], [0], [3], [4], [1], [2, 3], [], [3], [1]]
        clause_expected = [[0, 2], [5, 9], [1, 0, 6], [3, 6, 8], [4]]

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)

    def test_2_clauses(self):
        file_path = "../data/test3.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        literal_expected = [[0], [1]]
        clause_expected = [[0], [1]]

        self.assertEqual(literal, literal_expected)
        self.assertEqual(clause, clause_expected)
