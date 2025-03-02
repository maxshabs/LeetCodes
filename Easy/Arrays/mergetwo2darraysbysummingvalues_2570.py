# Solution for LeetCode Problem 2570: Merge Two 2D Arrays by Summing Values
# Time Complexity: O(N + M), where N and M are the lengths of nums1 and nums2, respectively.
#   - We traverse both arrays once using a two-pointer approach.
# Space Complexity: O(N + M), as we store the merged result in a new list.

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []  # Result array to store merged values
        i, j = 0, 0  # Pointers for nums1 and nums2
        
        # Merge process using two-pointer technique
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:  # Matching keys, sum values
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:  # nums1 has a smaller key, add it to result
                res.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:  # nums2 has a smaller key, add it to result
                res.append([nums2[j][0], nums2[j][1]])
                j += 1
        
        # Append any remaining elements from nums1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        # Append any remaining elements from nums2
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        
        return res  # Return the merged sorted array
