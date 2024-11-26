# Solution for LeetCode Problem 11. Container with the most water
# Time Complexity: O(n) where n is the size of the input array "heights"
# Space Complexity: O(1) because we only store 3 variables
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        cur_water = 0
        while j > i:
            if cur_water < min(height[i], height[j]) * (j - i):
                cur_water = min(height[i], height[j]) * (j - i)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return cur_water
