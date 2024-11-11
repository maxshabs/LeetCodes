# Solution for LeetCode Problem 1768. Merge Strings Alternately
# Time Complexity: O(n + m), where n is the length of the input string word1, and m is the length of input string word2
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = []
        i, j = 0, 0
        word1len = len(word1)
        word2len = len(word2)
        while i < word1len or j < word2len:
            if i < word1len:
                s.append(word1[i])
                i += 1
            if j < word2len:
                s.append(word2[j])
                j += 1
        return "".join(s)