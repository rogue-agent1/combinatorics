#!/usr/bin/env python3
"""Combinatorics utilities. Zero dependencies."""
import math

def factorial(n):
    if n < 0: raise ValueError
    r = 1
    for i in range(2, n + 1): r *= i
    return r

def nCr(n, r):
    if r < 0 or r > n: return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    if r < 0 or r > n: return 0
    return factorial(n) // factorial(n - r)

def catalan(n):
    return nCr(2*n, n) // (n + 1)

def derangements(n):
    if n == 0: return 1
    if n == 1: return 0
    a, b = 1, 0
    for i in range(2, n + 1): a, b = b, (i - 1) * (a + b)
    return b

def stirling2(n, k):
    """Stirling numbers of the second kind."""
    if n == 0 and k == 0: return 1
    if n == 0 or k == 0: return 0
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            dp[i][j] = j * dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]

def bell(n):
    if n == 0: return 1
    return sum(stirling2(n, k) for k in range(1, n+1))

def generate_permutations(arr):
    if len(arr) <= 1: return [arr[:]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            result.append([arr[i]] + p)
    return result

def generate_combinations(arr, r):
    if r == 0: return [[]]
    if not arr: return []
    with_first = [[arr[0]] + c for c in generate_combinations(arr[1:], r-1)]
    without = generate_combinations(arr[1:], r)
    return with_first + without

if __name__ == "__main__":
    print(f"C(10,3)={nCr(10,3)}, P(10,3)={nPr(10,3)}")
