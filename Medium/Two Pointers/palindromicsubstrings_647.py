# Solution for LeetCode Problem 647: Palindromic Substrings
# Time Complexity: O(n^2), where n is the length of the string `s`.
# - For each character in the string, we expand outward to find palindromic substrings.
# Space Complexity: O(1), as no additional data structures are used beyond variables.

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the total number of palindromic substrings in the given string.

        :param s: Input string
        :return: Total number of palindromic substrings
        """
        result = 0
        len_s = len(s)
        
        # Iterate over each character in the string to find palindromes centered at each position.
        for i in range(len_s):
            # Count odd-length palindromes centered at `i`.
            result += self.count(s, i, i)
            # Count even-length palindromes centered between `i` and `i + 1`.
            result += self.count(s, i, i + 1)
        
        return result
    
    def count(self, s: str, l: int, r: int) -> int:
        """
        Expands outward from the center to count palindromic substrings.

        :param s: Input string
        :param l: Left pointer
        :param r: Right pointer
        :return: Number of palindromic substrings found in this expansion
        """
        result = 0
        len_s = len(s)
        
        # Expand as long as the substring remains a palindrome.
        while l >= 0 and r < len_s:
            if s[l] != s[r]:  # Stop if characters at `l` and `r` are not equal.
                break
            result += 1  # Increment the count for a valid palindrome.
            l -= 1  # Move left pointer outward.
            r += 1  # Move right pointer outward.
        
        return result
