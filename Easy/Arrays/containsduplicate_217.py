# Solution for LeetCode Problem 217. Contains Duplicate
# Time Complexity: O(n), where n is the size of the input array "nums"
# Space Complexity: O(n), because the worst case is that all of the numbers are in the set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
