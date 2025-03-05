# Solution for LeetCode Problem 1657: Determine if Two Strings Are Close
# Time Complexity: O(N + M + 26 log 26) ≈ O(N), where:
#   - N is the length of word1 and M is the length of word2.
#   - We iterate through both strings to compute frequency (O(N + M)).
#   - Sorting the frequency arrays takes O(26 log 26) ≈ O(1), as there are only 26 letters.
# Space Complexity: O(1), as we use fixed-size frequency arrays of size 26.

from typing import List

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Determines if two words are 'close'. Two words are close if:
        1. They have the same unique characters.
        2. The frequency of characters can be rearranged to match.

        Parameters:
        word1 (str): The first input string.
        word2 (str): The second input string.

        Returns:
        bool: True if the words are close, False otherwise.
        """
        # Frequency arrays to store the count of each character (a-z)
        freq_word1 = [0] * 26
        freq_word2 = [0] * 26

        # Count the frequency of each character in word1
        for ch in word1:
            freq_word1[ord(ch) - ord('a')] += 1

        # Count the frequency of each character in word2
        for ch in word2:
            freq_word2[ord(ch) - ord('a')] += 1

        # Step 1: Check if both words contain the same set of unique characters
        for i in range(26):
            if (freq_word1[i] == 0 and freq_word2[i] != 0) or (freq_word2[i] == 0 and freq_word1[i] != 0):
                return False  # If a character is present in one string but not the other, return False

        # Step 2: Sort and compare the frequency lists
        freq_word1.sort()
        freq_word2.sort()

        # Check if sorted frequency distributions are identical
        for i in range(26):
            if freq_word1[i] != freq_word2[i]:
                return False  # If character frequencies do not match, return False

        return True  # The words are close
