# Solution for LeetCode Problem 2444: Count Subarrays With Fixed Bounds
# Time Complexity: O(n), where n is the length of nums
# Space Complexity: O(1), using only a few pointers

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0                   # Total number of valid subarrays
        mini, maxi, validi = -1, -1, -1  # Track the latest positions:
                                        # mini  → last position of minK
                                        # maxi  → last position of maxK
                                        # validi → last position of invalid element (out of bounds)

        for i in range(len(nums)):
            # If the number is out of bounds, reset the valid subarray start
            if nums[i] < minK or nums[i] > maxK:
                validi = i

            # Update latest position of minK and maxK
            if nums[i] == maxK:
                maxi = i
            if nums[i] == minK:
                mini = i

            # The number of valid subarrays ending at i is the distance between
            # the earliest occurrence of both minK and maxK after the last invalid index
            count += max(0, min(maxi, mini) - validi)

        return count
