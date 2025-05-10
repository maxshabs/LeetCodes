# Solution for LeetCode Problem 2918: Minimum Equal Sum of Two Arrays After Replacing Zeros
# Time Complexity: O(n + m), where n and m are the lengths of nums1 and nums2
# Space Complexity: O(1), only uses constant extra space

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        sum1 = 0
        sum2 = 0
        zero_count_nums1 = 0
        zero_count_nums2 = 0

        # Replace zeros in nums1 with 1s and count them
        for i in range(n):
            if nums1[i] == 0:
                zero_count_nums1 += 1
                nums1[i] = 1
            sum1 += nums1[i]

        # Replace zeros in nums2 with 1s and count them
        for j in range(m):
            if nums2[j] == 0:
                zero_count_nums2 += 1
                nums2[j] = 1
            sum2 += nums2[j]

        # If one array has a strictly larger sum and the other has no zeros to adjust, return -1
        if sum1 > sum2 and zero_count_nums2 == 0:
            return -1
        if sum2 > sum1 and zero_count_nums1 == 0:
            return -1

        # Return the maximum sum after optimal adjustments
        return max(sum1, sum2)
