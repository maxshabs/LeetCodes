# Solution for LeetCode Problem 283. Move Zeroes
# Time Complexity: O(n) where n is the size of the input array
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        non_zero_ptr = 0
        len_of_nums = len(nums)
        for i in range(len_of_nums):
            if nums[zero_ptr] != 0:
                zero_ptr += 1
                if zero_ptr >= len_of_nums:
                    break
            if nums[non_zero_ptr] == 0 or zero_ptr > non_zero_ptr:
                non_zero_ptr += 1
                if non_zero_ptr >= len_of_nums:
                    break
            if nums[zero_ptr] == 0 and nums[non_zero_ptr] != 0 and zero_ptr < non_zero_ptr:
                temp = nums[zero_ptr]
                nums[zero_ptr] = nums[non_zero_ptr]
                nums[non_zero_ptr] = temp
