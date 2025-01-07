# Solution for LeetCode Problem 300: Longest Increasing Subsequence
# Time Complexity: O(n^2), where n is the length of the input array.
# Space Complexity: O(n), due to the auxiliary array used for dynamic programming.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest increasing subsequence (LIS) in a given list of numbers.

        :param nums: List[int] - The input list of numbers.
        :return: int - The length of the LIS.
        """
        arr = [1] * len(nums)
        len_nums = len(nums)
        
        # Compute the LIS length for each index
        for i in range(len_nums):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[i], arr[j] + 1)
        
        # Return the maximum LIS length
        return max(arr)
