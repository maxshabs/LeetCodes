# Solution for LeetCode problem 434: Number of Segments in a String
# Time Complexity: O(n), where n is the length of the input string s
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
