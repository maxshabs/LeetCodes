# Solution for LeetCode Problem 5: Longest Palindromic Substring
# Time Complexity: O(n^2), where n is the length of the string. For each character, we expand outward to find palindromes.
# Space Complexity: O(1), as no additional data structures are used beyond variables.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the given string.

        :param s: Input string
        :return: Longest palindromic substring
        """
        # `max_i_val` stores the start index and length of the longest palindromic substring found.
        max_i_val = (0, 0)
        
        # Iterate through each character in the string, treating it as the potential middle of a palindrome.
        for mid in range(len(s)):
            # Case 1: Check for even-length palindrome centered between `mid` and `mid + 1`.
            i, j = mid, mid + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_i_val[1]:
                    max_i_val = (i, j - i + 1)  # Update start index and length.
                i -= 1
                j += 1
            
            # Case 2: Check for odd-length palindrome centered at `mid`.
            i, j = mid, mid
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_i_val[1]:
                    max_i_val = (i, j - i + 1)  # Update start index and length.
                i -= 1
                j += 1
        
        # Extract the longest palindromic substring using the stored indices and length.
        return s[max_i_val[0]:max_i_val[0] + max_i_val[1]]
