#!/usr/bin/env python3
"""Combinatorics: permutations, combinations, partitions, Catalan."""
def factorial(n):
    r=1
    for i in range(2,n+1): r*=i
    return r
def C(n,k):
    if k<0 or k>n: return 0
    return factorial(n)//(factorial(k)*factorial(n-k))
def P(n,k): return factorial(n)//factorial(n-k)
def permutations(lst):
    if len(lst)<=1: return [lst[:]]
    result=[]
    for i in range(len(lst)):
        rest=lst[:i]+lst[i+1:]
        for p in permutations(rest): result.append([lst[i]]+p)
    return result
def combinations(lst,k):
    if k==0: return [[]]
    if not lst: return []
    with_first=[[lst[0]]+c for c in combinations(lst[1:],k-1)]
    without=combinations(lst[1:],k)
    return with_first+without
def partitions(n):
    if n==0: return [[]]
    result=[]
    def _part(n,max_val,current):
        if n==0: result.append(current[:]);return
        for i in range(min(n,max_val),0,-1): current.append(i);_part(n-i,i,current);current.pop()
    _part(n,n,[]);return result
def catalan(n): return C(2*n,n)//(n+1)
def bell(n):
    B=[[0]*(n+1) for _ in range(n+1)];B[0][0]=1
    for i in range(1,n+1):
        B[i][0]=B[i-1][i-1]
        for j in range(1,i+1): B[i][j]=B[i][j-1]+B[i-1][j-1]
    return B[n][0]
def stirling2(n,k):
    if n==0 and k==0: return 1
    if n==0 or k==0: return 0
    return k*stirling2(n-1,k)+stirling2(n-1,k-1)
if __name__=="__main__":
    assert C(10,3)==120;assert P(5,3)==60
    assert len(permutations([1,2,3]))==6
    assert len(combinations([1,2,3,4],2))==6
    assert len(partitions(5))==7
    assert catalan(5)==42;assert bell(5)==52
    print("Combinatorics OK")
