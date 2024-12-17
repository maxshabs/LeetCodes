# Solution for LeetCode Problem 3090: Maximum Length of a Substring With At Most Two Occurrences of Each Character
# Time Complexity: O(n), where n is the length of the input string `s`
#   - The sliding window ensures that each character is processed at most twice.
# Space Complexity: O(1), as the `window_count` array has a fixed size of 26 (for lowercase English letters).

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Frequency count array to track the occurrence of characters in the current window
        window_count = [0] * 26

        # Variables to store the maximum length of a valid substring
        max_length = 0

        # Left pointer for the sliding window
        left = 0

        # Length of the input string
        s_len = len(s)

        # Iterate through the string with the right pointer
        for right in range(s_len):
            # Increment the count of the current character in the window
            window_count[ord(s[right]) - 97] += 1

            # If the count of the current character exceeds 2, shrink the window from the left
            while window_count[ord(s[right]) - 97] > 2:
                window_count[ord(s[left]) - 97] -= 1
                left += 1

            # Update the maximum length of a valid substring
            max_length = max(max_length, right - left + 1)

        # Return the maximum length found
        return max_length
