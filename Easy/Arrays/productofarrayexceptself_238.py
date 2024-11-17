# Solution for LeetCode Problem 238. Product of Array Except Self
# Time Complexity: O(n) where n is the size of the input list
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        ret_arr = [1] * nums_len
        prefix_prod = 1
        # Step 1: Calculate prefix products
        for i in range(nums_len):
            ret_arr[i] = prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        # Step 2: Calculate suffix products and multiply with prefix products
        for i in range(nums_len - 1, -1, -1):
            ret_arr[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ret_arr
