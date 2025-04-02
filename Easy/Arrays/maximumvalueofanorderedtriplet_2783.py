# Solution for LeetCode Problem 2873: Maximum Value of an Ordered Triplet I
# Time Complexity: O(N), where N is the length of the input list `nums`
# Space Complexity: O(1), uses constant space

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_dif = 0     # Stores the maximum value of (nums[i] - nums[j]) seen so far
        max_i = 0       # Tracks the maximum value of nums[i] seen so far
        result = 0      # Stores the maximum triplet value found

        for num in nums:
            # Update the result using the best (nums[i] - nums[j]) * nums[k] so far
            result = max(result, max_dif * num)

            # Update max_dif by trying (max_i - num), simulating nums[i] - nums[j]
            max_dif = max(max_dif, max_i - num)

            # Update max_i with the maximum value encountered so far
            max_i = max(max_i, num)

        return result
