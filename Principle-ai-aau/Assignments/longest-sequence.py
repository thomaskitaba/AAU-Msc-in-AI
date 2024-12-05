#!/usr/bin/python3 
# Using Dynamic Programing

def longestIncreasingSubsequence(a):
    """
    find the length of the longest increasing subsequence
    """
    seq = [1] * len(a)
    # loop across the sequence
    for i in range(1, len(a)):
        for j in range(i):
            if a[j] < a[i]:
                # set max seq value currently available
                seq[i] = max(seq[i], seq[j] + 1)
                # not when arr[i] = 10 and arr[j] = 4
                # that is where we need the max
    print(max(seq))

if __name__ == "__main__":
    array = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    longestIncreasingSubsequence(array)
