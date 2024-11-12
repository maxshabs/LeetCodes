# Solution for LeetCode Problem 1071: Greatest Common Divisor of Strings
# Time Complexity: O(min(n, m)^2), where n is the length of str1 and m is the length of str2
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1_len = len(str1)
        str2_len = len(str2)
        if str1_len <= str2_len:
            gcd = str1
        else:
            gcd = str2

        while True:
            gcd_len = len(gcd)
            if gcd_len == 0:
                return ""
            if str1_len % gcd_len != 0 or str2_len % gcd_len != 0:
                gcd = gcd[:-1]
                continue
            if (gcd * (str1_len // gcd_len) == str1 and
                    gcd * (str2_len // gcd_len) == str2):
                break
            gcd = gcd[:-1]
        return gcd
