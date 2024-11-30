# Solution for LeetCode Problem 1004. Max Consecutive Ones III
# Time Complexity: O(n), where n is the size of the input array "nums"
# Space Complexity: O(1), as we only use two pointers
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        nums_len = len(nums)
        while right < nums_len:
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        return right - left
