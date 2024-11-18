# Solution for LeetCode Problem 334. Increasing Triplet Subsequence
# Time Complexity: O(n) where n is the size of the input list
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')  # Smallest number seen so far
        second = float('inf') # Second smallest number after 'first'

        for num in nums:
            if num <= first:
                first = num  # Update smallest number
            elif num <= second:
                second = num  # Update second smallest number
            else:
                return True  # Triplet found

        return False  # No triplet found