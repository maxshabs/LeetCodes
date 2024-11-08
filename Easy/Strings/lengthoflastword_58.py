# Solution for LeetCode Problem 58: Length of Last Word
# Time Complexity: O(n), where n is the length of the input string s
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        last_word_length = 0
        s = s.lstrip()
        for character in s:
            if character == " ":
                break
            last_word_length += 1
        return last_word_length
