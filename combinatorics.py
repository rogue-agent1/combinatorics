#!/usr/bin/env python3
"""Combinatorics — permutations, combinations, partitions, derangements."""
import sys, math
from itertools import permutations as perm_iter, combinations as comb_iter

def nPr(n, r): return math.factorial(n) // math.factorial(n-r)
def nCr(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
def derangements(n):
    if n == 0: return 1
    if n == 1: return 0
    return (n-1) * (derangements(n-1) + derangements(n-2))
def catalan(n): return nCr(2*n, n) // (n+1)
def stirling2(n, k):
    if n == k: return 1
    if k == 0 or k > n: return 0
    return k * stirling2(n-1, k) + stirling2(n-1, k-1)
def bell(n):
    return sum(stirling2(n, k) for k in range(n+1))
def partitions(n, max_val=None):
    if max_val is None: max_val = n
    if n == 0: return 1
    if n < 0 or max_val == 0: return 0
    return partitions(n - max_val, max_val) + partitions(n, max_val - 1)

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"n = {n}")
    print(f"  P({n},3) = {nPr(n,3)}")
    print(f"  C({n},3) = {nCr(n,3)}")
    print(f"  {n}! = {math.factorial(n)}")
    print(f"  D({n}) derangements = {derangements(n)}")
    print(f"  Catalan({n}) = {catalan(n)}")
    print(f"  Bell({n}) = {bell(n)}")
    print(f"  Partitions({n}) = {partitions(n)}")
    print(f"\nCatalan numbers: {[catalan(i) for i in range(12)]}")
