# Solution for LeetCode Problem 4: Median of Two Sorted Arrays
# Time Complexity: O(log(m + n)), where m and n are the lengths of nums1 and nums2.
#   - Binary search is performed on the smaller array to reduce the search space.
# Space Complexity: O(1), as no additional data structures are used apart from variables.

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search space
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            B = nums1
            A = nums2

        # Calculate total length of both arrays and half-length for partitioning
        total_nums_len = len(nums1) + len(nums2)
        half = total_nums_len // 2

        # Binary search variables
        left, right = 0, len(A) - 1

        # Perform binary search
        while True:
            # Partition indices for A and B
            i = (left + right) // 2
            j = half - i - 2

            # Determine left and right values of the partitions
            A_left = float("-infinity")
            if i >= 0:
                A_left = A[i]
            A_right = float("infinity")
            if i + 1 < len(A):
                A_right = A[i + 1]
            B_left = float("-infinity")
            if j >= 0:
                B_left = B[j]
            B_right = float("infinity")
            if j + 1 < len(B):
                B_right = B[j + 1]

            # Check for valid partition
            if A_left <= B_right and A_right >= B_left:
                # If total length is even, median is the average of max(left side) and min(right side)
                if total_nums_len % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                # If total length is odd, median is the minimum of the right side
                else:
                    return min(A_right, B_right)
            # Adjust binary search range
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1
