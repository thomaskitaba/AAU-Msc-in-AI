#!/usr/bin/python3

"""
create max heap from 
the given area
"""

A = [1, 14, 10, 8, 7, 9, 3, 2, 4, 16]

def hipify(A, n, i):
    max = i 
    l = 2*i + 1   # since it is zero based
    r = 2*i + 2   # since it is zero based
    
    if l < n and A[l] > A[max]:
        max = l 
    if r < n and A[r] > A[max]:
        max = r  
    if max != i:
        A[i], A[max] = A[max], A[i]
        # recures over the affected index
        hipify(A, n, max)
def heapsort(A):
    n = len(A)
    # start from last non leaf node and go back to the top root node
    for i in range(n//2 - 1, -1, -1):
        hipify(A, n, i)
heapsort(A)
print(A)

# inplace ,     O(n log n)
