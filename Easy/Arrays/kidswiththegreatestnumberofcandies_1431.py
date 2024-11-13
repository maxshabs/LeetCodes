# Solution for LeetCode Problem 1431: Kids With the Greatest Number of Candies
# Time Complexity: O(n), where n is the size of the candies array
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_value = max(candies) - extraCandies
        for i in range(0, len(candies)):
            if candies[i] >= max_value:
                candies[i] = True
            else:
                candies[i] = False
        return candies