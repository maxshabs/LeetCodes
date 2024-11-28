# Solution for LeetCode Problem 643. Maximum Average Subarray I
# Time Complexity: O(n) where n is the size of the input array "nums"
# Space Complexity: O(1) because we only store 2 variables
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_avg = max_avg = sum(nums[:k])
        loop_len = len(nums) - (k - 1)
        for i in range(1, loop_len):
            cur_avg += nums[k + i - 1] - nums[i - 1] 
            if cur_avg > max_avg:
                max_avg = cur_avg
        return max_avg / k
