# Solution for LeetCode Problem 392. Is Subsequence
# Time Complexity: O(n) where n is the size of the input string "s"
# Space Complexity: O(1) because we only store one variable
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_ptr = 0
        for c in t:
            if s[s_ptr] == c:
                s_ptr += 1
                if s_ptr == len(s):
                    return True
        return False
