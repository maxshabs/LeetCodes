# Solution for LeetCode Problem 283. Move Zeroes
# Time Complexity: O(n) where n is the size of the input array
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] != 0:
                nums[non_zero_ptr], nums[i] = nums[i], nums[non_zero_ptr]
                non_zero_ptr += 1
