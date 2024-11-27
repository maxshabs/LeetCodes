# Solution for LeetCode Problem 1961. Check If String Is a Prefix of Array
# Time Complexity: O(n) where n is the size of the input array "words"
# Space Complexity: O(1) because we only store 1 variable
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            if word == s[i:i + len(word)]:
                i += len(word)
                if i == len(s):
                    return True
            else:
                return False
        return False