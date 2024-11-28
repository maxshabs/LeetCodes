# Solution for LeetCode Problem 643: Maximum Average Subarray I
# Time Complexity: O(n), where n is the size of the input array "nums"
# Space Complexity: O(1), as we only use two variables to track current and maximum sums

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1: Calculate the sum of the first 'k' elements
        cur_avg = max_avg = sum(nums[:k])
        
        # Determine the number of iterations required for the loop
        loop_len = len(nums) - (k - 1)
        
        # Step 2: Use a sliding window to find the maximum sum of any subarray of size 'k'
        for i in range(1, loop_len):
            # Update the current sum by subtracting the element leaving the window
            # and adding the element entering the window
            cur_avg += nums[k + i - 1] - nums[i - 1]
            
            # Update the maximum sum if the current sum is greater
            if cur_avg > max_avg:
                max_avg = cur_avg
        
        # Step 3: Return the maximum average (maximum sum divided by k)
        return max_avg / k
