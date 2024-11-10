# Solution for LeetCode problem 482: License Key Formatting
# Time Complexity: O(n), where n is the length of the input string s
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = (s[::-1].replace("-", "")).upper()
        substrings = [s[i: i + k][::-1] for i in range (0, len(s), k)]
        return "-".join(substrings[::-1])
        
