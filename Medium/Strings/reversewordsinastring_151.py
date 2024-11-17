# Solution for LeetCode Problem 151: Reverse Words in a String
# Time Complexity: O(n) where n is the size of the input string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_split = s.split()
        s_split.reverse()
        return " ".join(s_split)
