import unittest

from source.heuristics import mono_literal, pure_literal, literal_choice
from source.model import load


class TestMonoLiteral(unittest.TestCase):
    def test_one_unitary(self):
        file_path = "../data/test.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)
        clause_lenght = [2, 2, 3, 3, 1]

        lit = mono_literal(clause, clause_lenght)
        lit_expected = 4

        self.assertEqual(lit, lit_expected)

    def test_no_unitary(self):
        file_path = "../data/test2.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)
        clause_lenght = [2, 2, 2]

        lit = mono_literal(clause, clause_lenght)
        lit_expected = "No unitary clause"

        self.assertEqual(lit, lit_expected)

    def test_2_unitary(self):
        file_path = "../data/test3.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        clause_lenght = [1, 1]
        lit = mono_literal(clause, clause_lenght)
        lit_expected = 0

        self.assertEqual(lit, lit_expected)


class TestPureLiteral(unittest.TestCase):
    def test_only_pure(self):
        file_path = "../data/test3.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        lit = pure_literal(literal)
        lit_expected = 0

        self.assertEqual(lit, lit_expected)

    def test_no_pure(self):
        file_path = "../data/test2.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        lit = pure_literal(literal)
        lit_expected = "No pure literal"

        self.assertEqual(lit, lit_expected)

    def test_one_pure(self):
        file_path = "../data/test.txt"

        with open(file_path, "r") as f:
            literal, clause = load(f)

        lit = pure_literal(literal)
        lit_expected = 6

        self.assertEqual(lit, lit_expected)
