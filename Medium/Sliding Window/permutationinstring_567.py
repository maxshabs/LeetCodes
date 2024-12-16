# Solution for LeetCode Problem 567: Permutation in String
# Time Complexity: O(n), where n is the length of the input string `s2`
#   - The initial counting of characters takes O(s1).
#   - The sliding window iterates through `s2` once, making it O(n).
# Space Complexity: O(1), since the `s1_count` and `s2_count` lists always have a fixed size of 26.

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length of the window to search for in s2
        window_size = len(s1)

        # If s1 is longer than s2, it's impossible to find a permutation
        if window_size > len(s2):
            return False

        # Frequency count arrays for s1 and the current window in s2
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Populate the frequency arrays for s1 and the first window of s2
        for i in range(window_size):
            s1_count[ord(s1[i]) - 97] += 1
            s2_count[ord(s2[i]) - 97] += 1

        # Count how many character frequencies match between s1_count and s2_count
        current_matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                current_matches += 1

        # Sliding window approach
        left = 0
        for right in range(window_size, len(s2)):
            # If all 26 character frequencies match, we found a valid permutation
            if current_matches == 26:
                return True

            # Add the character at the right pointer to the window
            index = ord(s2[right]) - 97
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                current_matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                current_matches -= 1

            # Remove the character at the left pointer from the window
            index = ord(s2[left]) - 97
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                current_matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                current_matches -= 1

            # Move the left pointer to maintain the window size
            left += 1

        # Check for a match in the final window
        return current_matches == 26
