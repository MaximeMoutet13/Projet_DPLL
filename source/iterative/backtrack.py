from source.iterative.dpll_iterative_functions import update_clause
from source.heuristics import conjugate_literal


def backtrack(literal, clause, literal_state, running_literal):
    go_up = True
    next_lit = None

    while go_up:
        current_literal = running_literal.pop()
        no_current_literal = conjugate_literal(current_literal)

        if literal_state[no_current_literal] == 0:
            go_up = False
            next_lit = no_current_literal

        else:
            if len(running_literal) == 0:
                go_up = False
                next_lit = None

            else:
                literal_state[current_literal] = 0
                literal_state[no_current_literal] = 0

    clause_state, clause_lenght = reconstruct(literal, clause, running_literal)

    return next_lit, clause_state, clause_lenght


def reconstruct(literal, clause, pile):
    cl = [len(c) for c in clause]
    cs = [0 for i in range(len(clause))]

    for v in pile:
        update_clause(literal, cs, cl, v)

    return cs, cl

# def backtrack(literal, literal_state, clause, clause_state, clause_lenght, running_literal):
#     loop = True
#     lit = None
#     if len(running_literal) == 0:
#         loop = False
#
#     else:
#         stop_backtrack = False,
#         while stop_backtrack[0] is False:
#             if len(running_literal) == 0:
#                 loop = False
#                 return loop, literal_state, clause_state, clause_lenght, None
#             stop_backtrack = up_node(literal_state, running_literal)
#         lit = stop_backtrack[1]
#         literal_state, clause_state, clause_lenght = reconstruct(literal, literal_state, clause, running_literal, lit)
#     return loop, literal_state, clause_state, clause_lenght, lit
#
#
# def up_node(literal_state, running_literal):
#     lit = running_literal.pop()
#     not_lit = conjugate_literal(lit)
#
#     if literal_state[not_lit] == 0:
#         return True, not_lit
#
#     return False, lit
#
#
# def reconstruct(literal, literal_state, clause, running_literal, lit):
#     new_literal_state, new_clause_state, new_clause_lenght = initialisation(literal, clause)
#     for i in range(len(running_literal)):
#         current_literal = running_literal[i]
#         update_literal_state(new_literal_state, current_literal)
#         update_clause(literal, new_clause_state, new_clause_lenght, current_literal)
#         if current_literal % 2 == 0:
#             new_literal_state[current_literal + 1] = literal_state[current_literal + 1]
#         else:
#             new_literal_state[current_literal - 1] = literal_state[current_literal - 1]
#
#     if lit % 2 == 0:
#         new_literal_state[lit + 1] = literal_state[lit + 1]
#     else:
#         new_literal_state[lit - 1] = literal_state[lit - 1]
#     return new_literal_state, new_clause_state, new_clause_lenght


# def reconstruct_better(literal, clause, literal_state, clause_state, clause_lenght, lit, running_literal):
#     no_lit = conjugate_literal(lit)
#     printf = False
#     if lit == 3:
#         printf = True
#     if printf:
#         print("///////////////")
#         print("no_lit", no_lit)
#     for c in literal[lit]:
#         clause_state[c] = 0
#         if printf: print("c:", c)
#
#         for l in clause[c]:
#             if printf: print("l:", l)
#
#             if l == lit:
#                 clause_lenght[c] += 1
#
#             elif l != no_lit:
#                 if literal_state[l] == 1:
#                     if l in running_literal:
#                         clause_state[c] = 1
#                         clause_lenght[c] = 0
#                         break
#
#                 else:
#                     clause_lenght[c] += 1
#
#     for c in literal[no_lit]:
#         if clause_state[c] == 0:
#             clause_lenght[c] += 1
#
#     if printf:
#         print("cs:", clause_state)
#         print("cl:", clause_lenght)
#         print("ls:", literal_state)
#         print("///////////////")
