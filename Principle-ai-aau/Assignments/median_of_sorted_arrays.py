#!/usr/bin/python3
"""
Given two sorted arrays nums1 and nums2, find the median of the two sorted arrays
"""
def MedianOfSortedArray(nums1, nums2):
    
    A, B = nums1, nums2
    # for ease of use make the smaller A and the larger B
    if len(B) < len(A):
        A, B = B, A
    # calculate total and half of the combined list
    total = len(A) + len(B)
    half = total // 2
    
    l, r = 0, len(A) - 1  # left and right of A
    # claculate center of A and B that make up half of the total
    
    while True:
        i = (l + r) // 2  # half of A
        # j + 1 + i + 1 = half
        j = half - i - 2 # half of B
    
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
        
        # check if the partition is valid
        if Aleft <= Bright and Bleft <= Aright: 
            # find median for odd total
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(MedianOfSortedArray(nums1, nums2))
