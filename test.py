from combinatorics import factorial, nCr, nPr, catalan, derangements, stirling2, bell, generate_permutations, generate_combinations
assert factorial(5) == 120
assert nCr(10, 3) == 120
assert nPr(10, 3) == 720
assert nCr(5, 0) == 1
assert catalan(5) == 42
assert derangements(4) == 9
assert stirling2(4, 2) == 7
assert bell(4) == 15
perms = generate_permutations([1,2,3])
assert len(perms) == 6
combs = generate_combinations([1,2,3,4], 2)
assert len(combs) == 6
print("combinatorics tests passed")
